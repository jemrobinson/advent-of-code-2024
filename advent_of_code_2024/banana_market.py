from advent_of_code_2024.data_loaders import load_file_as_lines


class Buyer:
    def __init__(self, initial_secret: int) -> None:
        self.secrets = [initial_secret]

    def generate_secrets(self, n_to_generate: int) -> None:
        while len(self.secrets) < n_to_generate + 1:
            next_secret = self.secrets[-1]
            next_secret ^= next_secret << 6  # multiply by 64 and XOR
            next_secret %= 16777216  # take modulus
            next_secret ^= next_secret >> 5  # divide by 32 and XOR
            next_secret %= 16777216  # take modulus
            next_secret ^= next_secret << 11  # multiply by 2048 and XOR
            next_secret %= 16777216  # take modulus
            self.secrets.append(next_secret)


class BananaMarket:
    def __init__(
        self,
        filename: str,
    ) -> None:
        self.buyers = [
            Buyer(int(line.strip())) for line in load_file_as_lines(filename)
        ]

    def generate_secrets(self, n_to_generate: int) -> None:
        for buyer in self.buyers:
            buyer.generate_secrets(n_to_generate)

    def sum_buyer_secrets(self) -> int:
        return sum(buyer.secrets[-1] for buyer in self.buyers)
