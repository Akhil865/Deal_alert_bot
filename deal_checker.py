from config import MIN_DISCOUNT


def is_deal(discount):
    return discount >= MIN_DISCOUNT


def format_deal(product, price, old_price, discount, store, link):
    return (
        f"🔥 {discount}% OFF\n\n"
        f"🛒 {product}\n"
        f"💰 ₹{price} (was ₹{old_price})\n"
        f"🏪 {store}\n"
        f"🔗 {link}"
    )
