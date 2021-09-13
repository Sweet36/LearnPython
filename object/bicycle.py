#自行车
class Bicycle:
    def run(self,km):
        print(f"骑行了{km}km")

#电瓶车
class EBicycle(Bicycle):
    battery_leve:int
    def __init__(self,battery):
        self,battery_level = battery
    def fill_charge(self,vol):


