# return max value from array
def find_max(inputList):
    maxValue = float(inputList[0])
    for i in inputList:
        if float(i) > float(maxValue):
            maxValue = i
    return str(maxValue)


# load all lines one by one from file
def load_data():
    try:
        outputFile = open('../1_1/output.txt', 'w+')
        with open('../1_1/input.txt', 'r') as input_file:
            for line in input_file:
                append_to_file(outputFile, find_max(line.strip().split(";")))
        outputFile.close()
        print("Done!")
    except FileNotFoundError:
        print("from_rpn.txt not found")


# append value to file
def append_to_file(outputFile, outputValue):
    outputFile.writelines(outputValue + '\n')


load_data()
