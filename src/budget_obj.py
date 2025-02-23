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
        pass

    def _create_node(self, csv_line):
        self.__type__ = csv_line[0]
        self.__desc__ = csv_line[2]
        self.__date__ = csv_line[1]
        self.__amnt__ = round(float(csv_line[3]), 2)

    def __repr__(self):
        return f"CSVNode:\ntype: {self.__type__}\ndescription: {self.__desc__}\ndate: {self.__date__}\ntotal: {self.__amnt__:.2f}\n"
            

