print(__file__)

numbers = [1, 2, 3, 4, 5, 6]

number = int(input("Enter a number and I'll tell you it's square: \n"))
squares = []
squares = [number ** 2 for number in range(1, 7)]
for number in numbers:
    squares.append(number ** 2)

index_pos = numbers.index(number)
print(squares[index_pos])
