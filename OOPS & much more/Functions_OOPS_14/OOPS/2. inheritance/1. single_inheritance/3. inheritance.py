# Improve version of 2.inheritance
class Car:
    def set_car_info(self, color, type, mileage, seat_capacity):
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
    def set_audi_info(
        self,
        color: str,
        type: str,
        mileage: float,
        seat_capacity: int,
        electric: bool,
        city: str,
    ):
        self.set_car_info(color, type, mileage, seat_capacity)
        self.electric = electric
        self.city = city

    def audi_info(self):
        print(f"electric = {self.electric}")
        print(f"city = {self.city}")


c1 = Audi()
c1.set_audi_info("black", "Petrol", 12.4, 6, True, "Mumbai")
c1.audi_info()
c1.base_info()
