# An online retailer sells two products: widgets and gizmos. Each widget weighs 75
# grams. Each gizmo weighs 112 grams. Write a program that reads the number of
# widgets and the number of gizmos in an order from the user. Then your program
# should compute and display the total weight of the order.

# def widgets_and_gizmos(**user_order):
#     weight_of_widgets_and_gizmos = {'widget': 75, 'gizmo': 112}
#     list_of_item_price = []
#     for key, value in user_order.items():
#         if key in weight_of_widgets_and_gizmos.keys():
#             print(f"Number of {key}s = {value}")
#             weight_of_items = weight_of_widgets_and_gizmos.get(key)*value#getting respective values of keys and multiply
#             # print(weight_of_items)
#             list_of_item_price.append(weight_of_items)
#     # print(list_of_item_price)
#     widget, gizmos = list_of_item_price #unpacking list_of_item_price
#     print(f"Widget weight = {widget} grams")
#     print(f"Gizmos weight = {gizmos} grams")
#     # compute and display the total weight of the order
#     total_weight = sum(list_of_item_price)
#     print(f"Total weight of the order = {total_weight} grams")
#
#
#
# widgets_and_gizmos(widget=7, gizmo=1)

# class HeightConverter:
#
#     def __init__(self, feet, inches):
#         self.feet = feet
#         self.inches = inches
#
#     @staticmethod
#     def _get_number_and_unit(unit_text):
#         import re
#         number_and_unit = re.split(r'((-)?\d+(\.\d+)?)', unit_text)
#         return float(number_and_unit[1]), number_and_unit[2]
#
#     def _get_feet_inch_values(self):
#         feet, feet_unit = self._get_number_and_unit(self.feet)
#         inches, inches_unit = self._get_number_and_unit(self.inches)
#         return feet, inches
#
#     def conversion(self):
#         feet, inches = self._get_feet_inch_values()
#         if feet > 0 or inches > 0:
#             height_in_cms = round(feet * 30.48 + inches * 2.54, 2)
#             return height_in_cms
# HeightConverter.conversion(5feet)