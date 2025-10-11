class CarClass :
    def __init__(self, color, production_year,maximum_speed):
        self.color=color
        self.production_year=production_year
        self.maximum_speed=maximum_speed
        self.current_speed=0.1
        self.lights_status=False

    def accelerate(self,velocity):
        if  self.__check_speed(self.current_speed+velocity):
           self.current_speed+=velocity
           print(f"Accelerated current velocity is :{self.current_speed}")

    def decelerate(self,velocity):
        if  self.__check_speed(self.current_speed-velocity):
           self.current_speed-=velocity
           print(f"Decelerated current velocity is :{self.current_speed}")

    def __check_speed(self,targetSpeed):
        if targetSpeed <= 0:
           print(f"Speed is already 0.")
           return False
        if targetSpeed >= self.maximum_speed:
           print(f"""Already passed the maximum speed {self.maximum_speed}.
                 Our speed is {self.current_speed}""")
           return False
        return True

    def set_lights(self,lights_status):
        self.lights_status=lights_status
        if self.lights_status == True:
           print(f"Lights are ON")
        else:
           print(f"Lights are OFF")
