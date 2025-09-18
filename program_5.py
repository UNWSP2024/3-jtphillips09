# There are two kinds of hot dogs sold:  
# Hot Dog ($3.50), Chili Dog ($4.50).  
# Additionally a person can order cheese ($0.50), peppers ($0.75), or grilled onions ($1.00).  
# Also tax is 7%. 
# Write a program the inputs the type of hot dog wanted and optional toppings.  
# The program then displays the hot dog cost, tax and total cost. 
def hotdog_order(hotdog_type, cheese, peppers, onions):
 cost = 0.0
 if hotdog_type.lower() == "hot dog":
        cost = 3.50
 elif hotdog_type.lower() == "chili dog":
        cost = 4.50
 else:
        cost = 3.50 
 if cheese:
        cost += 0.50
 if peppers:
        cost += 0.75
 if onions:
        cost += 1.00
 tax = cost * 0.07
 total = cost + tax
 return cost, tax, total
if __name__ == '__main__':
   hotdog_type = input("Enter the hot dog type (hot dog / chili dog): ")
cheese = input("Do you want cheese? (yes/no): ").strip().lower() == "yes"
peppers = input("Do you want peppers? (yes/no): ").strip().lower() == "yes"
onions = input("Do you want grilled onions? (yes/no): ").strip().lower() == "yes"
cost, tax, total = hotdog_order(hotdog_type, cheese, peppers, onions)
print("Hot Dog Cost: $", format(cost, ".2f"))
print("Tax: $", format(tax, ".2f"))
print("Total Cost: $", format(total, ".2f"))
