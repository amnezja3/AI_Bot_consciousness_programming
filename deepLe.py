import multiWhile as mW

CUBES = 3

EYES = 6

shoot = []

for a in range( 1, EYES +1 ):
    shoot.append(a)

moves = mW.multiWhileIndexes(shoot, shoot, shoot)

for x in moves:
    for y in range(1):
    # for y in range( 1, EYES +1 ):
        print(str(int(x)))
        # print(str(moves[0+y]) + ' + ' + str(moves[1+y]) + ' + ' + str(y) + ' = ' +  str(int(x * CUBES)))