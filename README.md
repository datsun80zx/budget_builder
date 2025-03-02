# budget_builder

## Summary Of Project: 
This project was designed to test my understanding of some of the basic data types and data transformations that I currently have a decent understanding of. 
At this point this tool isn't everything I want it to be but it is a pretty good foundation. Currently the functionality built out will: 

- take a provided csv of banking transactions, process them down into transaction node
- sort each node by several different filters including: 
    - Date(from some provided date to most recent)
    - Date(Year and month)
    - Transaction type(Debit & Credit)
- output into the terminal a human readable breakdown. 

## Future Ideas: 
I would like to rewrite in Golang and then provide some simple UI as well as possible integration into banks through something like Plaid. 

## Concepts used: 
- Control flow
- system access for files
- data cleaning and parsing 
- OOP design princpals 