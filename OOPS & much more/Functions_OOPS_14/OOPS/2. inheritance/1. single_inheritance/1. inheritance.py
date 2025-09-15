class Car:
    def __init__(self, color, type, mileage, seat_capacity):
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"milage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(self):
        print("Audi init")


# Acessing Car class
c1 = Car("Black", "Petrol", 22.3, 7)
c1.base_info()

# Acessing car class through audi
# c2 = Audi()
# c2.base_info()  # Accessing base_info in car class
# py pehle audio class mai base_info search krega jo nhi hai fir car class mai dekhega
# jo ki hai pr vha hum variable print kara rhe hai define hmne init mai kiya hai so attribute error
# pr hme variable k naam pta hai to unko access kr skte hai

c3 = Audi()
c3.color = "Blue"
c3.type = "CNG"
c3.mileage = 33.2
c3.seat_capacity = 4
c3.base_info()
