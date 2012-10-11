'''
This program calculates and prints out the minimum fixed monthly payment needed
to pay off the total credit card balance within 12 months.
'''

balance = 4772
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
minMonthlyPayment = 10
newBalance = balance

while newBalance > 0:
 newBalance = balance
 for month in range (1,13):
    newBalance = (newBalance - minMonthlyPayment) * (1 + monthlyInterestRate)
 if newBalance > 0:
    minMonthlyPayment = minMonthlyPayment + 10

print ("Lowest payment: " + str(minMonthlyPayment))