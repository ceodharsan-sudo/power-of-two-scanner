num = int(input("Enter a number: "))
if num > 0 and (num & (num - 1)) == 0:
    print("It is a power of 2")
else:
    print("It is not a power of 2")
result = num & (num - 1)
print("After removing rightmost set bit:", result)
print("2 power 3 =", 2 ** 3)
print("2 power 4 =", 2 ** 4)
print("2 power 5 =", 2 ** 5)
