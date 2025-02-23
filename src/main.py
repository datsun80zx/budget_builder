from csv_parser import node_create
def main():
    file = "bank.csv"
    list = node_create(file)

    print(f"{list[0]}\n{list[1]}")


if __name__ == "__main__":
    main()

