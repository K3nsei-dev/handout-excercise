# compulsory Task
# cost of night is in rands

def hotel_cost(nights):
    return nights*140


# defining a plane ride cost
# cost in rands

def plain_ride_cost(city):
    if "Cape Town" == city:
        return 2500
    elif "Durban" == city:
        return 2300
    elif "JHB" == city:
        return 2000
    elif "BFN" == city:
        return 1800


# defining a rental car price
# cost in rands

def rental_car_cost(days):
    car_cost = 40 * days  # cost in rands
    if days >= 7:

        car_cost = car_cost - 50
    elif days >= 3 and days < 7:
        car_cost = car_cost - 20
    return car_cost



# defining a cost of a trip
# cost in rands

def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plain_ride_cost(city) + spending_money


location = input("Where did you stay: ")
days = int(input("How many days did you stay: "))
extras = float(input("How much extra did you spend on extras: "))


print(trip_cost(location, days, extras))
