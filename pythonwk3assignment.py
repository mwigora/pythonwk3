def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
    else:
        final_price = price
    return final_price

original_price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(original_price, discount_percent)

if discount_percent >= 20:
    print(f"The final price after applying a {discount_percent}% discount is: ${final_price:.2f}")
else:
    print(f"No discount was applied. The final price is: ${final_price:.2f}")