# 1. Suppose you have a dataset containing daily temperature readings for a city, and you want to identify days with extreme temperature conditions. Find days where the temperature either exceeded 35 degrees Celsius (hot day) or dropped below 5 degrees Celsius (cold day). 

# Input:

# temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2,4,25,12,-4,-12])
import numpy as np

temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2, 4, 25, 12, -4, -12])

# Find hot days (above 35°C)
hot_days = temperatures[temperatures > 35]

# Find cold days (below 5°C)
cold_days = temperatures[temperatures < 5]

print("Hot days (above 35°C):", hot_days)
print("Cold days (below 5°C):", cold_days)
# output:
# Hot days (above 35°C): [36.8 38.7 37.2]
# Cold days (below 5°C): [  4.  -4. -12.]







# 2. Suppose you have a dataset containing monthly sales data for a company, and you want to split this data into quarterly reports for analysis and reporting purposes. 

# Input: monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])
import numpy as np
monthly_sales = np.array([120, 135, 148, 165, 180, 155, 168, 190, 205, 198, 210, 225])

# Split the data into 4 quarters
quarterly_sales = np.split(monthly_sales, 4)

# Display the quarterly sales
for i, quarter in enumerate(quarterly_sales, 1):
    print(f"Q{i} sales: {quarter}")
# output:
# Q1 sales: [120 135 148]
# Q2 sales: [165 180 155]
# Q3 sales: [168 190 205]
# Q4 sales: [198 210 225]