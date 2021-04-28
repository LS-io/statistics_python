## The term recursion denotes the style of solving a problem using functions by having a function recursivelly call itself.
## The idea is, that if we can break down a problem into a smaller piece, and solve it, we can eventually solve the original problem.
##example:
def find_sum(my_list):
    if len(my_list) == 1:
        return my_list[0]
    return find_sum(my_list[: -1]) + my_list[-1]

print(find_sum([1, 2, 3]))