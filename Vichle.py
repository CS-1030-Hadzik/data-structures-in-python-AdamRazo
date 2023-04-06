class Vehicle:
    def __init__(self, make, model, year):
        self.parameters = make
        self.model = model
        self.year = year

    def  start(self):
        print('The car is starting...')

    def stop(self):
        print('The car is stopping...')