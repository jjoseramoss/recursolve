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
            
                


eq1 = linear_recurrence(2, 3, 2)
eq1.display_linear_recurrence()
eq1.solve_recurrence(5)
