import pytest

from pricing.pricing import apply_coupon, calculate_discount, shipping_cost



def test_discount_takes_the_percentage_off():
    assert calculate_discount(100, 25) == 75.0


def test_no_discount_keeps_the_price():
    assert calculate_discount(80, 0) == 80.0


def test_a_negative_price_is_rejected():
    with pytest.raises(ValueError):
        calculate_discount(-1, 10)


def test_a_percent_over_100_is_rejected():
    with pytest.raises(ValueError):
        calculate_discount(50, 150)


def test_coupon_is_case_insensitive():
    assert apply_coupon(200, "save10") == 180.0


def test_unknown_coupon_changes_nothing():
    assert apply_coupon(200, "NOPE") == 200.0


def test_shipping_is_free_from_fifty():
    assert shipping_cost(50) == 0.0
    assert shipping_cost(49.99) == 4.99
