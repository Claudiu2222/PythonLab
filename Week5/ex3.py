class Vehicle():
    def __init__(self, make, model, year, weight, fuel_tank_size, fuel_usage_100km,number_of_wheels,mileage = 0):
        self.validate_input(make, model, year, weight, fuel_tank_size, fuel_usage_100km,mileage)
        self.make = make       
        self.model = model
        self.year = year
        self.weight = weight
        self.fuel_tank_size = fuel_tank_size
        self.current_fuel_level = fuel_tank_size
        self.mileage = mileage
        self.fuel_usage_100km = fuel_usage_100km
        self.trip_distance = 0
        self.max_tow_weight = self.compute_max_tow_weight(weight)
        self.number_of_wheels = number_of_wheels
    
    def drive_distance(self, distance):
        if distance < 0:
            raise ValueError("distance cannot be negative")
        if self.get_fuel_level() < distance / 100 * self.fuel_usage_100km:
            raise ValueError("not enough fuel")
        print("Driving "+str(distance) + " km")
        self.mileage += distance
        self.trip_distance += distance
        self.current_fuel_level -= distance / 100 * self.fuel_usage_100km
    
    def reset_trip(self):
        self.trip_distance = 0

    def add_fuel(self, fuel):
        if fuel < 0:
            raise ValueError("fuel cannot be negative")
        if self.get_fuel_level() + fuel > self.fuel_tank_size:
            raise ValueError("too much fuel")
        self.current_fuel_level += fuel
    
    def get_fuel_level(self):
        return self.current_fuel_level

    def get_mileage(self):
        return self.mileage
    
    def tow(self, attached_cargo, distance):
        if attached_cargo.weight > self.max_tow_weight:
            raise ValueError("Vehicle IS TOO HEAVY to tow")
        if distance < 0:
            raise ValueError("distance cannot be negative")
        if self.get_fuel_level() < distance / 100 * self.fuel_usage_100km:
            raise ValueError("not enough fuel")
        print("Towing " + str(attached_cargo)+ " of weight " +str(attached_cargo.weight) + " for distance "+str(distance))    
        self.drive_distance(distance)

    def compute_max_tow_weight(self, weight):
        return weight * 1
    
    def __str__(self):
        return "Vehicle: "+self.make+" "+self.model+" "+str(self.year)
    
    def __repr__(self):
        return "Vehicle: "+self.make+" "+self.model+" "+str(self.year)
    
    def validate_input(self, make, model, year, weight, fuel_tank_size, fuel_usage_100km,mileage):
        if year < 0:
            raise ValueError("year cannot be negative")
        if weight < 0:
            raise ValueError("weight cannot be negative")
        if fuel_tank_size < 0:
            raise ValueError("fuel_tank_size cannot be negative")
        if fuel_usage_100km < 0:
            raise ValueError("fuel_usage_100km cannot be negative")
        if mileage < 0:
            raise ValueError("mileage cannot be negative")
        if make == "":
            raise ValueError("make cannot be empty")
        if model == "":
            raise ValueError("model cannot be empty")
    
class Car(Vehicle):
    def __init__(self, make, model, year, weight, fuel_tank_size, fuel_usage_100km,mileage = 0):
        super().__init__(make, model, year, weight, fuel_tank_size, fuel_usage_100km,4 ,mileage)
    def compute_max_tow_weight(self, weight):
        return weight * 1.5
class Motorcyle(Vehicle):
    def __init__(self, make, model, year, weight, fuel_tank_size, fuel_usage_100km,mileage = 0):
        super().__init__(make, model, year, weight, fuel_tank_size, fuel_usage_100km,2,mileage)
    def compute_max_tow_weight(self, weight):
        return weight * 0.5

class Truck(Vehicle):
    def __init__(self, make, model, year, weight, fuel_tank_size, fuel_usage_100km,mileage = 0):
        super().__init__(make, model, year, weight, fuel_tank_size, fuel_usage_100km,4,mileage)
    def compute_max_tow_weight(self, weight):
        return weight * 2


try:
    car = Car("Ford", "Fiesta", 2019, 1000, 45, 5)   
    motorcycle = Motorcyle("Honda", "CBR", 2019, 200, 15, 7)
    print(car)
    print("Current fuel level " + str(car.get_fuel_level()))
    car.drive_distance(100)
    car.add_fuel(3)
    print("Current fuel level " + str(car.get_fuel_level()))
    print("Current car mileage " +str(car.get_mileage()))
    car.reset_trip()
    car.tow(motorcycle, 150)
    print("Current fuel level " + str(car.get_fuel_level()))
    print("Current car mileage " +str(car.get_mileage()))
except ValueError as e:
    print(e)