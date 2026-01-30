def prime_no():
    num = int(input("Enter a number: "))
    if num <= 1:
        print(f"{num} is not a prime number.")
        return
    else:
        for i in range(2, num):
            if num % i == 0:
                print(f"{num} is not a prime number.")
                return
        print(f"{num} is a prime number.")




info = {
    "author": "Data Analytics Team",
    "version": "1.0",
    "description": "A module to check if a number is prime."
}