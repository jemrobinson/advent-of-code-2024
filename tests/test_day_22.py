from advent_of_code_2024.banana_market import BananaMarket, Buyer


def test_part_one():
    buyer = Buyer(123)
    buyer.generate_secrets(10)
    assert [buyer.secrets[idx] for idx in range(11)] == [
        123,
        15887950,
        16495136,
        527345,
        704524,
        1553684,
        12683156,
        11100544,
        12249484,
        7753432,
        5908254,
    ]
    market = BananaMarket("day-22.test.txt")
    market.generate_secrets(2000)
    assert [buyer.secrets[2000] for buyer in market.buyers] == [
        8685429,
        4700978,
        15273692,
        8667524,
    ]
    assert market.sum_buyer_secrets() == 37327623
