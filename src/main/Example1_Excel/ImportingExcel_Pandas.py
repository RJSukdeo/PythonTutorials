import pandas


def main():
    names = pandas.read_excel("../Names.xlsx", index_col=0)
    for name in names.index.array:
        print(name)


if __name__ == '__main__':
    main()
