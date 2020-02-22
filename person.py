# File person.py
"""
Record and process information about people.
Run this file directly to test its classes.
"""
from classtools import AttrDisplay                          # Use generic display tool

class Person(AttrDisplay): # Start a class. Mix in a repr at this level
    # Add record field initialization with defaults for constructor arguments
    """
    Create and process person records
    """
    def __init__(self, name, job=None, pay=0):              # Constructor takes three arguments
        self.name = name                                    # Fill out fields when created
        self.job  = job                                     # self is the new instance object
        self.pay  = pay
    def lastName(self):                                     # Behavior methods
        return self.name.split()[-1]                        # self is implied subject
    #@rangetest(percent=(0.0, 1.0))                         # Use decorator to validate
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))            # Must change here only
    #def __repr__(self):                                     # Added method
        #return '[Person: %s, %s]' % (self.name, self.pay)   # String to print

class Manager(Person):                                      # Define a subclass of Person. Inherit Person attrs.
    """
    A customized Person with special requirements
    """
    def __init__(self, name, pay):                          # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)             # Run original with 'mgr'
    def giveRaise(self, percent, bonus=.10):                # Redefine to customize at this level
        Person.giveRaise(self, percent + bonus)             # Call Person's version

if __name__ == '__main__':                          # When run for testing only
    # Add incremental self-test code
    bob = Person('Bob Smith')                           # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000)    # Runs __init__ automatically
    print(bob)                                          # Fetch attached attributes
    print(sue)                                          # sue's and bob's attrs differ
    print(bob.lastName(), sue.lastName())               # Use the new methods
    sue.giveRaise(.10)                                  # instead of hardcoding
    print(sue)
    tom = Manager('Tom Jones', 50000)                   # Make a Manager: __init__. Job name not needed.
    tom.giveRaise(.10)                                  # Runs custom version
    print(tom.lastName())                               # Runs inherited method
    print(tom)                                          # Runs inherited __repr__

