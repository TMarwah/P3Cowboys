

class Prime:

    def __init__(self, number):
        self._number = number

    """Algorithm for building Prime sequence, this id called from __init__"""
    @property
    def solution(self):
        n = self._number
        prime_nums = []

        for num in range(n+1):
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

class Vowel:

    def __init__(self, string):
        self._string = string
    @property
    def vowel_count(self):
        str = self._string
        count = 0
        vowel = set("aeiouAEIOU")

    # Loop to traverse the alphabet
    # in the given string
        for alphabet in str:

        # If alphabet is present
        # in set vowel
            if alphabet in vowel:
                count = count + 1

        return count









