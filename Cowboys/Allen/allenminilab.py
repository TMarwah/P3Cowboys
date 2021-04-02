

class Prime:

    def __init__(self, number):
        self._number = number

    def solution(self):
        n = self._number
        prime_nums = []

        for num in range(n):
            if num > 1: # prime numbers > 1
                for i in range(2, num):
                    if (num % i) == 0: # if the this yields 0, it means that the number can be divided cleanly by a number preceding it
                        break
                else:
                    prime_nums.append(num) # adds prime number to the list
        if (len(prime_nums) == 0):
            return "No prime numbers"
        else:
            return prime_nums

