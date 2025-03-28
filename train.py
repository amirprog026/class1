DISCOUNT_PRICE=100000
DISCOUNT_RATE=1
def get_price()->str:
    price= input("Please enter a price")
    return price
def get_vat()->str:
    vat=input("Please enter VAT rate")
    return vat
def str_to_int(value:str):
    return int(value)    
def calculate_vat(price:int,rate:int=10)->int:
    return (rate*price)/100
def is_discount_included(price:int)->bool: # این تابع بررسی میکند آیا قیمت شامل تخفیف میشود یا خیر
    return price>DISCOUNT_PRICE
def calculate_discount(price:int)->int:
    return price*(DISCOUNT_RATE/100)
def calculate_payable_price(vat:int,price:int):
    if is_discount_included(price):
        return vat+(price-(calculate_discount(price)))
    return vat + price

price=str_to_int(get_price())
vat=str_to_int(get_vat())
vat_amount=calculate_vat(price,vat)#مبلغ مالیات
print("Payable price ",calculate_payable_price(vat_amount,price))
