class Car:
    def __init__(self, color: str, type: str, mileage: float, seat_capacity: int):
        self.color = color
        self.type = type
        self.mileage = mileage
        self.seat_capacity = seat_capacity
        print("Car init")

    def base_info(self):
        print(f"color = {self.color}")
        print(f"type = {self.type}")
        print(f"milage = {self.mileage}")
        print(f"seat_capacity = {self.seat_capacity}")


class Audi(Car):
    def __init__(
        self,
        color: str,
        type: str,
        mileage: float,
        seat_capacity: int,
        electric: bool,
        city: str,
    ):
        super().__init__(
            color, type, mileage, seat_capacity
        )  # passing to Car's __init__
        self.electric = electric
        self.city = city
        print("Audi init")

    def audi_info(self):
        print(f"electric = {self.electric}")
        print(f"city = {self.city}")

    def show_full(self):
        self.base_info()
        self.audi_info()


# Create object with all required arguments
c1 = Audi("black", "Petrol", 12.4, 6, True, "Mumbai")
print("--------------------")
c1.show_full()
