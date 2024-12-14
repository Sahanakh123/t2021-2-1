def generate_series(a):
    result = []
    num = 1
    for _ in range(a):
        result.append(num)
        num += 2
    return result
try:
    a = int(input("Enter a number: "))
    series = generate_series(a)
    print("Output:", ", ".join(map(str, series)))
except ValueError:
    print("Please enter a valid integer.")
