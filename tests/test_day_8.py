from functools import reduce

from advent_of_code_2024.antennae import load_antenna_sets


def test_part_one():
    antennae = load_antenna_sets("day-8.test.txt")
    antinodes = reduce(set.union, [a.antinodes() for a in antennae])
    assert (len(antinodes)) == 14


def test_part_two():
    antennae = load_antenna_sets("day-8.test.txt")
    antinodes = reduce(
        set.union, [a.antinodes(first_harmonic=0, last_harmonic=999) for a in antennae]
    )
    assert (len(antinodes)) == 34
