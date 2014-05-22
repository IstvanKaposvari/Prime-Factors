def primeFactors(number):
    factors = []
    number = abs(number)
    if number < 2:
        return factors
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            factors.append(i)
            return factors + primeFactors(number // i)
    factors.append(number)
    return factors

if __name__ == "__main__":
    number = None
    while number is None:
        try:
            number = int(input('Choose an integer: '))
            print ('Prime factors of your number: ' + str(primeFactors(number)))
        except ValueError:
            print ('Not an integer!')