# Documentation

I am writing some documentation which will also be useful for me.

#### Index:

1. Technologies used
2. Relational Database
3. Interface

## Technologies used

I am using:

- Raspberry Pi 4 as a server
- Raspbian+Apache+SQL+PHPMyAdmin
- Python

## Relational Database

Later on I will try to provide a graphic representation.

I report here the logical schema, primary keys in *italic* and foreign keys **bold**. We add 'NULL' if the attribute is nullable. We add 'UNIQUE' if the Attribute is Unique

Area(*Code* tinyint unsigned, Address, verchar (50), City varchar(15), Email varchar(20), pec varchar(24))

Branch( *Code* tinyint unsigned, Address varchar(50), City varchar(15), Telephone int, Type Set:{'Retail', 'Affluent', 'Corporate'}, Pec varchar(29), Email varchar(25), **Area** code field from Area table)

Employee( *ID* smallint, **Branch** code field from Branch, SSN UNIQUE char 16, Birth date, Name varchar(15), Surname varchar(15), Address varchar(50), City varchar(15), Cellphone  int, SecondaryPhone NULL int, Email varchar(25), DocumentID UNIQUE char(20))

Private(*SSN* char(16), DocumentID UNIQUE char(20), Email varchar(25), Telephone int, SecondaryPhone NULL int, Birth date, Address varchar(50), City varchar(15)) //Privates are people who are customers of the bank; the other tupe of customers are companies

Company(*TaxCode* char(11), Address varchar(50), City varchar(15), Foundation date, Email varchar(25), Telephone int, Website NULL varchar(25), Representative varchar(30))

Binder(*Code* char(20), **Branch** code field from Branch, Type Set:{'Individual', 'Joint', 'Company'}) //It identifies a relation between the bank and a customer. The relation can be: individual (single person), company or joint (only for multiple people)

PeopleBinder(**Binder** code field from Binder, **SSN** SSN field from Private) // has all binders for individuals and joint; if you want to know how many people are in a joint one, simply use count(). To know the type, it's better to go to Binder table

CompanyBinder**Binder** code field from Binder, **TaxCode** TaxCode field from Company)

Contract(*Code* char(20), **Binder** Binder field from Binder, Type Set:{'Checking Account', 'Savings Account', 'Credit Card', 'Debit Card'})

Account(*IBAN* char(25), **Contract** code field from Contract, Interest float, OpeningDate date, Balance, Type Set:{'Checking', 'Savings'})

Card(*Code* int, ExpiryDate date, EmissionDate date, Price float, **Contract** field from Contract, Price float, Type Set:{'Debit','Credit'})

LOGICAL SCHEMA NOT YET COMPLETED!

We make the following assumptions (note that they are still susceptible to changes):

- Companies and Privates can buy the same type of products
- It is not possible to wire transfer money to other banks