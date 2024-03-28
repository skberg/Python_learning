#functions
print('a value')
#input('ask for a value') # returns a value
#print(input('ask for a value: '))

#methods -> functions of datatypes
print('value'.upper())
print('value'.lower())
print('value'.replace('e', '3'))

#new functions 

print(abs(-1))
print(max(10,5))
print(min(10,5))
print(len('test'))

#Pythagorean theorem

side_a = int(input("the width of a triangle: "))
side_b = int(input("the hight of the triangle: "))
hypotenuse = (side_a ** 2 + pow(side_b,2)) ** (1/2)
print('the hypotenus is:', round(hypotenuse,2))