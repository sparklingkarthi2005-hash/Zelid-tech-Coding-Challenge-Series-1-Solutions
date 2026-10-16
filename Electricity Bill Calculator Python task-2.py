units = float(input("Enter total units consumed: "))
bill = 0.0
if units <= 100:
 bill = units * 2
elif units <= 300:
 bill = (100 * 2) + ((units - 100) * 3)
elif units <= 600:
 bill = (100 * 2) + (200 * 3) + ((units - 300) * 5)
else:
 bill = (100 * 2) + (200 * 3) + (300 * 5) + ((units - 600) * 7)
print("Total Electricity Bill: ", bill)
