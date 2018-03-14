class JugException(Exception):
     def __init__(self, message="\'Jug\': The amount to be stored cannot exceed the size of the jug"):
        # Call the base class constructor with the parameters it needs
        super(JugException, self).__init__(message)
       
class Jug:
    """This class represents the object Jug and its functions as a container"""
    def __init__(self,size,amount=0):
        self.size = size
        if amount <= size:
            self.amount = amount
        else:
            raise JugException

    def empty(self):
        """This function empties the content of the current jug"""
        self.amount = 0

    def is_empty(self):
        return self.amount == 0

    def is_full(self):
        return self.amount == self.size
    
    def pour(self,another_jug):
        """This function pours the content of this jug into 'another_jug'"""
        if self.amount <= another_jug.size - another_jug.amount:
            another_jug.amount = another_jug.amount + self.amount
            self.empty()
        else:
            moved = another_jug.size - another_jug.amount
            self.amount = self.amount - moved
            another_jug.amount = another_jug.amount + moved

    def __str__(self):
        return str(self.amount)

def pump(jug):
    """This function fills the jug provided to the brim"""
    jug.amount = jug.size
    
 
def remain_amount(f_jug,s_jug,amount=2):
    if amount <= f_jug.size:
        if f_jug.amount == amount: # base case
            return(f_jug)
        else:
            print(str(f_jug) + " "+ str(s_jug))
            pump(f_jug)
            print(str(f_jug) + " "+ str(s_jug))
            f_jug.pour(s_jug)
            print(str(f_jug) + " "+ str(s_jug))
            s_jug.empty()
            if f_jug.amount != amount:
                f_jug.pour(s_jug)
                f_jug = remain_amount(f_jug,s_jug,amount)
            return f_jug
    else:
        raise JugException

first_jug = Jug(7)
second_jug = Jug(4)

first_jug = remain_amount(first_jug,second_jug,amount=2)
print(first_jug)



    
