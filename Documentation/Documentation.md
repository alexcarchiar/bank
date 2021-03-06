# Documentation

I am writing some documentation which will also be useful for me.

Current version: 0.2

The program is not functional, we currently have only the database structure and on my machine I filling it up. Once I have a few records here and there, I am going to start writing the Python code to interact with the database and then start making the rest of the application.

#### Version control:

- 0.1: created the backbone of the database
- 0.2: created the classes and established connection using remote.it to intereact with the database

#### Index:

1. Technologies used
2. Relational Database
3. Interface

## 1. Technologies used

I am using:

- Raspberry Pi 4 as a server
- MacOS Catalina as a client
- Raspbian+Apache+SQL+PHPMyAdmin
- Python. Modules:
  - proprietary (documentation below)
  - mysql connector (official mysql module to interact with MySQL server)

## 2. Relational Database

Later on I will try to provide a graphic representation.

I report here the logical schema, primary keys in *italic* and foreign keys **bold**. We add 'NULL' if the attribute is nullable. We add 'UNIQUE' if the Attribute is Unique

Area(*Code* tinyint unsigned, Address, varchar (50), City varchar(15), Email varchar(20), pec varchar(24))

Branch( *Code* tinyint unsigned, Address varchar(50), City varchar(15), Telephone int, Type Set:{'Retail', 'Affluent', 'Corporate'}, Pec varchar(29), Email varchar(25), **Area** code field from Area table)

Employee( *ID* smallint, **Branch** NULL code field from Branch, SSN UNIQUE char(16), Birth date, Name varchar(15), Surname varchar(15), Address varchar(50), City varchar(15), Cellphone  int, SecondaryPhone NULL int, Email varchar(25), DocumentID UNIQUE char(20), **Area** NULL code field from Area) //only one between **Branch** and **Area** can be NULL, since an employee either works in a branch or in a area hq

Private(*SSN* char(16), DocumentID UNIQUE char(20), Email varchar(25), Telephone int, SecondaryPhone NULL int, Birth date, Address varchar(50), City varchar(15), Name varchar(15), Surname varchar(15)) //Privates are people who are customers of the bank; the other tupe of customers are companies

Company(*TaxCode* char(11), Address varchar(50), City varchar(15), Foundation date, Email varchar(25), Telephone int, Website NULL varchar(25), Representative varchar(30))

Binder(*Code* char(20), **Branch** code field from Branch, Type Set:{'Individual', 'Joint', 'Company'}) //It identifies a relation between the bank and a customer. The relation can be: individual (single person), company or joint (only for multiple people)

PrivateBinder(**Binder** code field from Binder, **SSN** NULL SSN field from Private) // has all binders for individuals and joint; if you want to know how many people are in a joint one, simply use count(). To know the type, it's better to go to Binder table

CompanyBinder(**Binder** code field from Binder, **TaxCode** TaxCode field from Company)

Contract(*Code* char(20), **Binder** Binder field from Binder, Type Set:{'Checking Account', 'Savings Account', 'Credit Card', 'Debit Card'})

Account(*IBAN* char(25), **Contract** code field from Contract, Interest float, OpeningDate date, Balance, Type Set:{'Checking', 'Savings'})

Card(*Code* int, ExpiryDate date, EmissionDate date, Price float, **Contract** field from Contract, Type Set:{'Debit','Credit'})

RecordPayment(**SenderSSN** NULL SSN field from Private, **SenderTaxCode** NULL TaxCode field from Company ***SenderBinder*** code field from Binder, **ReceiverSSN** NULL SSN field from Private, **ReceiverTaxCode** NULL TaxCode field from Company ***ReceiverBinder*** code field from Binder, PaymentType SET:{'WireTransfer', 'CreditCard', 'DebitCard', 'Check', 'Deposit', 'Withdrawal'}, *Date* timestamp, Commission float )
The RecordPayment table keeps track of all money transfers. At least one between SenderSSN and SenderTaxCode need to be not null (it is the one making the operation). In case the PaymentType is Withdrawal or Deposit, we do not need any receiver since the operation is done on the same account. If the PaymentType is one of the other four categories, then we need one between ReceiverSSN and ReceiverTaxCode. Commision is the money the bank charges for the operation.

