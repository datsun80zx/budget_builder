# Okay so I want to first group the transactions by date: 

from budget_obj import CSVNode


# function takes a list of CSVNodes and then puts them in a list of nodes by month. 
def group_by_date(list):
    year_dict = {}
    for node in list:
        date_parts = node.__date__.split("/")
        year = int(date_parts[0])
        month = int(date_parts[1])

        # create a year and month if it doesn't exist
        if year in year_dict:
            if month in year_dict[year]:
                year_dict[year][month].append(node)
            else:
                year_dict[year][month] = []
                year_dict[year][month].append(node)

        else:
            year_dict[year] = {}
            year_dict[year][month] = []
            year_dict[year][month].append(node)

    return year_dict

def date_sort(list, year: int, month: int):
    sorted_list = []
    for node in list: 
        date_parts = node.__date__.split("/")
        yr = int(date_parts[0])
        mth = int(date_parts[1])
        if yr > year:
            sorted_list.append(node)
        elif yr == year and mth >= month:
            sorted_list.append(node)
    return sorted_list

# sort the transactions by credit or debit. 
def sort_by_type(list_of_nodes):
    credit_nodes = []
    debit_nodes = []
    for node in list_of_nodes: 
        if (node.__type__).upper() == "CREDIT":
            credit_nodes.append(node)
        elif (node.__type__).upper() == "DEBIT": 
            debit_nodes.append(node)
    return credit_nodes, debit_nodes

# I want to count the number of times a transaction occurs. I'll use a dictionary to do this. 

def transaction_counts(list_of_nodes):
    transactions = {}
    for node in list_of_nodes: 
        if node.__name__ in transactions:
            transactions[node.__name__] += 1
        else:
            transactions[node.__name__] = 1

    return transactions