#!/user/bin/env python3

def print_fibonacci(length):
    pass
    fibonacci_sequence = []
    if length > 0:
            fibonacci_sequence.append(0)
            if length >1:
                fibonacci_sequence.append(1)
                if length >2:
                    for i in range(2, length):
                        fibonacci_sequence.append(
                            fibonacci_sequence[i -1] + fibonacci_sequence [i-2])
                         
    print(fibonacci_sequence)


# def print_fibonacci(length):
#     # Initialize variables
#     a = 0
#     b = 1
#     fibonacci_sequence = []

#     # Calculate the Fibonacci sequence up to the provided length
#     for i in range(length):
#         fibonacci_sequence.append(a)
#         temp = a + b
#         a = b
#         b = temp

#     # Print the Fibonacci sequence
#     print("Fibonacci sequence:")
#     if length == 0:
#         print("[]")
#     else:
#         print(fibonacci_sequence)

