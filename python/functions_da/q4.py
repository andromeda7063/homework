def bank(init):
    bal = init

    def transaction(oper, amt):
        nonlocal bal

        if oper == "wd":
            if amt > bal:
                return "insufficient funds"

            elif amt < 0:
                return "invallid amount"
            
            else:
                bal -= amt
                return f"withdrew: {amt:.2f}. current balance: {bal:.2f}."

            
        elif oper == "dp":
            if amt < 0:
                return "invalid amount"

            else:
                bal += amt
                return f"deposited: {amt:.2f}. current balance: {bal:.2f}."


        elif oper == "vb":
            bal += amt
            return f"current balance: {bal:.2f}."

        elif oper == "ls":
            return " wd: withdraw\n dp: deposit\n vb: view balance\n ls: list all actions\n exit: exit bank"
        
    
    return transaction



def main():
    a = float(input("enter starting balance: "))
    acc = bank(a)

    while True:
        oper = input("user@bank /#: ").strip().lower()

        if oper in ['exit', 'e']:
            break

        elif oper in ['dp', 'wd']:
            try:
                amt = float(input("enter amount: " ))
                result = acc(oper, amt)

                print(result)

            except ValueError:
                print("invalid transcaction")

        elif oper in ['ls', 'vb']:
            try:
                result = acc(oper, 0)

                print(result)

            except ValueError:
                print("invalid operation")

        else:
            print("invalid operation, enter ls for list")

if __name__ == "__main__":
    main()