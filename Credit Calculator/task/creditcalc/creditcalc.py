from math import ceil

credit_principal = int(input('Enter the credit principal:\n'))
option = input("""
What do you want to calculate? 
type "m" - for count of months, 
type "p" - for monthly payment:
""")

if option == 'm':
    monthly_payment = int(input('Enter monthly payment:\n'))
    months_required = int(round(credit_principal/monthly_payment))
    if months_required == 1:
        print('It takes {} month to repay the credit'.format(months_required))
    else:
        print('It takes {} months to repay the credit'.format(months_required))
elif option == 'p':
    months_required = int(input('Enter count of months:\n'))
    monthly_payment = int(ceil(credit_principal / months_required))
    last_payment = int(credit_principal - (months_required - 1) * monthly_payment)
    if last_payment == monthly_payment:
        print('Your monthly payment = {}'.format(last_payment))
    else:
        print('Your monthly payment = {} with last month payment = {}'.format(monthly_payment,
                                                                              last_payment))
