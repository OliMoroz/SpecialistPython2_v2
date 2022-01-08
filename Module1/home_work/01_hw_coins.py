import random

class Coin:
    def __init__(self, side, heads, tails):
        # heads-орел/tails-решка
        self.side = None
        self.heads = heads #орел
        self.tails = tails #решка


    def flip(self):
        #print(self.side)
        #for _ in range(n):
        a = int(random.randint(1, 10000))
        if a % 2 == 0:
            return self.heads
            #print(self.heads)
            #i += 1
        else:
            return self.tails
            #print(self.tails)
            #j += 1
        #
        # if n == n:
        #     return ''


            #print(self.heads) if a % 2 == 0 else print(self.tails)
h = 0
t = 0
n = int(input('Введите число: '))
coin1 = Coin('None', 'heads', 'tails')
coin_l = []
for i in range(n):
    coin_l.append(coin1.side)
print('Cписок с какими-то монетами - ', coin_l)

for i in range(0, len(coin_l)):
    if coin_l[i] == None:
        coin_l[i] = coin1.flip()
        if coin_l[i] == 'heads':
            h += 1
        else:
            t += 1
    i += 1
print('Cписок с монетами после подбрасывания - ', coin_l)
print('heads = ', round(h / n * 100, ), '%', 'tails = ', round(t / n * 100, ), '%')

#print(coin1.flip())

