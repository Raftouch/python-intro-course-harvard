def main():
    hello(name='Bob')
    goodbye(name='Bob')


def hello(*, name: str) -> None:
    print(f"hello, {name}")


def goodbye(*, name: str) -> None:
    print(f"goodbye, {name}")


if __name__ == "__main__":
    main()