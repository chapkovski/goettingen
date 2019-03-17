import csv
import pandas as pd

db = pd.read_csv('houses.csv')

with open('houses.csv') as f:
    houses = list(csv.DictReader(f))

for h in houses:
    print('SPACE', int(h['width']) * int(h['length']))
    print('VOLUME', int(h['height']) * int(h['width']) * int(h['length']))
    if int(h['village']) == 1:
        print('PRICE', int(h['height']) * int(h['width']) * int(h['length']) * 100)
    else:
        print('PRICE', int(h['height']) * int(h['width']) * int(h['length']) * 50)

########### BLOCK: BETTER ##############################################################
village_price, city_price = 50, 100


class House:
    def __init__(self, length, width, height, village):
        self.length = int(length)
        self.width = int(width)
        self.height = int(height)
        self.village = bool(village)
        if self.village:
            self.price_per_m = village_price
        else:
            self.price_per_m = city_price

    def get_space(self):
        return self.length * self.width

    def get_volume(self):
        return self.height * self.get_space()

    def get_price(self):
        return self.get_volume() * self.price_per_m

new_houses = [House(**h) for h in houses]

for h in new_houses:
    print(f'SPACE: {h.get_space()}')
    print(f'VOLUME: {h.get_volume()}')
    print(f'PRICE: {h.get_price()}')
############ END OF: BETTER #############################################################
