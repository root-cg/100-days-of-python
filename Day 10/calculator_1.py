from art import logo

print(logo)

def addition(n1, n2):
    return n1 + n2


def substraction(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def division(n1, n2):
    return n1 / n2


calc_dict = {"+":  addition,
             "-":  substraction,
             "*":  multiply,
             "/":  division}

def calculator():
    should_continue = True

    num_1 = int(input("Whats the first number ? "))

    while (should_continue):
        num_2 = int(input("whats the next number ? "))
        
        for calc in calc_dict:
            print(calc)

        op_symbol = input("Pick an operation to perform: ")
        first_answer = calc_dict[op_symbol](num_1, num_2)
        print(f"{num_1} {op_symbol} {num_2} = {first_answer}")

        choice = input("type 'yes' to continue else type 'no' to start new Calculation.").lower()
        if choice == 'y':
            num_1 = first_answer
        else:
            should_continue = False
            calculator()


calculator()