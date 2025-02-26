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
    
