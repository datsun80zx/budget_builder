from csv_parser import node_create, path_create
from transaction_processor import group_by_date


def main():
    file = "bank.csv"
    path = path_create(file)
    list = node_create(path)

    # print(f"{list[0]}\n{list[1]}\n{list[2]}\n{list[3]}\n{list[4]}")
    # # for node in list:
    # #     node._get_name()

    # list[0]._get_name()
    # list[1]._get_name()
    # list[2]._get_name()
    # list[3]._get_name()
    # list[4]._get_name()

    transactions_by_year = group_by_date(list)
    # for key in transactions_by_year[2025]: 
    transaction = transactions_by_year[2025][1]
    for trans in transaction:
        print(trans.__name__)
    
    

if __name__ == "__main__":
    main()

