# itertools: product, permutation, combination, accumulate, groupby, and infinite iterators.

from itertools import product
a = product([0,1],'ab')
print(list(a))


from itertools import permutations

from itertools import accumulate

a = accumulate([0, 1, 2, 3, 4])
print(list(a))


from itertools import groupby

def smaller_than_3(x):
    return x < 3
a = [1, 2, 3, 4]
group_obj = groupby(a, key=smaller_than_3)
print(group_obj)
for key, value in group_obj:
    print(key, list(value))