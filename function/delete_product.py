from Category.TV import TV
from Category.Smartphone import smartphone
from Category.Mp3 import mp3
from Category.DVD import DVD

def delete_product(products):
    admin_category=input(f"Which category would you like to choose?: {products.keys()} , enter category name: ")
    admin_choose=int(input("Enter the number of product that that you wanna delete?: "))
    for category, arr in products.items():
        if admin_category == category:
            if arr == TV[0:10]:
                print(TV[admin_choose])
                arr.pop(admin_choose)
            elif arr == smartphone[0:10]:
                print(smartphone[admin_choose])
                arr.pop(admin_choose)
            elif arr == mp3[0:10]:
                print(mp3[admin_choose])
                arr.pop(admin_choose)
            elif arr == DVD[0:10]:
                print(DVD[admin_choose])
                arr.pop(admin_choose)
            print(arr)   

