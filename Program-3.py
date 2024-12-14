def generate_series(a):
    result = []
    if a == 1 or a == 2:
        return [1]
    else:
        num = 1
        for i in range(a):
            result.append(num)
            num += 2
            if len(result) == (a // 2) * 2 + 1 and a % 2 != 0:
                break
        if a % 2 == 0 and a > 2:
            result = result[:a - 1]
    return result
try:
    a = int(input("Enter a number: "))
    series = generate_series(a)
    print("Output:", ", ".join(map(str, series)))
except ValueError:
    print("Please enter a valid integer.")
