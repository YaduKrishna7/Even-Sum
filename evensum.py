n = int(input("Enter a number: "))

total = 0
count = 0

for number in range(1, n + 1):
    if number % 2 == 0:
        total = total + number
        count = count + 1

print("Sum of even numbers:", total)
print("Number of even numbers:", count)