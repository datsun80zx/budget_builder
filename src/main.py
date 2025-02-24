from csv_parser import node_create, path_create
def main():
    file = "bank.csv"
    path = path_create(file)
    list = node_create(path)

    print(f"{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}")
    # for node in list:
    #     node._get_name()

    list[0]._get_name()
    list[1]._get_name()
    list[2]._get_name()
    list[3]._get_name()
    list[4]._get_name()


if __name__ == "__main__":
    main()

