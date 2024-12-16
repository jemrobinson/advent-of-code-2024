from advent_of_code_2024.data_loaders import load_file_as_array, load_file_as_lines
from advent_of_code_2024.utility import count


class WordSearchSimple:
    def __init__(self, filename: str):
        lines = load_file_as_lines(filename)
        size = len(lines)
        self.rows = [line.strip() for line in lines]
        self.columns = ["".join([line[idx] for line in lines]) for idx in range(size)]
        self.diags_nwse = []
        self.diags_swne = []
        for idx_col in range(size):
            idx_row = 0
            chars_nwse = chars_swne = ""
            while idx_row + idx_col < size:
                chars_nwse += self.rows[idx_row][idx_row + idx_col]
                chars_swne += self.rows[size - idx_row - 1][idx_row + idx_col]
                idx_row += 1
            self.diags_nwse.append(chars_nwse)
            self.diags_swne.append(chars_swne)
        for idx_row in range(1, size):
            idx_col = 0
            chars_nwse = chars_swne = ""
            while idx_row + idx_col < size:
                chars_nwse += self.columns[idx_col][idx_row + idx_col]
                chars_swne += self.columns[idx_col][size - idx_row - idx_col - 1]
                idx_col += 1
            self.diags_nwse.append(chars_nwse)
            self.diags_swne.append(chars_swne)

    def search(self, pattern: str) -> int:
        pattern_r = pattern[::-1]
        rows = sum(count(pattern, row) for row in self.rows)
        rows_r = sum(count(pattern_r, row) for row in self.rows)
        columns = sum(count(pattern, column) for column in self.columns)
        columns_r = sum(count(pattern_r, column) for column in self.columns)
        diags_nwse = sum(count(pattern, diag_nwse) for diag_nwse in self.diags_nwse)
        diags_nwse_r = sum(count(pattern_r, diag_nwse) for diag_nwse in self.diags_nwse)
        diags_swne = sum(count(pattern, diag_swne) for diag_swne in self.diags_swne)
        diags_swne_r = sum(count(pattern_r, diag_swne) for diag_swne in self.diags_swne)
        return (
            (rows + rows_r)
            + (columns + columns_r)
            + (diags_nwse + diags_nwse_r)
            + (diags_swne + diags_swne_r)
        )


class WordSearch:
    def __init__(self, filename: str) -> None:
        self.array = load_file_as_array(filename)

    def search_xmas(self) -> int:
        total = 0
        for idx_x in range(1, self.array.shape[0] - 1):
            for idx_y in range(1, self.array.shape[1] - 1):
                if self.array[idx_y, idx_x] == "A":
                    nw = self.array[idx_y - 1, idx_x - 1]
                    ne = self.array[idx_y - 1, idx_x + 1]
                    se = self.array[idx_y + 1, idx_x + 1]
                    sw = self.array[idx_y + 1, idx_x - 1]
                    nwse = (nw == "S" and se == "M") or (nw == "M" and se == "S")
                    swne = (sw == "S" and ne == "M") or (sw == "M" and ne == "S")
                    if nwse and swne:
                        total += 1
        return total
