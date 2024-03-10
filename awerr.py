# for i in range(1, 5, 1):
#     print(i, end=",")
# for i in range(10, 0, -1):
#     print(i, end=",")
# for i in range(2, 23, 4):
#     print(i, end=",")
# for i in range(1, 50, 9):
#     print(i, end=",")
# for i in range(2, 22, 44):
#     print(i, end=",")
# for i in range(50, 31, -5):
#     print(i, end=",")
# deck = int(input("ckoлько раз вам написать привет ?   "))
# for deck in range(deck):
#     print("привет")
deck = int(input("введите число "))
r = int(input("введите число "))
u = int(input("введите число "))
if deck > r and u >= 0 or deck <= r and u <= 0:
    print("так не может быть")   
for i in range(deck,r,u):
    print(i , end = ",")