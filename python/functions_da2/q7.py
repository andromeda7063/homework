global annualInterest
annualInterest = 0.06

def loan(p, lt):
    mI = annualInterest / 12
    r = lt*12

    monthly = (p * mI) / (1 - (1 + mI) ** (-r))

    return monthly

a = float(input())
b = float(input())

print("monthly installment is", "$%.2f"%loan(a,b))