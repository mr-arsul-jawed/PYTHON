def sum_of_series(n):
    sum_series = 0
    for i in range(1, n+1):
        sum_series += i**2
    return sum_series


n = int(input("Enter the value of n: "))


print("Sum of the series is:", sum_of_series(n))
