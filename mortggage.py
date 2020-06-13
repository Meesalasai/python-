# mortgage.py

principal = 5000
rate = 0.01
payment =1000
total_paid = 1000
month = 0

extra_payment = 100
extra_payment_start_month =1
extra_payment_end_month = 6

while principal > 0:
    month = month + 1
    principal = principal * (1 + rate / 12) - payment
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
        principal = principal - extra_payment
        total_paid = total_paid + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print('Total paid', round(total_paid, 2))
print('Months', month)

