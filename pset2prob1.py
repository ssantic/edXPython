'''
Problem set 2, Problem 1: Paying the Minimum

A program that calculates the credit card balance after one year if a person
pays the minimum monthly payment required by the credit card company each
month.
'''
balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04

monthlyInterestRate = monthlyPaymentRate/12 #Monthly interest rate
minMonthlyPayment = monthlyPaymentRate * balance #Minimum monthly payment
newBalance = (balance - minMonthlyPayment) * (1 + monthlyInterestrate)

