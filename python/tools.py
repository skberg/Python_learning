# f strings
user_name = 'Anna'
User_age = 10
user_info = f'{user_name} is {User_age} years old'
bad_approaoch = user_name + ' is ' + str(User_age) + 'years old' # this is the bad approch
print(user_info)

#singel line if stamtes 

user_age = 15
user_status = 'Adult' if user_age >= 18 else 'Child'

print(f'{user_name} is {User_age} years old. The perosn is a {user_status}')

#list comperehsension 

simple_lsit = [f'{j}{i}' for i in range(0,11,1) for j in ('a', 'b', 'c') if j == 'a']
#for i in range(0,11,1):
 #   simple_lsit.append(i)
print(simple_lsit)

# lambda functions 

double_value = lambda num: num * 2
print(double_value(10))




#exercise 

battelship_board = [f'{letter}{num}' for letter in ('A' ,'B', 'C', 'D' ,'E') for num in range(1,6) if f'{letter}{num}' != 'C3']
print(battelship_board)