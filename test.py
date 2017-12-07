import polylabel
import json

water1 = json.load(open('fixtures/water1.json'))
water2 = json.load(open('fixtures/water2.json'))


def test_poi_for_water1_and_precision_1():
    p = polylabel.polylabel(water1, 1.0)
    assert p == [3865.85009765625, 2124.87841796875]


def test_poi_for_water1_and_precision_50():
    p = polylabel.polylabel(water1, 50.0)
    assert p == [3854.296875, 2123.828125]


def test_poi_for_water2_and_precision_1():
    p = polylabel.polylabel(water2, 1.0)
    assert p == [3263.5, 3263.5]


def test_degenerate_polygons():
    p = polylabel.polylabel([[[0, 0], [1, 0], [2, 0], [0, 0]]])
    assert p == [0, 0]

    p = polylabel.polylabel([[[0, 0], [1, 0], [1, 1], [1, 0], [0, 0]]])
    assert p == [0, 0]
