
class CreateTask:
    def __init__(self, sentence, algorithm_type):
        self._sentence = sentence
        self._algorithm_type = algorithm_type

    @property
    def testproc(self):

        if self._algorithm_type == "sort":
            def bubblesort(input):
                input_split = input.split(' ')
                length = len(input_split)
                for x in range(length-1):
                    for y in range(length-x-1):
                        if int(input_split[x]) > int(input_split[x+y+1]):
                            temp = input_split[x]
                            input_split[x] = input_split[y+x+1]
                            input_split[y+x+1] = temp
                return (input_split)
            return (bubblesort(str(self._sentence)))

        if self._algorithm_type == "average":
            def average(input):
                totalvalue = 0
                input_split = input.split(' ')
                length = len(input_split)
                for x in range(length):
                    totalvalue = totalvalue + int(input_split[x])
                totalvalue = totalvalue/length
                return(int(totalvalue))
            return (average(str(self._sentence)))












