
#employee enters total weekly hours worked & rate of pay
total_hours = input("Enter total hours: ")
hourly_rate = input("Enter hourly rate: ")
try:
    hours = float(total_hours)
    rate = float(hourly_rate)
except:
    print("Error. Please enter a numeric value.")
    quit()

#Calculates pay without overtime
if hours <= 40.0:
    total_pay = (hours * rate)
    print (f"""
        Regular pay: ${total_pay},
        Overtime pay: N/A,
        Total pay: ${total_pay}
        """)
    
#calculates pay including overtime
elif hours > 40.0:
    overtime = float((hours % 40.0) * (rate * 1.5))
    reg_pay= (40.0 * rate)
    total_pay = reg_pay + overtime
    print (f"""
        Regular pay: ${reg_pay},
        Overtime pay: ${overtime},
        Total pay: ${total_pay}
        """)
    
#calculates bi-weekly, monthly, and annual income
biweekly_pay = (total_pay * 2)
monthly_pay = (total_pay * 4)
annual_income = (monthly_pay * 12)

print (f"""
    Bi-weekly pay: ${biweekly_pay}, 
    Monthly pay: ${monthly_pay}, 
    Annual Income: ${annual_income}
    """)
input()

