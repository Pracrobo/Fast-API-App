# print("Hello World")
# Going to print hello World! ~~
from conda.utils import human_bytes


def print_color_red():
    color = "Red"
    print(color)

color = "Blue"
print_color_red() # Red
print(color) # Blue

def multiply_numbers(a, b):
    return a * b

solution = multiply_numbers(10,2)
print(solution)


def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


number_list = [1,2,3,4]
print_list(number_list)



def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item  * current_tax_rate

final_cost = buy_item(50)
print(final_cost)
# def print(self, *args, sep=' ', end='\n', file=None):  # known special case of print
#     """
#     Prints the values to a stream, or to sys.stdout by default.
#
#       sep
#         string inserted between values, default a space.
#       end
#         string appended after the last value, default a newline.
#       file
#         a file-like object (stream); defaults to the current sys.stdout.
#       flush
#         whether to forcibly flush the stream.
#     """
#     pass