"""
This module contains all the classes and helper functions
needed in order to correctly manage a banking system.
I am probably also going to put here all the functions
that are more specific to this banking system,
that is, the functions to make money transfers,
open accounts and everything else.
"""

import mysql.connector

class Area:
    """
    This class is used to deal with Area. Its attributes are the ones
    used in the Area table. Look it up in the documentatoin
    if needed
    """
    def __init__(self, code, address, city, email, pec):
        """
        Class contructor method for Area. It takes as input
        the fields from the table Area and it stores them into
        an object in order to deal with it.
        """
        self.code = code
        self.address = address
        self.city = city
        self.email = email
        self.pec = pec
    
    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'This Area has code ' + str(self.code) + ' located at ' + self.address + ' ' + self.city + ' and the contact information is ' + self.email + ' ' + self.pec
        print(string)
    def __repr(self):
        """
        Special method used to print all of the attribute of the current object
        """
        string = 'Area( ' + str(self.code) + ', ' + self.address + ', ' + self.city + ', ' + self.email + ', ' + self.pec + ')'
        print(string)

class Branch:
    """
    This class is used to deal with Branch. Its attributes are the same
    used in the Branch table. Look it up in the documentation
    if needed.
    """
    def __init__(self, code, address, city, email, telephone, area, pec, typ):
        """
        Class contructor method for Branch. It takes as input
        the fields from the table Branch and it stores them into
        an object in order to deal with it.
        """
        self.code = code
        self.address = address
        self.city = city
        self.email = email
        self.telephone = telephone
        self.area = area
        self.pec = pec
        self.type = typ #using typ since type is a python keyword
    
    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'This Branch has code ' + str(self.code) + ', area: ' + str(self.area) + ', located at ' + self.address + ' ' + self.city + '. It is a ' + self.type + 'branch. Contacts: ' + self.email + ' ' + self.pec + ' ' + str(self.telephone)
        print(string)
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Branch( ' + str(self.code) + ', ' + str(self.area) + ', ' + self.address + ', ' + self.city + ', ' + self.type + ', ' + self.email + ', ' + self.pec + ', ' +str(self.telephone) + ')'
        print(string)

class Employee:
    """
    This class is used to deal with Employee. Its attributes are the same
    used in the Employee table. Look it up in the documentation
    if needed.
    """
    def __init__(self, ID, branch, ssn, birth, name, surname, address, city, cellphone, secondaryPhone, email, documentID, area):
        """
        Class contructor method for Employee. It takes as input
        the fields from the table Employee and it stores them into
        an object in order to deal with it.
        """
        self.id = ID
        self.branch = branch
        self.ssn = ssn
        self.name = name
        self.surname = surname
        self.address = address
        self.city = city
        self.cellphone = cellphone
        self.secondaryPhone = secondaryPhone
        self.email = email
        self.documentID = documentID
        self.area = area
        self.birth = birth
    
    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'The Employee code ' + self.id + 'is ' + self.name + ' ' + self.surname + ' born on ' + self.birth +' works at branch ' + str(self.branch) + ' in area ' + str(self.area) + '. The registerd document is: ' + self.documentID + 'with SSN: ' + self.ssn + ' lives in ' + self.address + ' ' + self.city + 'contact information: email is ' + self.email + ' cellphone: ' + str(self.cellphone)
        if(self.secondaryPhone != None):
            string += 'secondary phone is: ' + str(self.secondaryPhone)
        print(string)

    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string  = 'Area( ' + self.id + ', ' + str(self.branch) + ', ' + str(self.area) + ', ' + self.ssn + ', ' + self.documentID + ', ' + self.name + ', ' + self.surname + ', ' + self.birth + ', ' + self.address + ', ' + self.city + ', ' + self.email + ', ' + self.cellphone + ', '
        if(self.secondaryPhone != None):
            string += str(self.secondaryPhone)
        else:
            string += 'None'
        string += ')'
        print(string)
    
