"""Topic: Custom Classes in Python

Description: You are tasked with creating a Rectangle class with the following requirements:

An instance of the Rectangle class requires length:int and width:int to be initialized.
We can iterate over an instance of the Rectangle class 
When an instance of the Rectangle class is iterated over, we first get its length in the format: {'length': <VALUE_OF_LENGTH>} 
followed by the width {width: <VALUE_OF_WIDTH>}

"""

class Rectangle:
    '''Class of rectangle on whose instance you can iterate over '''
    #defining constructor
    def __init__(self,length,width):
        self.length=length
        self.width=width
    #defining magic method str for string representation of the instance/oject
    def __str__(self):
        return  f'Rectangle with length {self.length} and width {self.width}'
    
    #defining __iter__ to make the object iterable and using the yield keyword instead of return to make it ehave like generator.
    def __iter__(self):
        yield {'length':self.length}
        yield {'width':self.width}

    def __del__(self):
        print(f'{self} deleted')    
    


obj1= Rectangle(5,7)
print(obj1)
for i in obj1:
    print(i)
       
    