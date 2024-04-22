# დავალება 1
#1) for i in range (11):
    # print (i)
    
#2) for i in range (10, -1, -1):
#     print (i)

# 3)for i in range (2, 0, ):
#     print (i)

# 4)for i in range (99, 1, -1):
#      print (i)

#5
# sum_of_numbers = 0

# for i in range(1, 11):
#     sum_of_numbers += i

# print("ნატურალური რიცხვების ჯამი:", sum_of_numbers)

#6
# # a = int(input("Please enter starting point number: "))
# b = int(input("Please enter ending point number: "))
# for i in range(a , b,):
#     print(i)


#while ციკლი

#1)
# count = 1

#while count<= 10:
#    print(count)
 #   count +=1
 
#2)
# count = 10
# while count>= 1:
#  print(count)
#  count -=1
 
#3)

# number = 0
# while number <= 100:
#     if number % 2 == 0:
#         print(number, end=" ")
#     number += 1
    
#4)
# number = 99

# while number >= 1:
#     if number % 2 != 0:
#         print(number, end=" ")
#     number -= 1

#5)
# sum_of_numbers = 0
# count = 1
# while count <= 10:
#     sum_of_numbers += count
#     count += 1
# print("პირველი 10 ნატურალური რიცხვის ჯამი:", sum_of_numbers)

#6)
a = int(input("შეიტანეთ a: "))
b = int(input("შეიტანეთ b: "))

while a <= b:
    print(a)
    a += 1