# check weather the given input is a leap year or not
# n=int(input())
# if n>0:
#     if (n%4==0 and n%100!=0) or (n%400==0):
#         print("Leap Year.")
#     else:
#         print("Not a Leap Year.")

# calculates the total cost of running the heater for 5 hours. print the final cost where heater uses 2kw epr hour and charges o.15rs per kw
heater_power_kw=2
run_time_hours=5
cost_per_kw=0.15
total_energy_kwh=heater_power_kw*run_time_hours
total_cost=total_energy_kwh*cost_per_kw
print(f"Total cost: ${total_cost:.2f}") 
print(f"Total Power: {total_energy_kwh:.2f}kw")
