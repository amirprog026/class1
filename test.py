DISCOUNT_PRICE=100000
DISCOUNT_RATE=1
price=int(input("please enter product price"))
vat=int(input("Please enter VAT rate"))
tax=(price*vat)/100
payable_price=tax+price
print("Pure price",price)
print("TAX Rate",vat)
print("payable before discount",payable_price)
discount=(price*DISCOUNT_RATE)/100
finalprice=payable_price - discount if payable_price>DISCOUNT_PRICE else  payable_price

print("final price",finalprice)