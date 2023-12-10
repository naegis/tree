
class Palindrome:
    def __init__ (self, max_size):
        self.stack = []
        self.top = -1
        self.max_size = max_size
       
    def is_full(self):
        return self.top == self.max_size - 1
   
    def is_empty(self):
        return self.top == -1
   
    def push(self, data):
        if not self.is_full():
            self.top += 1
            self.stack.append(data)
            return data
        else:
            #stack is full or overflow
            return "Stack overflow"
       
    
    def display_elements(self):
        if self.is_empty():
            return "Stack Underflow"
        else:
            result = "This is your word: "
            for i in range(self.top + 1):
                result += self.stack[i]
            return result
    
    def pop(self):
        if not self.is_empty():
            popped_element = self.stack[self.top]
            self.top -= 1
            return popped_element
        else:
            return "Stack Underflow"
        
    
#Function to check if character is special           
def is_special(char):
    special_characters = " !@#$%^&*9)_+|:;<>?,./?"
    return char in special_characters

#Function to check if character is alphanumeric
def is_alphanumeric(char):
    alphnumeric = "QQWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"
    return char in alphnumeric

#Function to check if character is a palindrome
def is_palindrome(self):
    palindrome = palindrome1.lower()
    length = len(palindrome)
    stack = Palindrome(length)
    p_array = []

    for each in palindrome:
        if not is_special(each) & is_alphanumeric(each):
            p_array.append(each)

    array1 = []
    for each in p_array:
        pushed = stack.push(each)
        array1.append(pushed)
    
    
    print(stack.display_elements())  

    print("This is your reversed word: ", end='')
    
    array2 = []
    while not stack.is_empty():
        popped = stack.pop()
        array2.append(popped)
        print(popped, end='')

    for each in array1:    
        for every in array2:
            if each == every:
                equal = True
            else:
                equal = False

    print()
    print()

    if equal == True:
        print("Your word is a palindrome.")
    else:
        print("Your word is not a palindrome.")

    print()

palindrome1 = input("Please enter your palindrome word: ")
is_palindrome(palindrome1)