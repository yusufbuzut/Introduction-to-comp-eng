# Your solution for part c



montly_salary= float(input("Enter your monthly salary:"))
percentage_saved= float(input("Enter the percentage to save, as a decimal:"))
total_cost= float(input("Enter the cost of the dream car:"))
percentage_increase= float(input("Enter the increase in the car's price, as a decimal:"))
interest_rate= 0.01

percentage_salary_increase= float(input("Enter the percentage salary raise, as a decimal:"))
n=0
current_savings= montly_salary*percentage_saved*((pow(1+interest_rate,n)-1)/interest_rate)


while total_cost> current_savings:
  if n % 12 == 0:
    total_cost= total_cost*(1+percentage_increase)
  current_savings = current_savings+montly_salary*percentage_saved +(current_savings*interest_rate)
  if n % 6 == 0:
    montly_salary= montly_salary*(1+percentage_salary_increase)
  n= n+1
  
print("Number of months:",n)
