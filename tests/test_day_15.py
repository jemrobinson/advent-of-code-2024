from advent_of_code_2024.warehouse import LargeWarehouse, Warehouse


def test_part_one():
    warehouse_0 = Warehouse("day-15-moves.test-0.txt", "day-15-warehouse.test-0.txt")
    assert warehouse_0.score_gps() == 2028
    warehouse_1 = Warehouse("day-15-moves.test-1.txt", "day-15-warehouse.test-1.txt")
    assert warehouse_1.score_gps() == 10092


def test_part_two():
    warehouse_0 = LargeWarehouse(
        "day-15-moves.test-0.txt", "day-15-warehouse.test-0.txt"
    )
    assert warehouse_0.score_gps() == 1751
    warehouse_1 = LargeWarehouse(
        "day-15-moves.test-1.txt", "day-15-warehouse.test-1.txt"
    )
    assert warehouse_1.score_gps() == 9021
