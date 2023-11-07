def fibonacci(n):
    if n <= 0:
        return "Invalid input"
    elif n == 1:
        return [0], 0
    elif n == 2:
        return [0, 1], 1
    else:
        series = [0, 1]
        a, b = 0, 1
        steps = 1
        while n > 2:
            c = a + b
            series.append(c)
            a, b = b, c
            steps += 1
            n -= 1
        return series, steps
n = int(input('Enter number: '))
print(fibonacci(n))
