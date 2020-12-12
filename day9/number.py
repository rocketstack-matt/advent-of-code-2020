from typing import Tuple


class ValidNumber:
    
    def __init__(self, number, previous_numbers):
        super().__init__()
        
        self.number = number
        self.previous_numbers = previous_numbers

    def is_valid(self):
        for n1 in self.previous_numbers:
            n2_array = self.previous_numbers.copy()
            n2_array.remove(n1)
            for n2 in n2_array:
                if n1 + n2 == self.number:
                    return True
        return False

