# Okay so I want to first group the transactions by date: 

from budget_obj import CSVNode


# function takes a list of CSVNodes and then puts them in a list of nodes by month. 
def group_by_date(list):
    year = []
    for m in range(12): 
        month = []
        for node in list: 
            if m == int(node.__date__.split("/")[1]) and node.__date__.split('/')[0] == "2024":
                month.append(node)
        year.append(month)
    return year

