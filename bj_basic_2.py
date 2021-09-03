#1
from sys import stdin

A, B = map(int, stdin.readline().split())

if A < B:
    print("<")
elif A > B:
    print(">")
else:
    print("==")


#2
from sys import stdin

A = int(stdin.readline())

if A in range(90, 101):
    print("A")
elif A in range(80, 90):
    print("B")
elif A in range(70, 80):
    print("C")
elif A in range(60, 70):
    print("D")
else:
    print("F")


#3
A = int(input())

if ((A % 4 == 0) and (A % 100 != 0)) or (A % 400 == 0):
    print("1")
else:
    print("0")


#4
# 런타임 에러
# a, b = map(int, input().split())
#
# if a > 0 and b > 0:
#     print(1)
# elif a < 0 and b > 0:
#     print(2)
# elif a < 0 and b < 0:
#     print(3)
# elif a > 0 and b < 0:
#     print(4)
# else:
#     print(0)

#4-1
x, y = map(int, input().split())

if x > 0:
    if y > 0:
        print(1)
    else:
        print(4)
else:
    if y > 0:
        print(2)
    else:
        print(3)


#5

h, m = map(int, input().split())

if m > 44:
    print(h, m - 45)
elif h >= 1 and m <= 44:
    print(h - 1, m + 15)
else:
    print(23, m + 15)