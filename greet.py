import sys


def greet(name: str) -> str:
    return f"Hello, {name}!"


def main() -> int:
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "world"
    print(greet(name))
    return 0


def test_greet():
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    raise SystemExit(main())
