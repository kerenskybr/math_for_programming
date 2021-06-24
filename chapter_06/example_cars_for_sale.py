from coordinate_vectors import Vector
from datetime import datetime

class CarForSale(Vector):
    retrieved_data = datetime(2018,11,30,12)
    def __init__(self, model_year, mileage, price, posted_datetime, model="(virtual)", source="(virtual)", location="(virtual)", description="(virtual"):
        self.model_year = model_year
        self.mileage = mileage
        self.price = price
        self.posted_datetime = posted_datetime
        self.model = model
        self.source = source
        self.location = location
        self.description = description

    def add(self, other):
        def add_dates(d1, d2):
            age1 = CarForSale.retrieved_data - d1
            age2 = CarForSale.retrieved_data - d2
            sum_age = age1 + age2
            return CarForSale.retrieved_data - sum_age
        return CarForSale(self.model_year + other.model_year, self.mileage + other.mileage, self.price + other.price, add_dates(self.posted_datetime, other.posted_datetime))

    def scale(self, scalar):
        def scale_date(d):
            age = CarForSale.retrieved_data - d
            return CarForSale.retrieved_data - (scalar * age)

        return CarForSale(scalar * self.model_year, scalar * self.mileage, scalar * self.price, scale_date(self.posted_datetime))

    @classmethod
    def zero(cls):
        return CarForSale(0, 0, 0, CarForSale.retrieved_data)


# Loading data from disc
from json import loads, dumps
from pathlib import Path
from datetime import datetime
contents = Path('cargraph.json').read_text()
cg = loads(contents)
cleaned = []

def parse_date(s):
    input_format="%m/%d - %H:%M"
    return datetime.strptime(s,input_format).replace(year=2018)
    
    return dt
for car in cg[1:]:
    try:
        row = CarForSale(int(car[1]), float(car[3]), float(car[4]), parse_date(car[6]), car[2],  car[5],  car[7], car[8])
        cleaned.append(row)
    except: pass

cars = cleaned

(cars[0] + cars[1]).__dict__

average_prius = sum(cars, CarForSale.zero()) * (1.0/len(cars))
average_prius.__dict__