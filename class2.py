#num = int(input("數字是多少?"))
#print("數字是%d"%num)

# 
# age = 30
# if age >= 20:
#     print("我成年了")
# print("悲哀")    
# 

#age = int(input("請輸入你的身高:"))
#if age >= 18:
#    print("悲哀")
#else:
#    print("好")


# age = int(input("請輸入你的身高:"))
# if age >= 18:
#     print("悲")
# elif age < 18 and age >= 12:
#     print("還行")
# else:
#     print("爽")

# i = 0
# while i < 10:
#     print("你好")
#     i += 1

# num = 0
# i = 1
# while i <= 100:
#     num += i
#     i += 1
# print(num)

# import random
# ans = random.randint(1,100)
# count = 0
# guess_num = 0
# while guess_num != ans:
#     guess_num = int(input("請輸入你的數字:"))
#     count += 1
#     if guess_num > ans:
#         print("你猜大")
#     else:
#         print("你猜小")
# print("你猜對了,猜了%d次"%count)

# print("hello",end='')
# print("world",end='')

# print("hello\tworld")
# print("yujin\tpretty")

# i = 1
# while i <= 9:
#     j = 1
#     while j <= i:
#         print(f"{j} * {i} = {j*i}\t",end="")
#         j += 1
#     i += 1
#     print()

# name = "jacklin"
# for x in name:
#     print(x)

# name = "a apple a day the doctor away"  
# count = 0
# for i in name:
#     if i == 'a':
#         count += 1
# print(count)

# range(num) 取 0~num-1
# range(num1,num2,step) 取num1~num2-1，按照step的間隔取
# for i in range(10):
#     print(i)
# for i in range(1,10):
#     print(i)
# for x in range(1,10,2):
#     print(x)

# count = 0
# for i in range(1,100):
#     if i % 2 == 0:
#         count += 1
# print(count)        

# for i in range(1,10):
#     for j in range(1,10):
#         if(i > j):
#             print(f"{i} * {j} = {i*j}\t",end="")
#         elif (i == j):
#             print(f"{i} * {j} = {i*j}\t")

#更好的寫法
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{i} * {j} = {i*j}\t",end="")
#     print()

#continue用於跳過此次循環，直接進入下一次循環
# import random
# money = 10000
# for j in range(1,21):
#     num = random.randint(1,10)
#     if money >= 1000:
#         money -= 1000
#         print(f"向員工{j}發1000元,剩{money}元")
#     else:
#         print("錢沒了,不發了")
#         break
#     if num < 5:
#         print(f"員工{j},績效分{num},不發錢,下一位")
#         continue

# for i in range(1,21):
#     ans = random.randint(1,10)
#     if money == 0:
#         print("錢沒了,不發了")
#         break
#     elif ans < 5:
#         print(f"員工{i},績效分{ans},不發錢,下一位")
#     else:   
#         money -= 1000
#         print(f"向員工{i}發1000元,剩{money}元")

    
    