num_input = input("Enter a positive number: ")
num_of_digits = len(num_input)
original_number = int(num_input)
total_sum = 0

for digit_char in num_input:
    digit = int(digit_char)
    total_sum = total_sum + (digit ** num_of_digits)

if total_sum == original_number:
    print(original_number, "is an Armstrong number.")
else:
    print(original_number, "is NOT an Armstrong number.")
