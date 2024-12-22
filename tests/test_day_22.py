from advent_of_code_2024.banana_market import BananaMarket, Buyer


def test_part_one_buyer():
    buyer = Buyer(123, 10)
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


def test_part_one_market():
    market = BananaMarket("day-22.test-0.txt")
    assert [buyer.secrets[2000] for buyer in market.buyers] == [
        8685429,
        4700978,
        15273692,
        8667524,
    ]
    assert market.sum_buyer_secrets() == 37327623


def test_part_two_buyer():
    buyer = Buyer(123, 10)
    assert [
        (buyer.secrets[idx], buyer.prices[idx], buyer.price_diffs[idx])
        for idx in range(10)
    ] == [
        (123, 3, None),
        (15887950, 0, -3),
        (16495136, 6, 6),
        (527345, 5, -1),
        (704524, 4, -1),
        (1553684, 4, 0),
        (12683156, 6, 2),
        (11100544, 4, -2),
        (12249484, 4, 0),
        (7753432, 2, -2),
    ]
    assert buyer.price_at_sequence((-1, -1, 0, 2)) == 6


def test_part_two_market():
    market = BananaMarket("day-22.test-1.txt")
    assert market.price_at_sequence((-2, 1, -1, 3)) == 23
    assert market.best_sequence() == (-2, 1, -1, 3)
    assert market.most_bananas() == 23
