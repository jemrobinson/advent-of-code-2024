from advent_of_code_2024.plant_regions import GardenPlot


def test_part_one():
    plot_0 = GardenPlot("day-12.test-0.txt")
    assert plot_0.price() == 140
    plot_1 = GardenPlot("day-12.test-1.txt")
    assert plot_1.price() == 772
    plot_2 = GardenPlot("day-12.test-2.txt")
    assert plot_2.price() == 1930
