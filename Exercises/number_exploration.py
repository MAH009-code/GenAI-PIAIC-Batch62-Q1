name = input("Enter your name: ")

fav_number1 = int(input("Enter your first favorite number: "))
fav_number2 = int(input("Enter your second favorite number: "))
fav_number3 = int(input("Enter your third favorite number: "))

favorite_numbers = [fav_number1, fav_number2, fav_number3]

even_odd_list = []
for num in favorite_numbers:
    # Check for even odd num
    if num % 2 == 0:
        even_odd_list.append((num, "even"))
    else:
        even_odd_list.append((num, "odd"))

print(f"\nHello, {name}! Let's explore your favorite numbers:")

for num, even_odd in even_odd_list:
    print(f"The number {num} is {even_odd}.")

for num in favorite_numbers:
    print(f"The number {num} and its square: ({num}, {num ** 2})")

sum_of_numbers = sum(favorite_numbers)

print(f"\nAmazing! The sum of your favorite numbers is: {sum_of_numbers}")
# Check for prime num
is_prime = True
if sum_of_numbers <= 1:
    is_prime = False
else:
    for i in range(2, int(sum_of_numbers ** 0.5) + 1):
        if sum_of_numbers % i == 0:
            is_prime = False
            break
# Check for prime num msg
if is_prime:
    print(f"Wow, {sum_of_numbers} is a prime number!")
else:
    print(f"{sum_of_numbers} is not a prime number.")
