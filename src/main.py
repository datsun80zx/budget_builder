from csv_parser import node_create, path_create
def main():
    file = "bank.csv"
    path = path_create(file)
    list = node_create(path)

    # print(f"{list[0]}\n{list[1]}")
    for node in list:
        print(node)


if __name__ == "__main__":
    main()

