from advent_of_code_2024.plant_regions import GardenPlot


def test_part_one():
    plot_0 = GardenPlot("day-12.test-0.txt")
    assert plot_0.price() == 140
    plot_1 = GardenPlot("day-12.test-1.txt")
    assert plot_1.price() == 772
    plot_2 = GardenPlot("day-12.test-2.txt")
    assert plot_2.price() == 1930


def test_part_two():
    plot_0 = GardenPlot("day-12.test-0.txt")
    assert plot_0.price_discounted() == 80
    plot_1 = GardenPlot("day-12.test-1.txt")
    assert plot_1.price_discounted() == 436
    plot_2 = GardenPlot("day-12.test-2.txt")
    assert plot_2.price_discounted() == 1206
    plot_3 = GardenPlot("day-12.test-3.txt")
    assert plot_3.price_discounted() == 236
    plot_4 = GardenPlot("day-12.test-4.txt")
    assert plot_4.price_discounted() == 368
