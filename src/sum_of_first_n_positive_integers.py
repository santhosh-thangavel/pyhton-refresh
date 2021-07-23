# Write a program that reads a positive integer, n, from the user and then displays the
# sum of all of the integers from 1 to n. The sum of the first n positive integers can be
# computed using the formula:
# sum = (n)(n + 1)/2

def sum_of_first_n_positive_integers(positive_integer):

    if positive_integer == int(positive_integer):
        sum_of_first_positive_integers = ((positive_integer)*(positive_integer+1))/2
        print(f"sum of first n positive integers = {int(sum_of_first_positive_integers)}")
    else:
        print(f"Input an integer and not a float or string, please")

sum_of_first_n_positive_integers(3)