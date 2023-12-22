char_input = input("Enter a character: ")

for i in range(1, 6):
    if i % 2 == 1:
        print(char_input * i)
    else:
        print(char_input * (i - 1) + char_input.upper())