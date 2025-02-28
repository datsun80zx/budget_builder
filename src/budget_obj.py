import csv
import re
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
        self._date_formatter()
        self._get_name()
        

    def _get_name(self):
        desc = self.__desc__.strip()

        if desc.startswith("ATM WITHDRAWAL"):
            return "ATM"

        if "REAL TIME PAYMENT" in desc and "MONEYLION" in desc.upper():
            self.__name__ = "MoneyLion Instacash"
            return
        
        if "OVERDRAFT FEE" in desc.upper():
            self.__name__ = "Bank Fee - Overdraft"
            return
        
       # Apply merchant-specific mappings
        merchant_mappings = {
        "DAVE INC": "Dave",
        "DAVE": "Dave",
        "CHARLES SCHWAB & PAYROLL": "Payroll - Schwab",
        "MEIJER EXPRESS 323": "Meijer Gas",
        "MEIJER STORE #323": "Meijer",
        "SCHWAB MKTPL RCHFLD": "Schwab Market",
        "AM INCOME LIFE": "Insurance - American Income Life",
        "PLANET FIT": "Planet Fitness",
        "INSTACASH REPAYMENT": "MoneyLion Repayment",
        "BOOT.DEV EDUCATION": "Boot.dev",
        "SCRIBD": "Scribd",
        "NETFLIX": "Netflix",
        "SPOTIFY USA": "Spotify",
        "OPENAI *CHATGPT": "ChatGPT Plus",
        "CLAUDE.AI": "Claude AI",
        "CRUNCHYROLL": "Crunchyroll",
        "CANVA": "Canva",
        "ECM, A LEGALZOOM CO.": "LegalZoom",
        "LEGALZOOM.COM": "LegalZoom",
        "LEGALZOOM": "LegalZoom",
        "ZOOM.COM": "Zoom",
        "NOTION LABS": "Notion",
        "FREECODECAMP.ORG": "FreeCodeCamp",
        "AUDIBLE": "Audible",
        "GOOGLE *LASTPASS": "LastPass",
        "GOOGLE *HIDIVE": "HIDIVE",
        "DD *DOORDASHDASHPASS": "DoorDash Pass"
    }

        # split off the PPD ID and cleans up the whitespace before and after if any. 
        cleaned_desc = desc.split("PPD ID:")[0].strip()

        # Sort merchant mappings by key length (longest first) to prioritize more specific matches
        sorted_mappings = sorted(merchant_mappings.items(), key=lambda x: len(x[0]), reverse=True)
        
        for key, value in sorted_mappings:
            # Check if it's a complete word match using word boundaries
            if re.search(r'\b' + re.escape(key) + r'\b', cleaned_desc.upper()):
                self.__name__ = value
                return
            # Or if it starts with the key (for beginning-of-string matches)
            elif cleaned_desc.upper().startswith(key):
                self.__name__ = value
                return
            
        subscription_pattern = r"(?:GOOGLE|AMZN|APPLE) \*([A-Za-z0-9\.\s]+)"
        match = re.search(subscription_pattern, cleaned_desc, re.IGNORECASE)
        if match:
            self.__name__ = match.group(1).strip().title()
            return

        cleaned_desc = ' '.join(part for part in desc.split() if not part.startswith(('01/', '02/', '03/', '04/', '05/', '06/', '07/', '08/', '09/', '10/', '11/', '12/')))
        # print(desc)

        # create a list of common state abbrev. to split off, 
        states = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 
              'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 
              'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 
              'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
        
        words = cleaned_desc.split()

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
        
        self.__name__ = name.strip().title()

    def _create_node(self, csv_line):
        self.__type__ = csv_line[0]
        self.__desc__ = csv_line[2]
        self.__date__ = csv_line[1]
        self.__amnt__ = round(float(csv_line[3]), 2)

# turns date from mm/dd/yyyy into yyyy/mm/dd
    def _date_formatter(self):
        raw_dates = self.__date__.split("/")
        self.__date__ = raw_dates[2] + "/" + raw_dates[0] + "/" + raw_dates[1]
        
    def __repr__(self):
        return f"CSVNode:\nname: {self.__name__}\ntype: {self.__type__}\ndescription: {self.__desc__}\ndate: {self.__date__}\ntotal: {self.__amnt__:.2f}\n"
            

