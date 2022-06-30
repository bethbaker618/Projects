# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the block. 
# Your job is to go through the lists of data that have been collected in the past couple of weeks. 
# You will be calculating some important metrics that Carly can use to plan out the operation of the business for the rest of the month.

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

total_price = 0
index = 0
count = len(prices)
while count > index:
  total_price += prices[index]
  index += 1
print(total_price)
average_price = total_price/count
print("Average Haircut Price: ")
print(average_price)
new_prices = [price-5 for price in prices]
print(new_prices)

total_revenue = 0
for i in range(len(hairstyles)):
  total_revenue += (last_week[i]*prices[i])
print("Total Revenue: " + str(total_revenue))

average_daily_revenue = total_revenue/7
print("Average Daily Revenue: " + str(average_daily_revenue))

cuts_under_30 = [hairstyles[i] for i in range(len(prices)-1) if prices[i] < 30]
print(cuts_under_30)