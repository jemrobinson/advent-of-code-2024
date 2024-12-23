from advent_of_code_2024.lan_party import LanParty


def test_part_one():
    party = LanParty("day-23.test.txt")
    assert party.count_triples_with_ts() == 7


def test_part_two():
    party = LanParty("day-23.test.txt")
    assert party.find_password() == "co,de,ka,ta"
