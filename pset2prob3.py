'''
This program calculates the fixed minimum monthly payment needed to pay off
the complete credit card balance within one year. It uses the bisection search
(also known as biserial search) algorithm, and then prints out the value.
'''

balance = 999999
annualInterestRate = 0.18

monthlyInterestRate = annualInterestRate/12
lowerBound = balance/12 #Lower bound for bisection search
upperBound = (balance * (1 + monthlyInterestRate)**12)/12 #Upper bound
minMonthlyPayment = (lowerBound + upperBound)/2.0 #Startin minimum payment
newBalance = balance

while abs(newBalance) > 0.01:
 newBalance = balance
 for month in range (1,13):
   newBalance = (newBalance - minMonthlyPayment) * (1 + monthlyInterestRate)
 if newBalance <= 0: #This loop is charachteristic for bisection search
    upperBound = minMonthlyPayment
 else:
    lowerBound = minMonthlyPayment
 minMonthlyPayment = (lowerBound + upperBound)/2.0


print ("Lowest payment: " + str(round(minMonthlyPayment,2)))