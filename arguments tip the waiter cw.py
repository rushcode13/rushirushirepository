def total_calc(bill_amount,tip_percentage):
    total=bill_amount*(1+(1/100)*tip_percentage)
    total=round(total,2)
    print(f"please pay${total}")
total_calc(150,20)
