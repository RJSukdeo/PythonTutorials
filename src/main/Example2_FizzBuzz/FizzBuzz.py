def main():
    for i in range(1, 100):
        divisibleByThree = i % 3
        divisibleByFive = i % 5
        if divisibleByThree != 0 and divisibleByFive != 0:
            print(i)
            continue
        output = ""
        if divisibleByThree == 0:
            output += "Fizz "
        if divisibleByFive == 0:
            output += "Buzz"
        print(output)


if __name__ == '__main__':
    main()
