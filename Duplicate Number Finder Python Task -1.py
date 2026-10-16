n = int(input("Enter total number of elements: "))
a = []
print("Enter the numbers one by one:")

for i in range(n):
    num = int(input())
    a.append(num)

duplicate = None

for i in range(len(a)):
    for j in range(i + 1, len(a)):
        if a[i] == a[j]:
            duplicate = a[i]
            break
    if duplicate is not None:
        break

if duplicate is not None:
    print("Duplicate number is:", duplicate)
else:
    print("No duplicate number found.")
