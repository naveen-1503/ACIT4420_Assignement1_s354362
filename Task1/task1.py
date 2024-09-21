def find_prime_factors(n):
    prime_factors = []

    while n % 2 == 0:
        prime_factors.append(2)
        n //= 2
    
    i=3
    while i * i <= n:
        if n % i == 0:
            prime_factors.append(i)
            n //= i
        else:
            i+=2
    
    if n>1:
        prime_factors.append(n)
    return prime_factors


print(f'The prime factors of 5 is: {find_prime_factors(5)}')
print(f'The prime factors of 8 is: {find_prime_factors(8)}')
print(f'The prime factors of 999 is: {find_prime_factors(999)}')
print(f'The prime factors of 150000 is: {find_prime_factors(150000)}')

#Result in PDF file