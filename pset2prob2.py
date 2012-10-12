'''
This program calculates and prints out the minimum fixed monthly payment needed
to pay off the total credit card balance within 12 months. It starts by
checking whether a minimum amount of $10 is sufficient, and iterates over
and over by increasing the amount by $10 until the whole debt is payed.
'''

balance = 4227
annualInterestRate = 0.2

monthlyInterestRate = annualInterestRate/12
minMonthlyPayment = 10
newBalance = balance

while newBalance > 0: #Loop checks whether debt is still unpayed
 newBalance = balance
 for month in range (1,13): #Calculates yearly payment
    newBalance = (newBalance - minMonthlyPayment) * (1 + monthlyInterestRate)
 if newBalance > 0:
    minMonthlyPayment = minMonthlyPayment + 10 #Increase payment by $10

print ("Lowest payment: " + str(minMonthlyPayment))