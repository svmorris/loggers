from log import log


def function1():
    log([1, 2, 3, 4])
    eval("print()")

def function2(test = "hey, hey"):
    function1()

def function3():
    function2()

def function4():
    function3()


function4()
