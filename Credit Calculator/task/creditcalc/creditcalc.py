from math import ceil, log


def calc_nominal_interest(ci):
    return ci / (12 * 100)


def calc_count_periods(p, mp, int_):
    """
    :param p: principal
    :param mp: monthly payment
    :param int_: nominal interest
    :return: number of months in int
    """
    return log((mp / (mp - int_ * p)), 1 + int_)


def display_months(month):
    month = ceil(month)
    if month // 12 == 0:
        print('You need {month} months to repay this credit!'.format(month=month))
    else:
        year = month // 12
        month = month % 12
        if year == 1 and month == 1:
            print('You need {year} year and {month} month to replay this credit!'.format(year=year,
                                                                                         month=month))
        elif year == 1:
            print('You need {year} year and {month} months to replay this credit!'.format(year=year,
                                                                                          month=month))
        elif month == 1:
            print('You need {year} year and {month} month to replay this credit!'.format(year=year,
                                                                                         month=month))
        else:
            print('You need {year} years and {month} months to replay this credit!'.format(year=year,
                                                                                           month=month))


def calc_principal(mp, int_, n):
    return mp / ((int_ * pow(1 + int_, n)) / (pow(1 + int_, n) - 1))


def calc_monthly_payment(p, n, int_):
    return p * ((int_ * pow(1 + int_, n)) / (pow(1 + int_, n) - 1))


def display_monthly_payment(mp):
    print('Your annuity payment = {}!'.format(ceil(mp)))


def display_principal(p):
    print('Your credit principal = {}!'.format(int(p)))


option = input('''
What do you want to calculate?
type "n" - for count of months,
type "a" - for annuity monthly payment,
type "p" - for credit principal:
''')
if option == 'n':
    principal = float(input('Enter credit principal:\n'))
    monthly_payment = float(input('Enter monthly payment:\n'))
    credit_interest = float(input('Enter credit interest:\n'))
    i = calc_nominal_interest(credit_interest)
    months = calc_count_periods(p=principal, mp=monthly_payment, int_=i)
    display_months(months)
elif option == 'p':
    monthly_payment = float(input('Enter monthly payment:\n'))
    count_periods = float(input('Enter count of periods:\n'))
    credit_interest = float(input('Enter credit interest:\n'))
    i = calc_nominal_interest(credit_interest)
    principal = calc_principal(monthly_payment, i, count_periods)
    display_principal(principal)
elif option == 'a':
    principal = float(input('Enter credit principal:\n'))
    count_periods = float(input('Enter count of periods:\n'))
    credit_interest = float(input('Enter credit interest:\n'))
    i = calc_nominal_interest(credit_interest)
    monthly_payment = calc_monthly_payment(principal, count_periods, i)
    display_monthly_payment(monthly_payment)
