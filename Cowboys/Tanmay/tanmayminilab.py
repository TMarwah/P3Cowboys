
class Counters:
    def __init__(self, sentence):
        self._sentence = sentence

    def wordcount(self):
        i = 0
        input = self._sentence
        input_split = input.split(' ')
        for word in input_split:
            i += 1

        return i

    def lettercount(self):
        i = 0
        input = self._sentence
        input_split = input.split(' ')
        for word in input_split:
            i = i + len(word)
        return i
