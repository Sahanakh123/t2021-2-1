def count_multiples(numbers):
    counts = {i: 0 for i in range(1, 10)}
    for number in numbers:
        for i in range(1, 10):
            if number % i == 0:
                counts[i] += 1 
    return counts
numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
result = count_multiples(numbers)
print(result)
