from calculator import calculate_total
from invoice import print_invoice

name = input("Enter customer name: ")
amount = float(input("Enter purchase amount: "))

discount, tax, total = calculate_total(amount)

print_invoice(name, amount, discount, tax, total)