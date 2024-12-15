from advent_of_code_2024.warehouse import Warehouse


def test_part_one():
    warehouse_0 = Warehouse("day-15-moves.test-0.txt", "day-15-warehouse.test-0.txt")
    assert warehouse_0.score_gps() == 2028
    warehouse_1 = Warehouse("day-15-moves.test-1.txt", "day-15-warehouse.test-1.txt")
    assert warehouse_1.score_gps() == 10092
