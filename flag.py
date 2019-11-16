import argparse


class ArgumentError(Exception):
    def __init__(self, message):
        self.message = message


def validate_number(number):
    if number % 2:
        raise ArgumentError("Input parameter N should be an even number")
    if not number:
        raise ArgumentError("Input parameter N shouldn't be 0")


def border(func):
    def wrapper(N):
        border = "#"*(3*N+2)
        return border + "\n" + func(N) + border
    return wrapper


def empty_place(func):
    def wrapper(N):
        return add_empty_place(N) + func(N) + "\n" + add_empty_place(N)
    return wrapper


def add_empty_place(N):
    result = ""
    for i in range(int(N/2)):
        result += "#"+" "*3*N+"#"+"\n"
    return result


@border
@empty_place
def flag(N):
    validate_number(N)
    half_of_string = "#" + " " * int(N*1.5-1) + "*"
    result = [half_of_string + half_of_string[::-1]]
    for i in range(1, int(N/2)):
        full_string = half_of_string[0] + half_of_string[i+1:] + "o" * i
        full_string += full_string[::-1]
        result.append(full_string)
    result.extend(result[::-1])
    return "\n".join(result)


def main():
    parser = argparse.ArgumentParser(description="ACSII art of an japanese flag")
    parser.add_argument("N", metavar="N", type=int, help="input parameter")
    try:
        args = parser.parse_args()
        print(flag(args.N))
    except ArgumentError as e:
        print(e)


if __name__ == "__main__":
    main()
