
#employee enters annual salary
salary = input("Enter annual salary: ")
hours = input("Enter number of weekly hours that you are expected to work: ")

try:
    salary_amount = float(salary)
    hours_per_week = float(hours)
except:
    print("Error. Please enter a numeric value without any special characters.")
    quit()

yearly_hours = (hours_per_week * 52)

#rounded dollar amounts to 2 decimal places
rounded_hourly_rate = round((salary_amount/yearly_hours), 2)
rounded_monthly_pay = round(((hours_per_week * rounded_hourly_rate) * 4), 2)

#formatted each amount to ensure it always has 2 decimal places and does not omit any ending zeros
formatted_hourly_rate = "{:.2f}".format(rounded_hourly_rate)
formatted_monthly_pay = "{:.2f}".format(rounded_monthly_pay)

print (f"""
    Approximate hourly rate: ${formatted_hourly_rate}
    Approximate monthly pay: ${formatted_monthly_pay}
    """)

input()

