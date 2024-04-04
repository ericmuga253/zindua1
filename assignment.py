products = [
    {"name": "product1", "price": 10},
    {"name": "product2", "price": 20},
    {"name": "product3", "price": 15}
]

def find_highest_priced_product(products):
    highest_price = 0
    highest_priced_product = None
    for product in products:
        if product['price'] > highest_price:
            highest_price = product['price']
            highest_priced_product = product

    print(highest_priced_product)

find_highest_priced_product(products)