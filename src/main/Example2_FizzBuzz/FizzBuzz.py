def main():
    for i in range(1, 100):
        divisibleByThree = i % 3
        divisibleByFive = i % 5
        if divisibleByThree != 0 and divisibleByFive != 0:
            print(i)
            continue
        outputString = ""
        if divisibleByThree == 0:
            outputString += "Fizz "
        if divisibleByFive == 0:
            outputString += "Buzz"
        print(outputString)

if __name__ == '__main__':
    main()
