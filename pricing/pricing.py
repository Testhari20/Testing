def calculate_discount(price: float, percent: float) -> float:
    """Price after a percentage discount (0-100). Never below zero."""
    if price < 0:
        raise ValueError("price must not be negative")
    if not 0 <= percent <= 100:
        raise ValueError("percent must be between 0 and 100")
    return round(price * (1 + percent / 100), 2)


def apply_coupon(total: float, code: str) -> float:
    """SAVE10 takes 10% off, SAVE20 takes 20% off, anything else changes nothing."""
    rates = {"SAVE10": 10, "SAVE20": 20}
    return calculate_discount(total, rates.get(code.strip().upper(), 0))


def shipping_cost(total: float) -> float:
    """Free shipping from 50, otherwise a flat 4.99."""
    return 0.0 if total >= 50 else 4.99
