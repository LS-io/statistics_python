## Here, we will use the dictionary data to build a skeletal version of a shopping application.
## This will allow us to review and understand the data structure and the operations that can be applied to it.
prices = {'Macbook 13': 1300, 'Macbook 15': 2100,'ASUS ROG': 1600}
cart = {}

while True:
    _continue = input('Would you like to continue shopping? [y/n]: ')

    if _continue == 'y':
        print(f'Available products and prices: {prices}')
        new_item = input('Which product would you like to add to your cart? ')

        if new_item in prices:
            if new_item in cart:
                cart[new_item] += 1
            else:
                cart[new_item] = 1
        else:
            print('Please only choose from the available products.')
    
    elif _continue == 'n':
        break
    else:
        print('Please only enter "y" or "n".')

# Calculations of the total bill.