class Private:
    """
    This class is used to deal with Private. Its attributes are the same
    used in the Private table. Look it up in the documentation
    if needed.
    """
    def __init__(self, ssn, documentID, email, telephone, secondaryphone, birth, address, city, name, surname):
        """
        Class contructor method for Private. It takes as input
        the fields from the table Private and it stores them into
        an object in order to deal with it.
        """
        self.ssn = ssn
        self.documentID = documentID
        self.email = email
        self.telephone = telephone
        self.secondaryPhone = secondaryphone
        self.birth = birth
        self.address = address
        self.city = city
        self.name = name
        self.surname = surname
    
    def __str__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'This private has SSN ' + self.ssn + ' and the registerd document is ' + self.documentID + '. The name is ' + self.name + ' ' + self.surname + 'born on ' + self.birth + ', lives in ' + self.address + ' ' + self.city + '. Contact information: email: ' + self.email + ' telephone: ' + self.telephone
        if(self.secondaryPhone != None):
            string += ' the secondary phone is: ' + self.secondaryPhone
        print(string)

    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Private( ' + self.ssn + ', ' + self.documentID + ', ' + self.name + ', ' + self.surname + ', ' + self.birth + ', ' + self.email + ', ' + self.telephone
        if(self.secondaryPhone != None):
            string += str(self.secondaryPhone)
        else:
            string += 'None'
        string += ')'
        print(string)

class Company:
    """
    This class is used to deal with Company. Its attributes are the same
    used in the Company table. Look it up in the documentation
    if needed.
    """
    def __init__(self, taxCode, address, city, foundationDate, email, telephone, website, representative):
        """
        Class contructor method for Company. It takes as input
        the fields from the table Company and it stores them into
        an object in order to deal with it.
        """
        self.taxCode = taxCode
        self.address = address
        self.city = city
        self.foundationDate = foundationDate
        self.email = email
        self.telephone = telephone
        self.website = website
        self.representative = representative
    
    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'The company has tax code ' + self.taxCode + ' founded on ' + self.foundationDate + '. Headquarters in ' + self.address + ' ' + self.city + '. Contact information: email ' + self.email + ' telephone ' + str(self.telephone) 
        if(self.website != None):
            string += 'the website is ' + self.website
        string += '. The representative is ' + self.representative
        print(string)

    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Company( ' + self.taxCode + ', ' + self.address + ', ' + self.city + ', ' + self.foundationDate + ', ' + self.email + ', ' + self.telephone + ', '
        if(self.website != None):
            string += self.website + ', '
        else:
            string += 'None, '
        string += self.representative + ')'
        print(string)

class Binder:
    """
    This class is used to deal with Binder. Its attributes are the same
    used in the Binder table. Look it up in the documentation
    if needed.
    """
    def __init__(self, code, branch, typ):
        self.code = code
        self.branch = branch
        self.type = typ
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Binder( ' + self.code + ', ' + self.branch + ', ' + self.type + ')'
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'The Binder has code: ' + self.code + ' signed in branch ' + self.branch + ' and it is of type ' + self.type
        print(string)

class PrivateBinder:
    """
    This class is used to deal with PrivateBinder. Its attributes are the same
    used in the PrivateBinder table. Look it up in the documentation
    if needed.
    """
    def __init__(self, binder, ssn):
        """
        Class contructor method for PrivateBinder. It takes as input
        the fields from the table Private and it stores them into
        an object in order to deal with it.
        """
        self.binder = binder
        self.ssn = ssn
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'PrivateBinder( ' + self.binder + ', ' + self.ssn + ')'
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'This is a binder code '+ self.binder + ' for a private ' + self.ssn
        print(string)

class CompanyBinder:
    """
    This class is used to deal with CompanyBinder. Its attributes are the same
    used in the CompanyBinder table. Look it up in the documentation
    if needed.
    """
    def __init__(self, binder, taxCode):
        """
        Class contructor method for CompanyBinder. It takes as input
        the fields from the table CompanyBinder and it stores them into
        an object in order to deal with it.
        """
        self.binder = binder
        self.taxCode = taxCode
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'PrivateBinder( ' + self.binder + ', ' + self.taxCode + ')'
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'This is a binder code '+ self.binder + ' for a private ' + self.taxCode
        print(string)

class Contract:
    """
    This class is used to deal with Contract. Its attributes are the same
    used in the Company table. Look it up in the documentation
    if needed.
    """
    def __init__(self, code, binder, typ):
        """
        Class contructor method for Contract. It takes as input
        the fields from the table Contract and it stores them into
        an object in order to deal with it.
        """
        self.code = code
        self.binder = binder
        self.type = typ
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Contract( ' + self.code + ', ' + self.binder + ', ' + self.type + ')'
        print(string)
    
    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'Contract number ' + self.code + ' signed by binder ' + self.binder + ' is for a ' + self.type
        print(string)

class Account:
    """
    This class is used to deal with Account. Its attributes are the same
    used in the Account table. Look it up in the documentation
    if needed.
    """
    def __init__(self, iban, contract, interest, openingDate, balance, typ):
        """
        Class contructor method for Account. It takes as input
        the fields from the table Account and it stores them into
        an object in order to deal with it.
        """
        self.iban = iban
        self.contract = contract
        self.interest = interest
        self.openingDate = openingDate
        self.balance = balance
        self.type = typ

    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Account( ' + self.iban + ', ' + self.contract + ', ' + self.interest + ', ' + self.openingDate + ', ' + self.balance + ', ' + self.type + ')'
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'This ' + self.type + ' account has iban ' + self.iban + ' with contract ' + self.contract + '. Its interest is ' + self.interest + '. The account was opened on ' + self.openingDate + '. The balance is ' + self.balance
        print(string)

    def addToDatabase(self, mydb): #this method works!
    	mycursor = mydb.cursor()

    	sql = "INSERT INTO Account (IBAN, contract, Interest, OpeningDate, Balance, Type) VALUES (%s, %s, %s, %s, %s, %s)"
    	val = [(str(self.iban), str(self.contract), str(self.interest), str(self.openingDate), str(self.balance), str(self.type))]
    	mycursor.executemany(sql, val)
    	mydb.commit()

class Card:
    """
    This class is used to deal with Account. Its attributes are the same
    used in the Account table. Look it up in the documentation
    if needed.
    """
    def __init__(self, code, expiryDate, emissionDate, price, contract, typ):
        """
        Class contructor method for Card. It takes as input
        the fields from the table Card and it stores them into
        an object in order to deal with it.
        """
        self.code = code
        self.expiryDate = expiryDate
        self.emissionDate = emissionDate
        self.price = price
        self.contract = contract
        self.type = typ
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Card( ' + self.code + ', ' + self.expiryDate + ', ' + self.emissionDate + ', ' + self.price + ', ' + self.contract + ', ' + self.type + ')'
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        string = 'The ' + self.type + ' card ' + self.code + 'contract ' + self.contract + 'was emitted on ' + self.emissionDate + 'and expires on' + self.expiryDate + '. It costs ' + self.price 
        print(string)

class RecordPayment:
    """
    This class is used to deal with RecordPayment. Its attributes are the same
    used in the RecordPayment table. Look it up in the documentation
    if needed.
    """
    def __init__(self, senderSSN, senderTaxCode, senderBinder, receiverSSN, receiverTaxCode, receiverBinder, paymentType, date, commission):
        """
        Class contructor method for RecordPayment. It takes as input
        the fields from the table RecordPayment and it stores them into
        an object in order to deal with it.
        """
        self.senderSSN = senderSSN
        self.senderTaxCode = senderTaxCode
        self.senderBinder = senderBinder
        self.receiverSSN = receiverSSN
        self.receiverTaxCode = receiverTaxCode
        self.receiverBinder = receiverBinder
        self.paymentType = paymentType
        self.date = date
    
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'RecorPayment( ' + self.senderSSN + ', ' + self.senderTaxCode + ', ' + self.senderBinder + ', ' + self.receiverSSN + ', ' + self.receiverTaxCode + ', ' + self.receiverBinder + ', ' + self.paymentType + ', ' + self.date
        print(string)

    def __str__(self):
        """
        Special method used to print all of the attributes of the current object
        """
        #need to find a better idea for the string format, but I am pretty sure that in this case
        #the repr format is good enough since in this case it is just a payment record
        string = 'RecorPayment( ' + self.senderSSN + ', ' + self.senderTaxCode + ', ' + self.senderBinder + ', ' + self.receiverSSN + ', ' + self.receiverTaxCode + ', ' + self.receiverBinder + ', ' + self.paymentType + ', ' + self.date
        print(string)

def wireTransfer(senderAccount, receiverAccount, commission, amount, database):
    """
    This function takes two accounts and allows us
    to transfer money from one account to another one
    senderAccount and receiverAccount are two accounts as defined above
    amount is the amount that needs to be transfered from
    senderAccount towards receiverAccount
    commission is a floating point number that represents
    the commission the bank takes to realize a wire transfer
    It returns a RecordPayment instance if it works, otherwise
    it returns None.
    """
    if(senderAccount.balance >= (amount + commission)):
        sql = """
            SELECT Binder FROM Contract
            WHERE Contract = (SELECT Contract FROM Account
                                WHERE Contract = """
        sql += str(senderAccount.contract) + ");"
        cursor = database.cursor()
        cursor.execute(sql)

        print(sql)


    else:
        return None


acc1 = Account("IT902429353143", 1, 1.2, '2000-08-12', 10000.2, 'checking') 
acc2 = Account("IT90444353143", 2, 1.2, '2000-08-12', 10000.2, 'checking')
acc3 = Account("IT90544353143", 3, 1.2, '2000-08-12', 10000.2, 'checking')
def createConnection():
	database = mysql.connector.connect(
	    host = 'proxy55.rt3.io',
	    user = 'pi',
	    passwd = 'password', port = '37162', database = 'bank'
	)
	return database
#acc1.addToDatabase(database)
#acc2.addToDatabase(database)
database = createConnection()
acc3.addToDatabase(database)
database.close()
print('yay')