############### Section 6: Loops ################

# While Loop example
secret_word = "parabola"
pw = ""
while pw != secret_word:
    pw = input("What's the secret word?\t")
print("You may enter!")

# For Loop example
animals = ["bear", "cat", "dog", "snake", "lion"]

for value in animals:
    print(value)

for num in range(5):
    print(num)

for num in range(5, 10):
    print(num)

# Some additional controls using:
# continue, break and else(normally else is not used in other languages)
secret_word = "zootopia"
pw = ""
authorized = False
attempt_count = 0

while pw != secret_word:
    attempt_count += 1
    if attempt_count > 5: break  # It will break out from the loop
    if attempt_count == 3: continue  # It will skip the below lines in the loop and continue from top
    pw = input(f"{attempt_count}. What's the secret word?\t")
else:
    authorized = True  # This line will execute if the loop doesn't break

print("You may enter!" if authorized else "Calling the police...!!!")
