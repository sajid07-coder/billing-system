
print("================================")
print("       SHOP BILLING SYSTEM")
print("================================")

customer = input("Enter customer name: ")

total = 0
n = int(input("Enter number of products: "))

for i in range(n):

    print("\nProduct", i + 1)

    product = input("Enter product name: ")
    price = float(input("Enter price per unit: "))

    quantity = float(input("Enter quantity: "))
    unit = input("Enter unit (kg/g/litre/ml/pcs): ").lower()

    amount = price * quantity
    total += amount

    print("Product:", product)
    print("Quantity:", quantity, unit)
    print("Amount: Rs.", amount)

# Discount
discount = total * 0.10

# GST
gst = (total - discount) * 0.05

# Final amount
final_amount = total - discount + gst

print("\n================================")
print("          FINAL BILL")
print("================================")

print("Customer Name:", customer)
print("--------------------------------")
print("Total Amount: Rs.", round(total, 2))
print("Discount (10%): Rs.", round(discount, 2))
print("GST (5%): Rs.", round(gst, 2))
print("--------------------------------")
print("Final Amount: Rs.", round(final_amount, 2))

print("================================")
print("         THANK YOU!")
print("================================")
