import argparse


def probability(num_people):
    i = 0
    p = 1.0
    while i < num_people:
        p = p * (1 - (float(i)/365))
        i += 1
    return 1.0 - p


def main():
    parser = argparse.ArgumentParser("Compute birthday problem.")
    parser.add_argument('num_people')
    args = parser.parse_args()

    print(100 * probability(int(args.num_people)))


if __name__ == '__main__':
    main()
