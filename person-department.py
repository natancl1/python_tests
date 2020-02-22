# File person-department.py

class Person: # Start a class
    # Add record field initialization with defaults for constructor arguments
    def __init__(self, name, job=None, pay=0):              # Constructor takes three arguments
        self.name = name                                    # Fill out fields when created
        self.job  = job                                     # self is the new instance object
        self.pay  = pay
    def lastName(self):                                     # Behavior methods
        return self.name.split()[-1]                        # self is implied subject
    #@rangetest(percent=(0.0, 1.0))                         # Use decorator to validate
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))            # Must change here only
    def __repr__(self):                                     # Added method
        return '[Person: %s, %s]' % (self.name, self.pay)   # String to print

class Manager(Person):                                      # Define a subclass of Person. Inherit Person attrs.
    def __init__(self, name, pay):                          # Redefine constructor
        Person.__init__(self, name, 'mgr', pay)             # Run original with 'mgr'
    def giveRaise(self, percent, bonus=.10):                # Redefine to customize at this level
        Person.giveRaise(self, percent + bonus)             # Call Person's version

class Department:
    def __init__(self, *args):
        self.members = list(args)
    def addMember(self, person):
        self.members.append(person)
    def giveRaises(self, percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)

if __name__ == '__main__':                          # When run for testing only
    # Add incremental self-test code
    bob = Person('Bob Smith')                           # Test the class
    sue = Person('Sue Jones', job='dev', pay=100000)    # Runs __init__ automatically
    tom = Manager('Tom Jones', 50000)                   # Make a Manager: __init__. Job name not needed.

    development = Department(bob, sue)                  # Embed objects in a composite
    development.addMember(tom)
    development.giveRaises(.10)                         # Runs embedded object's giveRaise
    development.showAll()                               # Runs embedded object's __repr__

