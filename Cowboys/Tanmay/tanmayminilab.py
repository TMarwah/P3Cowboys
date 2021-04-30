
class Counters:
    def __init__(self, sentence):
        self._sentence = sentence

    def wordcount(self):
        input = str(self._sentence)
        input_split = input.split(' ') #turns sentence into list of words
        wordcount = len(input_split)
        return wordcount

    def lettercount(self):
        lettercount = 0
        input = str(self._sentence)
        input_split = input.split(' ')
        for word in input_split: #cycles through list of words
            lettercount = lettercount + len(word)
        return lettercount

    def bubblesort(self):
        input = str(self._sentence)
        input_split = input.split(' ')
        length = len(input_split)
        def sort(input_split):
            for term in range(length):
                for x in range(len(input_split)-1):
                    if len(input_split[x]) > len(input_split[x+1]):
                        input_split[x], input_split[x+1] = input_split[x+1],input_split[x]
        sort(input_split)
        return(input_split)



