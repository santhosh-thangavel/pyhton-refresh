# The program that you create for this exercise will begin by reading the cost of a meal
# ordered at a restaurant from the user. Then your program will compute the tax and
# tip for the meal. Use your local tax rate when computing the amount of tax owing.
# Compute the tip as 18 percent of the meal amount (without the tax). The output from
# your program should include the tax amount, the tip amount, and the grand total for
# the meal including both the tax and the tip. Format the output so that all of the values
# are displayed using two decimal places.
import struct


# Match multiple input item name with dict keys

def food_item_and_count(**kwargs):
    meal_and_cost = {'spegatti': 3.1, 'tortillo': 3.2, 'muffin': 2.8, 'nan': 2, 'roti': 3, 'tandoori': 4.3,
                     'icecream': 1.8}
    menu_price_list = []
    for key, value in kwargs.items():
        if key in meal_and_cost.keys():
            print(f"{key} = {value}")
            menu_price = round(meal_and_cost.get(key)*value, 2)
            # print(f"Total price of {key} = {menu_price}")
            menu_price_list.append(menu_price)

    total_price_of_items_without_tax_and_tip = round(sum(menu_price_list), 2)
    tax_amount = 0.2*total_price_of_items_without_tax_and_tip
    tip_amount = 0.18*total_price_of_items_without_tax_and_tip
    grand_total = total_price_of_items_without_tax_and_tip + tax_amount + tip_amount
    print(f"Total price of items without tax and tip = {total_price_of_items_without_tax_and_tip}")
    print(f"Tax amount = {tax_amount}")
    print(f"Tip amount = {tip_amount}")
    print(f"Grand Total including price, tax and tip to be paid by customer = £{grand_total}")

# How to program without appending menu_price to empty list?


food_item_and_count(spegatti=2, nan=3, soup=4, tortillo=3)
