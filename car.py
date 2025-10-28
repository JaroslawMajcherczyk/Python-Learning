
class Car:

    wheels = 4

    def __init__(self,model,yer,color,for_sale):
        self.model = model
        self.yer = yer
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive a {self.color} {self.model}")

    def stop(self):
        print(f"You stop a {self.color} {self.model}")

    def describe(self):
        print(f"{self.yer} {self.color} {self.model}")