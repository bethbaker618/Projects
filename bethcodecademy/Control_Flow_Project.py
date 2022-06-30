# Write a shipping.py Python program that asks the user for the weight of their package and then tells them 
# which method of shipping is cheapest and how much it will cost to ship their package using Sal’s Shippers.

weight = 41.5
#GroundShipping
if weight <= 2:
  price = 1.50*weight + 20
  print("Standard Ground Shipping: " + str(price))
elif weight <= 6:
  price = 3.0*weight + 20
  print("Standard Ground Shipping: " + str(price))
elif weight <= 10:
  price = 4.0*weight + 20
  print("Standard Ground Shipping: " + str(price))
else:
  price = 4.75*weight + 20
  print("Standard Ground Shipping: " + str(price))

Premium_Ground_Shipping_Cost = 125
print("Premium Ground Shipping: " + str(Premium_Ground_Shipping_Cost))

#DroneShipping
if weight <= 2:
  price = 4.50*weight 
  print("Drone Shipping: " + str(price))
elif weight <= 6:
  price = 9.0*weight 
  print("Drone Shipping: " + str(price))
elif weight <= 10:
  price = 12.0*weight 
  print("Standard Ground Shipping: " + str(price))
else:
  price = 14.25*weight 
  print("Standard Ground Shipping: " + str(price))