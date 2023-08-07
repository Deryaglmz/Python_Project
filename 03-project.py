# Salary Calculation

basis = 12500

for_each_year_of_experiencen =100 

for_child =250

for_each_hour_of_overtime =50


experience = int (input("How many years of your experience :"))

child = int (input("how many children do you have : "))

shift = int (input("How many hours did you work overtime? :"))

wage =basis + experience*for_each_year_of_experiencen + child*for_child +shift*for_each_hour_of_overtime

print("wage : ", wage)
