"""
This module contains all the classes and helper functions
needed in order to correctly manage a banking system.
I am probably also going to put here all the functions
that are more specific to this banking system,
that is, the functions to make money transfers,
open accounts and everything else.
"""

class Area:
    """
    This class is used to deal with Area. Its attributes are the ones
    used in the Area table. Look it up in the documentatoin
    if needed
    """
    def __init__(self, code, address)

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
        an object in order to deal with it. s
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
        Special method used to print all of the attribute of the current object
        """
        string = 'This Branch has code ' + str(self.code) + ', area: ' + str(self.area) + ', located at ' + self.address + ' ' + self.city + '. It is a ' + self.type + 'branch. Contacts: ' + self.email + ' ' + self.pec + ' ' + str(self.telephone)
        print(string)
    def __repr__(self):
        """
        Special method to have a quick way to print a log of the current state of the object
        """
        string = 'Branch(' + str(self.code) + ', ' + str(self.area) + ', ' + self.address + ', ' + self.city + ', ' + self.type + ', ' + self.email + ', ' + self.pec + ', ' +str(self.telephone) + ')'
        print(string)

