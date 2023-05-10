import os
import random

os.rmdir('your mailbox')
os.mkdir('your mailbox')
os.chdir('your mailbox')
num = 0

for i in range(random.randint(30, 50)):
    num = num +1
    pipename = 'pipebomb' + str(num) + '.txt'
    pipe = open(pipename, 'w+')
    pipe.write('this is a pipebomb')
    pipe.close()