We make the following assumptions (note that they are still susceptible to changes):

- Companies and Privates can buy the same type of products
- It is not possible to wire transfer money to other banks

## 3. Python code

We have the following modules:

- bank.py

### Bank.py

This module contains all the classes and helper functions needed in order to correctly manage a banking system. I am probably also going to put here all the functions that are more specific to this banking system, that is, the functions to make money transfers, open accounts and everything else.

#### Area

class Area(code, address, city, email, pec, telephone).
All the attributes are the ones found in Area table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Area) is called)
- class string representation used to have a quick representation of Area's attributes (it is shorter than string format)
- addToDatabase(self, mydb) stores into the database the current Area

#### Branch

class Branch(code, address, city, email, telephone, area *code*, pec, type).
All the attributes are the ones found in Branch table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Branch) is called)
- class string representation used to have a quick representation of Branch's attributes (it is shorter than string format)
- addToDatabase(self, mydb) stores into the database the current Branch

#### Employee

class Employee(ID, branc *code* , ssn, birth, name, surname, address, city, cellphone, secondaryPhone, email, documentID, area *code*)
All the attributes are the ones found in Employee table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Employee) is called)
- class string representation used to have a quick representation of Employee's attributes (it is shorter than string format)
- addToDatabase(self, mydb) stores into the database the current Employee

#### Private

class Private(ssn, documentID, email, telephone, secondaryphone, birth, address, city, name, surname)
All the attributes are the ones found in Private table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Private) is called)
- class string representation used to have a quick representation of Private's attributes (it is shorter than string format)

#### Company

class Company(taxCode, address, city, foundationDate, email, telephone, website, representative)
All the attributes are the ones found in Company table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Company) is called)
- class string representation used to have a quick representation of Company's attributes (it is shorter than string format)

#### Binder

class Binder(code, branch, typ)
All the attributes are the ones found in the Binder table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Binder) is called)
- class string representation used to have a quick representation of Binder's attributes (it is shorter than string format)

#### PrivateBinder

class PrivateBinder(binder *code*, ssn)
All the attributes are the ones found in the PrivateBinder table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(PrivateBinder) is called)
- class string representation used to have a quick representation of PrivateBinder's attributes (it is shorter than string format)

#### CompanyBinder

class CompanyBinder(binder *code*, taxCode)
All the attributes are the ones found in the CompanyBinder table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(CompanyBinder) is called)
- class string representation used to have a quick representation of CompanyBinder's attributes (it is shorter than string format)

#### Contract

class Contract(code, branch *code*, binder *code*, type)
All the attributes are the ones found in the Contract table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Contract) is called)
- class string representation used to have a quick representation of ContractBinder's attributes (it is shorter than string format)

#### Account

class Account(iban, contract *code*, interest, openingDate, balance, type)
All the attributes are the ones found in the Account table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Account) is called)
- class string representation used to have a quick representation of Account's attributes (it is shorter than string format)
- addToDatabase(self, mydb): it is used to add the current account to the database mydb

#### Card

class Card(code, expirtyDate, emissionDate, price, contract *code*, type)
All the attributes are the ones found in the Card table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(Card) is called)
- class string representation used to have a quick representation of Card's attributes (it is shorter than string format)

#### RecordPayment

class RecordPayment(senderSSN, senderTaxCode, senderBinder, receiverSSN, receiverTaxCode, receiverBinder, paymentType, date, commission)
All the attributes are the ones found in the RecordPayment table (see the *2. Relational Database* in the documentation)

We have the following methods:

- class constructor
- class string format (used when print(RecordPayment) is called)
- class string representation used to have a quick representation of RecordPayment's attributes (it is shorter than string format)

#### Functions

- createConnection(hostname, portnumber):
  	this function establishes a connection with the database and returns it. It is used to call mysql.connector.connect() faster and without having to write all parameters.