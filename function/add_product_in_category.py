from function.add_product import add_product
from Category.TV import TV
from Category.Smartphone import smartphone
from Category.Mp3 import mp3
from Category.DVD import DVD

def add_product_in_category(products):
    admin_category=input(f"Which category would you like to choose?: {products.keys()} , enter category name: ")
    admin_label = input("Enter product: ")
    admin_price = int(input("Enter price: "))
    for category, arr in products.items():
        if admin_category == category:
            if arr == TV[0:10]:
                admin_product=add_product(admin_label, admin_price)
                arr.append(admin_product)
            elif arr == smartphone[0:10]:
                admin_product=add_product(admin_label, admin_price)
                arr.append(admin_product)
            elif arr == mp3[0:10]:
                admin_product=add_product(admin_label, admin_price)
                arr.append(admin_product) 
            elif arr == DVD[0:10]:
                admin_product=add_product(admin_label, admin_price)
                arr.append(admin_product)  
            print(arr)            
    
