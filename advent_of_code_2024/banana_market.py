from collections import defaultdict
from itertools import pairwise

from advent_of_code_2024.data_loaders import load_file_as_lines

PriceSequence = tuple[int, int, int, int]


class Buyer:
    def __init__(self, initial_secret: int, n_secrets: int) -> None:
        self.secrets = Buyer.generate_secrets(initial_secret, n_secrets)
        self.prices = [secret % 10 for secret in self.secrets]
        self.price_diffs: list[int] = [None] + [p[1] - p[0] for p in pairwise(self.prices)]  # type: ignore[assignment]
        self.diff_sequences: list[PriceSequence] = [None, None, None, None] + [  # type: ignore[assignment]
            tuple(self.price_diffs[idx : idx + 4])  # type: ignore[misc]
            for idx in range(1, len(self.price_diffs) - 3)
        ]

    @staticmethod
    def generate_secrets(initial_secret: int, n_to_generate: int) -> list[int]:
        secrets = [initial_secret]
        while len(secrets) < n_to_generate + 1:
            next_secret = secrets[-1]
            next_secret ^= next_secret << 6  # multiply by 64 and XOR
            next_secret %= 16777216  # take modulus
            next_secret ^= next_secret >> 5  # divide by 32 and XOR
            next_secret %= 16777216  # take modulus
            next_secret ^= next_secret << 11  # multiply by 2048 and XOR
            next_secret %= 16777216  # take modulus
            secrets.append(next_secret)
        return secrets

    def price_at_sequence(self, sequence: PriceSequence) -> int:
        try:
            return self.prices[self.diff_sequences.index(sequence)]
        except (IndexError, ValueError):
            return 0


class BananaMarket:
    def __init__(self, filename: str, n_secrets: int = 2000) -> None:
        self.buyers = [
            Buyer(int(line.strip()), n_secrets) for line in load_file_as_lines(filename)
        ]

    def best_sequence(self) -> PriceSequence:
        sequences: dict[PriceSequence, int] = defaultdict(int)
        for buyer in self.buyers:
            for sequence in set(buyer.diff_sequences):
                if sequence is not None:
                    sequences[sequence] += buyer.price_at_sequence(sequence)
        return max(sequences, key=sequences.get)  # type: ignore[arg-type]

    def most_bananas(self) -> int:
        return self.price_at_sequence(self.best_sequence())

    def price_at_sequence(self, sequence: PriceSequence) -> int:
        return sum(buyer.price_at_sequence(sequence) for buyer in self.buyers)

    def sum_buyer_secrets(self) -> int:
        return sum(buyer.secrets[-1] for buyer in self.buyers)
