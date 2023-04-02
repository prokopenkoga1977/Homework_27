from Category.TV import TV
from Category.Smartphone import smartphone
from Category.Mp3 import mp3
from Category.DVD import DVD
  
def change_product(products):
    admin_category=input(f"Which category would you like to choose?: {products.keys()} , enter category name: ")
    admin_choose=int(input("Enter the number of product that that you wanna change?: "))   
    admin_label = input("Enter product: ")
    admin_price = int(input("Enter price: "))
    for category, arr in products.items():
        if admin_category == category:
            if arr == TV[0:10]:
                print(TV[admin_choose])
                for i, item in enumerate(TV[0:10]):
                    if i==admin_choose:
                        TV[i]={'label': admin_label, 'price': admin_price}
                print(TV[0:10])
            elif arr == smartphone[0:10]:
                print(smartphone[admin_choose])
                for i, item in enumerate(smartphone[0:10]):
                    if i==admin_choose:
                        smartphone[i]={'label': admin_label, 'price': admin_price}
                print(smartphone[0:10])
            elif arr == mp3[0:10]:
                print(mp3[admin_choose])
                for i, item in enumerate(mp3[0:10]):
                    if i==admin_choose:
                        mp3[i]={'label': admin_label, 'price': admin_price}
                print(mp3[0:10])
            elif arr == DVD[0:10]:
                print(DVD[admin_choose])
                for i, item in enumerate(DVD[0:10]):
                    if i==admin_choose:
                        DVD[i]={'label': admin_label, 'price': admin_price}
                print(DVD[0:10])
