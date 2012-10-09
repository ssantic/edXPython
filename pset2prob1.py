'''
Problem set 2, Problem 1: Paying the Minimum

A program that calculates the credit card balance after one year if a person
pays the minimum monthly payment required by the credit card company each
month. It prints out payments and remaining balances for each month, as well as
the total paid amount, and the remaining balance at the end of the year.
'''

balance = 4213 #Starting debt balance
annualInterestRate = 0.2 #Yearly interest rate in decimals
monthlyPaymentRate = 0.04 #Monthly minimum payment rate in decimals


monthlyInterestRate = annualInterestRate/12 #Monthly interest rate

totalPaid = 0 #Sets the cumulation for total paid amount

for month in range (1,13): #Reports payments for 12 months
    minMonthlyPayment = monthlyPaymentRate * balance
    balance = (balance - minMonthlyPayment) * (1 + monthlyInterestRate)
    totalPaid = totalPaid + minMonthlyPayment
    print ("Month: " + str(month))
    print ("Minimum monthly payment: " + str(round(minMonthlyPayment,2)))
    print ("Remaining balance: " + str(round(balance,2)))
                           #End of for loop

print ("Total paid: " + str(round(totalPaid,2)))
print ("Remaining balance: " + str(round(balance,2)))