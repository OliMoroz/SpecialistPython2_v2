class Car:
    mileage_x = 100
    def __init__(self, gas, capacity, gas_per_km):
        self.gas = gas
        self.capacity = capacity
        self.gas_per_km = gas_per_km


    def fill(self, fuel):
        self.gas = self.gas + fuel

        if self.gas <= self.capacity:

            print('бак пополнен')
            f.write('бак пополнен')

        elif self.gas > self.capacity:
            surplus = self.gas - self.capacity
            self.gas = self.capacity
            print('бак полон, остаток - ', surplus, 'л')
            f.write(f'бак полон, остаток - {surplus} л ' + '\n')

    def ride(self, distance):
        while self.gas > 0:
            n = input('вы готовы ехать y/n? - ')
            if n == 'y':
                litrs = round(self.gas_per_km / 100 * distance)  # потратит л на заданный км путь
                self.gas = self.gas - litrs
                way = round(self.gas / self.gas_per_km * 100)  # проедет км на том количистве топлива в баке, которое есть сейчас
                if self.gas > 0:
                    Car.mileage_x = distance + Car.mileage_x
                    print('Вы проехали  - ', distance, 'км')
                    print('осталось л - ', self.gas, 'можете еще проехать - ', way)
                    f.write(f'Вы проехали  - {distance} км' + '\n')
                    f.write(f'осталось л - {self.gas} можете еще проехать - {way}' + '\n')
                elif self.gas <= 0:
                    self.gas = self.gas + litrs
                    print('пора заправится')
                    f.write('пора заправится' + '\n')
                    break
            else:
                print('конец')
                f.write('конец' + '\n')
                break

        print('пробег - ', Car.mileage_x)
        f.write(f'пробег - {Car.mileage_x}' + '\n')


    def mileage(self, x):
        Car.mileage_x = x
# а) У машины  должны быть атрибуты
#
# "сколько бензина в баке"(gas)топливо "вместимость бака" - сколько максимум
# вмещается бензина(capacity)емкость
# "расход топлива на км"(gas_per_km) - расход
f = open('02.md', 'w')
#f.close()
car1 = Car(30, 50, 12)

print(car1.gas, ' л в баке')
print(car1.capacity, ' объем в бака')
print(car1.gas_per_km, ' расход')

f.write(f'{car1.gas} л в баке' + '\n')
f.write(f'{car1.capacity}, объем в бака' + '\n')
f.write(f'{car1.gas_per_km} расход' + '\n')
# б) метод "залить столько-то литров в бак"
# car1.fill(5)  # залили 5 литров
# должна  учитываться вместительность  бака  если  пытаемся
# залить больше, чем вмещается, то заполняется
# полностью + print  'ом выводится сообщение о лишних литрах

car1.fill(10)
print(car1.gas, ' л в баке')
print(car1.capacity, ' объем в бака')
print(car1.gas_per_km, ' расход')

f.write(f'{car1.gas} л в баке' + '\n')
f.write(f'{car1.capacity} объем в бака' + '\n')
f.write(f'{car1.gas_per_km} расход' + '\n')

# в) метод  "проехать сколько-то км"
#
# car1.ride(50)  # едем 50 км (если хватит топлива)
# выведите сообщение: "проехали ... километров"  в  результате
# поездки  тратится  бензин  Машина едет
# пока хватает бензина
#

car1.ride(50)
print(car1.gas, ' л в баке')

f.write(f'{car1.gas} л в баке' + '\n')
# г) добавить  атрибут  с пробегом mileage, который
# увеличивается в  результате  ride
print('Пробег - ', Car.mileage_x)

f.write(f'Пробег -  {Car.mileage_x}' + '\n')
f.close()
