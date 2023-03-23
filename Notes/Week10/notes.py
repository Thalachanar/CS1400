from functools import reduce # Needed in order to use reduce


# values = range(1,10)

# odds1 = [value for  value in values if value % 2 == 1]
# print(odds1)

# odds2 = list(filter(lambda x: x%2 == 1, values))
# print(odds2)

# sum1 = sum(values)
# print(sum1)

# sum2 = reduce(lambda x,y: x*y, values, 2)
# print(sum2)



# fruit = ['banana', 'apple', 'pear', 'peach']

# fruit1 = reduce(lambda x,y: x+', '+y, fruit)
# print(fruit1)

# fruit2 = ', '.join(fruit)
# print(fruit2)


# fruits = ['banana', 'apple', 'pear', 'peach']

# for fruit in fruits:
#     print(fruits.index(fruit), '-->', fruit)

# for i in range(len(fruits)):
#     print(i, '-->', fruits[i])
    
# for what in enumerate(fruits):
#     print(what[0], '-->', what[1])

# for i,fruit in enumerate(fruits, 1): # By including '1' as an optional parameter for the `enumerate` function, it will start the index at 1 when printed
#     print(i, '-->', fruit)

fruits = {'banana', 'apple', 'pear', 'peach', 'apple'}
print(fruits, type(fruits), id(fruits))

fruits.sort()
print(fruits, type(fruits), id(fruits))

# fruits2 = sorted(fruits)
# print(fruits2, type(fruits2), id(fruits2))
