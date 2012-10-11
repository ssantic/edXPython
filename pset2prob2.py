'''
This program calculates and prints out the minimum fixed monthly payment needed
to pay off the total credit card balance within 12 months.
'''

balance = 3329
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
minMonthlyPayment = 10

while balance > 0:
 minMonthlyPayment = minMonthlyPayment + 10
 for month in range (1,13):
    balance = (balance - minMonthlyPayment) * (1 + monthlyInterestRate)











print ("Lowest payment: " + str(minMonthlyPayment))