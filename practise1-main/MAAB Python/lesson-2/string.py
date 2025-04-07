#hello = """world
#hello""" # triple qoute needed to string in more than one line
#print(hello)
#word= "i'm a teacher"
#print(word)
#word1= 'i\'m a teacher'
#print(word1)

#ab= "hello\t salom"
#print(tab)
# \t  3 space
#directory= r" D:\Python\bi-and_ai_talents"
# r  row string

#name = "John" #input(" what is your name? ")
#age= int(input("age: "))
#print(" Your name is " +name +"  and your are "+ str(age) +" years old")
# + stringlar uchun "concatenation"
#print(f" Your name is {name} and your are {age}  years old")
#print(" Your name is {fname} and your are {Age}  years old".format(Age=age, fname=name))

#name1= "Adam"
#name2 ="John"
#print(f"{name1:<8} -first name")
#print(f"{name2:<8} - second name")



# my_str= "Hello world" #sequence
# print(len(my_str))
# Slicing or Indexing
# [Begin:End]
#print(my_str[::2])
#print(my_str[:4]+my_str[5:])
# print(my_str[-5:])



#word= input("Word: ")
#last_character= word[-1]
#print(f"Last character is:" ,last_character)
#print(f"Last character is:" ,last_character, end=" ")

#mutable amd unmutable

# mine= "Apple"
# print("oldin: ", id(mine))
# mine="a" + mine[1:]
# print("keyin: ", id(mine))
# print(mine)


# object.method()

# fruit="Apple"
# print("original: ",fruit)
# print(fruit.lower())
# print(fruit.upper())
# print(fruit.capitalize())
# print(fruit.title())
#
# print(fruit.endswith('b'))
# print(fruit.startswith('A'))

# word = ('-'*50)
# word= '       Hello World'
# print(word)
# print(word.strip())

# fruits= '       adsd  fsd qf wrf'
# print(fruits.split())
#
#
# print("-"*50)
# file_name="first.py"
# base_name=file_name.split('.')[0]
# extension=file_name.split('.')[1]
# print(f"{file_name=}")
# print(f"{base_name=}")
# print(f"{extension=}")




# True va False
#
# a= 4
# b= 3
# # print(a!=b)
#
# print(bool(0))
# print(bool(1))
# print('Stringlar uchun')
# print(bool('afesd'))
#
# print("containerlar uchun")
# print(bool([])) #empty
# print(bool([1,3])) #list\


# word= input()
# print(bool(word))
# if not bool(word.strip()):
#     print('please enter something')
# else:
#     print("you enetered ", word)