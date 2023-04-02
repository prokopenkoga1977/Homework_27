# import buy
# from buy import buy as buy_something
#
# from buy import buy
# from User import User

# print(User.User)
#
# bob = User.User("customer" , 300 , [])
#
# print(bob)

# john = {
#     "role" : "customer",
#     "money" : 300 ,
#     "bag" : []
# }
#
# mike = {
#     "role": "manager",
#     "money": 0,
#     "bag": [
#         {
#             "product" : "Hoover",
#             "price" : 100
#         } ,
#         {
#             "product" : "Phone",
#             "price" : 120
#         } ,
#         {
#             "product" : "Computer",
#             "price" : 150
#         } ,
#         {
#             "product" : "Fork",
#             "price" : 180
#         }
#     ]
# }
#
# buy(john,mike)



# 1) Store
# 2) Into store you might : a) Category ( [] )
#    b) Show All products
#    c) Admin mode
#    q) Quit
# if a) -> a) TV , b) Smartphone , c) Mp3 , d) DvD
#       a -> show all TV []
#       b -> show all Sm []
#       c -> show all Mp3 []
# products are dictionaries :
# { "label" : "..." , "price" : "..." , desc : ""... }
# 3) User might buy product if user has money (
#                   {
#                   "name" : "..." ,
#                   "money" : ... ,
#                   "bag" : []
#                   }
# )
# 4) Admin mode yields ->
#   1) add product to category ,
#   2) Delete product
#   3) Change name of product


from Category.TV import TV
from Category.Smartphone import smartphone
from Category.Mp3 import mp3
from Category.DVD import DVD
from function.show_products import show_products
from function.print_products import print_products
from function.delete_product import delete_product
from function.change_product import change_product
from function.add_product import add_product
from function.add_product_in_category import add_product_in_category  

prod_TV = TV[0:10]
prod_Smartphone = smartphone[0:10]
prod_mp3 = mp3[0:10]
prod_DVD = DVD[0:10]


products = {
    "TV" : prod_TV,
    "Smartphone" :prod_Smartphone,
    "MP3": prod_mp3,
    "DvD": prod_DVD
}

is_Running = True

while is_Running :
    user_pick = int(input(
        f"""
        1) Show products 
        2) Show Category
        3) Add product to category
        4) Delete product
        5) Change name of product
        6) Quit
        Answer : """)
    )
        
    if user_pick == 1:
        show_products(products)
            
    elif user_pick == 2 :
        print_products(products)

    elif user_pick == 3:
        add_product_in_category(products)    
    elif user_pick == 4:
        delete_product(products)
    elif user_pick == 5:
        change_product(products)
    elif user_pick == 6 :
        is_Running = False
