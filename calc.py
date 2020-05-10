"""calc v1.0"""
def input_number():
    num=input("Vvedite chislo: ")
    if num == '':
        return None
    try:
         num=float(num)
    except ValueError:
        num = num
    return num

def input_oper():
    oper=input("Operaciya('+','-','*','/','^','**'): ")
    return oper

def calc_me(x,y,oper):
    if x is None:
        return "ERROR: send me Number1"
    if y is None:
        return "ERROR: send me Number2"
    if (not isinstance(x, (int, float))) or (not isinstance(y, (int, float))):
        return "ERROR: now it is does not supported"


    if oper=='*':
        return x*y
    elif oper=='/':
        if y==0:
            return "ERROR: Divide by zero!"
        else:
            return x/y
    elif oper=='+':
        return x+y
    elif oper=='-':
        return x-y
    elif oper == '^' or oper == '**':
        return x ** y
    else:
        return("Wrong operatiopn")

def body():
    num1 = input_number()
    oper = input_oper()
    num2 = input_number()

    result = calc_me(num1,num2,oper)
    print(result)


if __name__=='__main__':
    body()
