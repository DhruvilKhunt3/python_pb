calculated_gross_pay = 0
def cal_gross_pay(basic_pay,other_allowances,hra):
    global calculated_gross_pay
    calculated_gross_pay+=basic_pay+(hra*basic_pay)+(0.5*basic_pay)+other_allowances+900-200-(0.11*basic_pay)
    return calculated_gross_pay
basic_pay,other_allowances,gross_pay,hra,annual_pay,incometax = 0,0,0,0,0,0
grade = input('Enter the grade_level (A,B,C,D,E or F:) ')
print('city 1 is a tier 1 (metro), city 2 is tier 2 and city 3 is tier 3')
city = input('Enter the city (1,2 or 3) -> ')
if(grade=='a'):
    basic_pay=60000
    other_allowances=8000
elif(grade=='b'):
    basic_pay=50000
    other_allowances=7000
elif(grade=='c'):
    basic_pay=40000
    other_allowances=6000
elif(grade=='d'):
    basic_pay=30000
    other_allowances=5000
elif(grade=='e'):
    basic_pay=20000
    other_allowances=4000
elif(grade=='f'):
    basic_pay=10000
    other_allowances=3000
if(city==1):
    hra=0.3
elif(city==2):
    hra=0.2
elif(city==3):
    hra=0.1
gross_pay= cal_gross_pay(basic_pay,other_allowances,hra)
annual_pay=gross_pay*12

if(annual_pay < 250000):
    incometax = 0
    
elif(annual_pay >= 250000 and annual_pay < 500000):
    taxable_amount = annual_pay - 250000
    tax_before_cess = taxable_amount * 0.05
    if annual_pay <= 500000:
        incometax = 0 # Due to Section 87A Rebate
    else:
        incometax = tax_before_cess # If you were not applying the full rebate
        
elif(annual_pay >= 500000 and annual_pay < 1000000):
    tax_on_first_5lakh = 12500  # 5% of (500000 - 250000)
    taxable_amount = annual_pay - 500000
    tax_on_balance = taxable_amount * 0.20
    
    tax_before_cess = tax_on_first_5lakh + tax_on_balance
    incometax = tax_before_cess * 1.04 # Add 4% Health & Education Cess
    
elif(annual_pay >= 1000000):
    tax_on_first_10lakh = 12500 + (500000 * 0.20) # ₹12,500 + ₹1,00,000 = ₹1,12,500
    taxable_amount = annual_pay - 1000000
    tax_on_balance = taxable_amount * 0.30
    
    tax_before_cess = tax_on_first_10lakh + tax_on_balance
    incometax = tax_before_cess * 1.04 # Add 4% Health & Education Cess

monthly_tax = incometax / 12
net_annual_pay = annual_pay - incometax

print("\n--- Pay Calculation Summary ---")
print("Annual Gross Pay: ₹ ",annual_pay)
print("Annual Income Tax: ₹ ",incometax)
print("Monthly Tax Deduction: ₹ ",monthly_tax)
print("Annual Net Pay (After Tax): ₹ ",net_annual_pay)