from Hamming import Hamming


def main():
    hamming = Hamming(
        n=7,
        m=4
    )
    data = "1111111"
    print(hamming.decode(data))


if __name__ == '__main__':
    main()
