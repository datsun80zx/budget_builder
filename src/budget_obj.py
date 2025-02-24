import csv
from enum import Enum


class Type(Enum):
    DEBIT = 1
    CREDIT = 2

class Transaction:
    def __init__(self, name, description, date, type: Type, amount):
        self.__name__ = name
        self.__desc__ = description
        self.__date__ = date
        self.__type__ = type
        self.__amount__ = amount

    def _categorize_transaction(self):
        pass

class CSVNode:
    def __init__(self, line):
        self.__type__ = ""
        self.__desc__ = ""
        self.__date__ = ""
        self.__amnt__ = 0.0
        self.__name__ = ""
        self._create_node(line)

    def _get_name(self):
        desc = self.__desc__.strip()

        if desc.startswith("ATM WITHDRAWAL"):
            return "ATM"
        
        # split off the PPD ID and cleans up the whitespace before and after if any. 
        desc = desc.split("PPD ID:")[0].strip()
    

        desc = ' '.join(part for part in desc.split() if not part.startswith(('01/', '02/', '03/', '04/', '05/', '06/', '07/', '08/', '09/', '10/', '11/', '12/')))
        # print(desc)

        # create a list of common state abbrev. to split off, 
        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 
              'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 
              'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 
              'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        
        words = desc.split()

        cutoff_idx = len(words)
        for i, word in enumerate(words):
            if word in states:
                cutoff_idx = i - 1
                break

        name = ' '.join(words[:cutoff_idx])
        # print(name)

        # remove some common suffixes
        sfx_to_remove = ["CLUB FEES", "INS.PREM"]
        for suffix in sfx_to_remove: 
            if suffix in name.upper():
                name = name.replace(suffix, '').strip()
        
        print(name.strip().title())




    def _create_node(self, csv_line):
        self.__type__ = csv_line[0]
        self.__desc__ = csv_line[2]
        self.__date__ = csv_line[1]
        self.__amnt__ = round(float(csv_line[3]), 2)

    def __repr__(self):
        return f"CSVNode:\ntype: {self.__type__}\ndescription: {self.__desc__}\ndate: {self.__date__}\ntotal: {self.__amnt__:.2f}\n"
            

