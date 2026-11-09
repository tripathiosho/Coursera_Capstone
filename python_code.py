print("Hello Github!")

def print_numbers(n):
    if n == 0:
        print(n)
        return
    print(n)
    print_numbers(n-1)

print_numbers(5)