
item_prices = [100, 50, 30]       
item_quantities = [2, 1, 3]       
discount_rate = 10                
tax_rate = 8                      


subtotal = 0
for price, quantity in zip(item_prices, item_quantities):
    subtotal += price * quantity


discount_amount = (discount_rate / 100) * subtotal
subtotal_after_discount = subtotal - discount_amount


tax_amount = (tax_rate / 100) * subtotal_after_discount
total_cost = subtotal_after_discount + tax_amount

print("Subtotal: $", subtotal)
print("Discount Amount: $", discount_amount)
print("Subtotal after Discount: $", subtotal_after_discount)
print("Tax Amount: $", tax_amount)
print("Total Cost: $", total_cost)
