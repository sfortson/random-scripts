import click


def factorial_iterative(n):
    if type(n) != int or n < 0:
        raise ValueError('Input must be a positive integer')

    ans = 1
    for i in range(n, 1, -1):
        ans *= i
    return ans


def factorial_recursive(n):
    if type(n) != int or n < 0:
        raise ValueError('Input must be an integer')

    if n == 0:
        return 1

    return n * factorial_recursive(n - 1)


@click.command()
@click.argument('num')
@click.option('-i', '--iterative', is_flag=True, default=False, help='Use the iterative solution')
def main(num, iterative):
    if iterative:
        print(factorial_iterative(int(num)))
    else:
        print(factorial_recursive(int(num)))


if __name__ == '__main__':
    main()
