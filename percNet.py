def perceptronCalc(x_input, w_weights):
    weighted_sum = 0
    for x,w in zip(x_input, w_weights):
        weighted_sum += x * w
        # print(weighted_sum)
    return weighted_sum

def getMemeory(file):
    f = open(f'./memories/{file}', 'r', encoding = 'utf-8')
    m = f.readline()
    f.close()
    splitMemory = m.strip().split(';')
    exp = [
            [ float(splitMemory[a]) for a in range(len(splitMemory) - 1)], float(splitMemory[len(splitMemory) - 1])
        ]
    return exp

def saveMemory(file, m = [[None], None]):
    f = open(f'./memories/{file}', 'w+', encoding = 'utf-8')
    stringMemory = ''
    stringBias = str(m[1])
    for i in m[0]:
        i = str(i)
        stringMemory += i + ';'
    exp = stringMemory + stringBias
    f.write(exp)
    f.close()
   