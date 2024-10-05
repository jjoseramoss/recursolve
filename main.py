import numpy as np
# Solves linear recurrence relations
    # Ex: a(n) = c1 * a(n-1) + c2

class linear_recurrence:
    # Constructor
    def __init__(self, c1, c2, base):
        self.c1 = c1
        self.c2 = c2
        self.base = base

    #Method to display the recurrence relation
    def display_linear_recurrence(self):
        print(f"The linear recurrence relation is: a(n) = {self.c1} * a(n-1) + {self.c2} with a base case of: a(1) = {self.base}")

    def solve_recurrence(self, n):
        #Start from base case and displays sequence up to n:
        sequence = np.empty(n)
        for i in range( n):
            # inputs base case into sequence
            if(i == 0):
                sequence[i] = self.base
                continue

            ans = self.c1 * sequence[i-1] + self.c2
            sequence[i] = ans

        # prints sequence
        print("The sequence is: " , end='')
        print("{", end='')
        for i in range(n):
            print(f"{sequence[i]}," , end=' ')
        print("}")
            
print("Welcome to Recursolve!")
print("Please choose the type of recursive relation problem do you have?")
type = int(input("1-linear, 2- , 3- ,: "))

if(type == 1):
    print("a(n) = c1 * a(n-1) + c2)")
    const1 = int(input("What is your first constant: "))
    const2 = int(input("What is your second constant: "))
    base_case = int(input("What is your base case: "))
    
    eq1 = linear_recurrence(const1, const2, base_case)
    eq1.display_linear_recurrence()

    length = int(input("How long would you like the sequence to be?: "))
    eq1.solve_recurrence(length)
