from csv_parser import node_create, path_create
from transaction_processor import transaction_counts, sort_by_type, group_by_date, date_sort

def main():
    file = "bank.csv"
    path = path_create(file)
    list = node_create(path)
    year = 2024
    month = 9

    sorted_list = date_sort(list, year, month)
    credit, debit = sort_by_type(sorted_list)

    
    breakdown_of_credit_transactions = transaction_counts(credit)
    breakdown_of_debit_transactions = transaction_counts(debit)

    # print(credit)
    # print(debit)

    
    print(f"Calculating Credit Transactions...")
    sort_by_num_credit = sorted(breakdown_of_credit_transactions.items(), key=lambda x: x[1], reverse=True)
    for i in sort_by_num_credit:
        total = i[1]
        print(f"Transaction Name: {i[0]}, Number of transactions: {total}")
    
    print(f"\nCalculating Debit Transactions...")
    sort_by_num_debit = sorted(breakdown_of_debit_transactions.items(), key=lambda x: x[1], reverse=True)
    for j in sort_by_num_debit:
        total = j[1]
        print(f"Transaction Name: {j[0]}, Number of transactions: {total}")
    

if __name__ == "__main__":
    main()

