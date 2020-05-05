def ground_shipping(weight):
    if weight <= 2:
        cost = 1.50 
    elif weight <= 6:
        cost = 3.00 
    elif weight <= 10:
        cost = 4.00
    else:
        cost = 4.75 
    return 20 + (cost * weight)

print(ground_shipping(8.4))

premium_ground_shipping = 125

def drone_shipping(weight):
  if weight <= 2:
    cost =  4.50 
  elif weight <= 6:
    cost = 9.00 
  elif weight <= 10:
    cost = 12.00 
  else:
    cost =  14.25 
  return cost * weight

print(drone_shipping(1.5))      

def cheapest_shipping_method(weight):
    ground = ground_shipping(weight)
    premium = premium_ground_shipping
    drone = drone_shipping(weight)
    
    if ground < premium and ground < drone:
        method = "Ground shipping"
        cost = ground
    elif premium < ground and premium < drone:
        method = "Premium Ground Shipping"
        cost = premium
    else:
        method = "Drone shipping"
        cost = drone
        
    print("The cheapest shipping method is %s which costs $%.2f " %( method, cost))

cheapest_shipping_method(4.8)
cheapest_shipping_method(41.5)
