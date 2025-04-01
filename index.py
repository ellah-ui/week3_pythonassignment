price = ""
discount_percent = ""
calculated_discount = (price, discount_percent)

price = 1000
discount_percent = 28
calculated_discount = price * discount_percent / 100
# Check if the discount is greater than or equal to 20%
# If it is, print the discounted price
# If not, print the original price

if discount_percent >= 20:
	print(price - (calculated_discount))
else:
    print(price)

    
    