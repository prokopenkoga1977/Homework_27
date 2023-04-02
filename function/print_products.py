def print_products(products) :
    user_category = input(f"Which category would you like to choose?: {products.keys()} , enter category name: ")

    for category, arr in products.items():

        if user_category == category:
            print(arr)

