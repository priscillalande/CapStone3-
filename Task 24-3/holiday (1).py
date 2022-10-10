def hotel_cost(nights):#Cost of the hotel per night 
    return nights * 875

def plane_cost(city):#plane cost is calculated by per city that will be visited 
    ticket = 0
    
    if city == '1':#City 1 = OR Tambo
        ticket = 750

    elif city == '2':#City 2 = Cape Town
        ticket = 850
    elif city == '3':#City 3 = King Shaka
        ticket = 600
    
    return ticket
    

def car_rental(days):#car rental per days 
    return days * 275

def holiday_cost(nights, city, days):#Calculation of the holiday in totality , nights,city,and rental
    nights = hotel_cost(nights)
    city = plane_cost(city)
    days = car_rental(days)
    return nights + city + days

nights = int(input('How many nights will you be staying? '))#Asking the user how may days they will be staying 
city = input('\n1. O.R. Tambo International\n2. Capetown International\n3. King Shaka International\nWhere you flying to? ')#asking the user, where they are planing to visit
days = int(input('How many days will you need a car for?: '))#asking how many days the user will be needing thr car for 

total = holiday_cost(nights,city,days)#calculation of the total cost 
description = " total : "
print (total)#print total cost 
