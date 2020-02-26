import click
from math import sqrt
import sys


@click.command()
@click.argument('number', type=click.INT)
def main(number):
    print sieve_of_eratosthenes(number)


def sieve_of_eratosthenes(number):
    if number <= 1:
        sys.exit('Input number must be greater than 1')

    prime_array = [True for x in range(number + 1)]

    for i in range(2, int(round(sqrt(number)))):
        if prime_array[i]:
            j = i**2
            idx = 0
            while j <= number:
                prime_array[j] = False
                j = i**2 + idx*i
                idx += 1

    primes = []
    for i in range(2, len(prime_array)):
        if prime_array[i]:
            primes.append(i)

    return primes


if __name__ == '__main__':
    main()
