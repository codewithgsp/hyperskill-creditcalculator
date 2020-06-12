import argparse
from math import ceil, log


# noinspection PyMethodMayBeStatic
class CreditCalculator:

    def __init__(self):
        self.type = None
        self.payment = 0
        self.principal = 0
        self.periods = 0
        self.interest = 0

    def read_arguments(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--type', type=str, required=True, help='Credit calculation type')
        parser.add_argument('--payment', type=float, default=0, required=False, help='Monthly payment')
        parser.add_argument('--principal', type=float, default=0, required=False, help='Principal amount')
        parser.add_argument('--periods', type=int, default=0, required=False, help='Number of months')
        parser.add_argument('--interest', type=float, default=0, required=False, help='Interest value')
        args = vars(parser.parse_args())
        # assign values
        self.type = args.get('type')
        self.principal = args.get('principal')
        self.periods = args.get('periods')
        self.interest = args.get('interest')
        self.payment = args.get('payment')
        # main method to calculate values
        self.credit_calculator(self.type, self.principal, self.periods, self.interest, self.payment)

    def credit_calculator(self, type_, principal, periods, interest, payment):
        if type_ == 'diff' and principal > 0 and periods > 0 and interest > 0 and payment == 0:
            self.calc_diff_payment(self.principal, self.periods, self.interest)
        elif type_ == 'annuity' and interest > 0 and principal > 0 and periods > 0 and payment == 0:
            self.calc_monthly_payment(principal, periods, interest)
        elif type_ == 'annuity' and interest > 0 and principal > 0 and periods == 0 and payment > 0:
            self.calc_count_periods(principal, payment, interest)
        elif type_ == 'annuity' and interest > 0 and principal == 0 and periods > 0 and payment > 0:
            self.calc_principal(payment, interest, periods)
        else:
            print('Incorrect parameters')

    def calc_nominal_interest(self, credit_interest):
        return credit_interest / (12 * 100)

    def calc_count_periods(self, principal, monthly_payment, credit_interest):
        nominal_interest = self.calc_nominal_interest(credit_interest)
        periods = ceil(log((monthly_payment / (monthly_payment - nominal_interest * principal)), 1 + nominal_interest))
        self.display_months(periods)
        self.display_overpayment(principal, monthly_payment * periods)

    def display_months(self, month_):
        year = month_ // 12
        month = month_ % 12
        if year == 0:
            print('You need {month} months to repay this credit!'.format(month=month))
        elif month == 0:
            print('You need {year} years to repay this credit!'.format(year=year))
        else:
            if year == 1 and month == 1:
                year_plural = ''
                month_plural = ''
            elif year == 1:
                year_plural = ''
                month_plural = 's'
            elif month == 1:
                year_plural = 's'
                month_plural = ''
            else:
                year_plural = 's'
                month_plural = 's'
            print('You need {year} year{month_plural} and {month} month{month_plural} to replay this credit!'
                  .format(year=year, month=month, month_plural=month_plural, year_plural=year_plural))

    def calc_principal(self, monthly_payment, credit_interest, period):
        nominal_interest = self.calc_nominal_interest(credit_interest)
        principal = (monthly_payment /
                     ((nominal_interest * pow(1 + nominal_interest, period)) / (pow(1 + nominal_interest, period) - 1)))
        self.display_principal(principal)
        self.display_overpayment(principal, monthly_payment * period)

    def calc_monthly_payment(self, principal, period, credit_interest):
        nominal_interest = self.calc_nominal_interest(credit_interest)
        monthly_payment = ceil(principal * ((nominal_interest * pow(1 + nominal_interest, period))
                                            / (pow(1 + nominal_interest, period) - 1)))
        self.display_monthly_payment(monthly_payment)
        self.display_overpayment(principal, monthly_payment * period)

    def display_monthly_payment(self, monthly_payment):
        print('Your annuity payment = {}!'.format(monthly_payment))

    def display_principal(self, principal):
        print('Your credit principal = {}!'.format(int(principal)))

    def display_overpayment(self, principal, paid_amount):
        print('Overpayment = {}'.format(ceil(paid_amount - principal)))

    def calc_diff_payment(self, principal, period, credit_interest):
        nominal_interest = self.calc_nominal_interest(credit_interest)
        total_paid_out = 0
        for m in range(1, period+1):
            monthly_paid_out = ceil((principal / period) +
                                    nominal_interest * (principal - ((principal * (m - 1)) / period)))
            print('Month {month_num}: paid out {monthly_amt}'.format(month_num=m, monthly_amt=monthly_paid_out))
            total_paid_out += monthly_paid_out
        self.display_overpayment(principal, total_paid_out)


credit_calc = CreditCalculator()
credit_calc.read_arguments()
