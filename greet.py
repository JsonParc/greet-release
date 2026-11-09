import sys


def greet(name: str, punctuation: str = "!") -> str:
    # 공백만 있거나 빈 이름이면 "world"를 사용한다.
    if name.strip() == "":
        name = "world"
    return f"Hello, {name}{punctuation}"


def main() -> int:
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = "world"
    print(greet(name))
    return 0


def test_greet():
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank():
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation():
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
