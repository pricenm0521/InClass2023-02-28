# vehicleclass.py

'''
Vehicle Class
'''

class Vehicle:
    '''
    this initializes the object when it is instantiated
    also referred to as a constructor or the constructor method
    '''
    def __init__(self, type):
        self.type = type;

    def printType(self):
        print(self.type);
        
# this code only runs if this module is the entry point
if __name__ == "__main__":
    # Some code to test the class would go here.
    # If there's no code, just pass
    # pass  placeholder, basically means skip
    # this could be the test code for this module
    # only want the test code to run under controlled circumstances
    print("I am in VehicleClass.py") # if vehicle class is your entry point this line of code will run, if you are in another entry point it will not run
    