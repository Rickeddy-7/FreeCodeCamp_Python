


# import budget
# from math import floor

# def draw_bar_chart(categories):

#     for cat in categories:
#         if isinstance(cat, budget.Category):
#             max_value = max(0, sum(cat['amount'] for cat in categories if cat['amount'] < 0))
        
#             max_value = abs(max_value)
#             scale = 100 / max_value
        
#             chart = ''

#             # Draw y-axis labels
#             for i in range(100, -10, -10):
#                 chart += f'{i:>3d}|'
#                 for cat in categories:
#                     value = sum(cat['amount'] for cat in categories if cat['amount'] < 0)
#                     value = floor(abs(value) * scale)
#                     if value >= i:
#                         chart += "o"
#                     else:
#                         chart += " "
#                 chart += "\n"
        
#             # Draw horizontal line
#                 chart += " " * 4
#                 for _ in categories:
#                     chart += "-" * 2
#                 chart += "\n"
            
#             # Draw category names
#                 chart += " " * 4
#                 for category in categories:
#                     chart += f"{category.name:^2}"
  
#     return chart


# food = budget.Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# clothing = budget.Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = budget.Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# # print(food,'\n')
# # print(clothing,'\n')
# # print(auto,'\n')

# print(draw_bar_chart([food, clothing, auto]))
