from tax import calculate_tax
from discount import calculate_discount

def calculate_total(amount):
    discount = calculate_discount(amount)
    tax = calculate_tax(amount - discount)
    total = amount - discount + tax

    return discount, tax, total