import logging
from collections.abc import Generator
from typing import Any, ClassVar

from ply import lex, yacc


class MemoryLexer:

    # List of keywords
    keywords: ClassVar[dict[str, str]] = {
        "mul": "MUL",
        "do": "DO",
        "don't": "DONT",
    }

    # List of token names.
    tokens = (
        "COMMA",
        "INVALID",
        "LPAREN",
        "NUMBER",
        "RPAREN",
        *keywords.values(),
    )

    # Regular expression rules for simple tokens
    t_COMMA = r","  # noqa: N815
    t_INVALID = r"dummy-invalid-token"  # noqa: N815
    t_MUL = r"mul"  # noqa: N815
    t_DO = r"do"  # noqa: N815
    t_DONT = r"don't"  # noqa: N815
    t_LPAREN = r"\("  # noqa: N815
    t_RPAREN = r"\)"  # noqa: N815

    # Build the lexer
    def __init__(self, **kwargs: Any) -> None:
        self.lexer = lex.lex(module=self, **kwargs)

    # Regular expression rules for more complicated tokens
    def t_NUMBER(self, t: lex.LexToken) -> lex.LexToken:  # noqa: N802
        r"\d+"
        t.value = int(t.value)
        return t

    # Error handling rule
    def t_error(self, t: lex.LexToken) -> lex.LexToken:
        t.value = t.value[0]
        t.type = "INVALID"
        t.lexer.skip(1)
        return t

    def tokenise(self, data: str) -> Generator[lex.LexToken, None, None]:
        self.lexer.input(data)
        while True:
            tok = self.lexer.token()
            if not tok:
                break
            yield tok


class MemoryParser:
    tokens = MemoryLexer.tokens

    precedence = (
        ("left", "INVALID"),
        ("left", "DO", "DONT", "MUL"),
    )

    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.lexer = MemoryLexer()
        self.parser: yacc.LRParser = yacc.yacc(
            module=self, debuglog=self.logger, write_tables=False
        )
        self.enabled = True

    def p_func_implicit_add(self, p: yacc.YaccProduction) -> None:
        """numexpr : numexpr numexpr"""
        self.logger.debug(f"Performing an implicit add: {p[1]} + {p[2]}")
        p[0] = p[1] + p[2]

    def p_func_enable(self, p: yacc.YaccProduction) -> None:
        """numexpr : DO LPAREN RPAREN"""
        self.logger.info(f"Applying an enable instruction: {p[1]}")
        self.enabled = True
        p[0] = 0

    def p_func_disable(self, p: yacc.YaccProduction) -> None:
        """numexpr : DONT LPAREN RPAREN"""
        self.logger.info(f"Applying a disable instruction: {p[1]}")
        self.enabled = False
        p[0] = 0

    def p_func_multiply(self, p: yacc.YaccProduction) -> None:
        """numexpr : MUL LPAREN NUMBER COMMA NUMBER RPAREN"""
        self.logger.info(
            f"{'Applying' if self.enabled else 'Ignoring'} a multiply instruction: {p[3]} * {p[5]}"
        )
        p[0] = p[3] * p[5] if self.enabled else 0

    def p_numexpr_error(self, p: yacc.YaccProduction) -> None:
        """numexpr : numexpr error"""
        p[0] = p[1]

    def p_error(self, t: lex.LexToken) -> None:
        self.logger.debug(f"Ignoring token {t}")

    def parse(self, input_data: str) -> int:
        return int(self.parser.parse(input_data))
