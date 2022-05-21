def whileTest(loop = None):
    if(loop == 0):
        exit()

    print('test')
    whileTest(loop = loop - 1)

whileTest(5)