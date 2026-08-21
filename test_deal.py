from deal_checker import is_deal, format_deal

discount = 80

if is_deal(discount):
    message = format_deal(
        product="Test Product",
        price=199,
        old_price=999,
        discount=discount,
        store="Amazon",
        link="https://example.com/test-deal"
    )

    print(message)
else:
    print("Not a qualifying deal")
