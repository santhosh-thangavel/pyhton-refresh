# Pretend that you have just opened a new savings account that earns 4 percent interest
# per year. The interest that you earn is paid at the end of the year, and is added
# to the balance of the savings account. Write a program that begins by reading the
# amount of money deposited into the account from the user. Then your program should
# compute and display the amount in the savings account after 1, 2, and 3 years. Display
# each amount so that it is rounded to 2 decimal places.
# Formula to calculate principal
# p = a/((1+ (r/n))^(n*t))


def calculate_years(years):
    reverse_years = []
    next = years-1

    if next >0:
        reverse_years.append(next)
        calculate_years(next)
        return reverse_years[-1]

# def append_an_year():



# def compound_interest(user_amount, years):
#
#     next = years + 1
#     if next < 5:
#         r = 4/100
#         n = 12
#         t = 1
#         amount = user_amount
#         principal = amount/((1+ (r/n))**(n*t))  # formula doesn't give the right result. To be fixed.
#         # print(principal)
#         amount += amount+principal
#         # print(f"amount for  year {years} = {round(amount, 2)}")
#         compound_interest(amount, next)


# compound_interest()
calculate_years(4)


# I don't like how the function is written as it has a key word argument. Key word argument can be over rided
# and the function will still give results which the function shouldn't be doing. To be fixed.