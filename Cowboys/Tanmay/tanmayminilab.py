
class Counters:
    def __init__(self, sentence):
        self._sentence = sentence

    def wordcount(self):
        input = str(self._sentence)
        input_split = input.split(' ')
        wordcount = len(input_split)
        return wordcount

    def lettercount(self):
        lettercount = 0
        input = str(self._sentence)
        input_split = input.split(' ')
        for word in input_split:
            lettercount = lettercount + len(word)
        return lettercount
