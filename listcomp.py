print(__file__)

squares = [number ** 2 for number in range(1, 7)]
number = int(input("Enter a number and I'll tell you it's square: \n"))

# print(squares)
index_pos = range(1, 7).index(number)
print(squares[index_pos])
