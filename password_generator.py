import random
import string

#Program generujący losowe hasło spełniające warunki zadane przez użytkownika
dane = []
print("Jeżeli zamiast wybrać, chcesz wylosować liczbę od 4 do 12, wpisz \"r\"")
lower_case = input("Podaj liczbę małych liter: \n")
dane.append(lower_case)
upper_case = input("Podaj liczbę wielkich liter: \n")
dane.append(upper_case)
numbers = input("Podaj liczbę cyfr: \n")
dane.append(numbers)
special = input("Podaj liczbę znaków specjalnych: \n")
dane.append(special)

for i in range(len(dane)):
  if dane[i] == "r":
    dane[i] = random.randint(4,12)
  else:
    dane[i] = int(dane[i])

password = ""
while sum(dane) > 0:
  if random.randint(1,4) == 1 and dane[0] > 0:
    password += string.ascii_lowercase[random.randint(1,26)]
    dane[0] -= 1
  if random.randint(1,4) == 2 and dane[1] > 0:
    password += string.ascii_uppercase[random.randint(1,26)]
    dane[1] -= 1
  if random.randint(1,4) == 3 and dane[2] > 0:
    password += str(random.randint(0,9))
    dane[2] -= 1
  if random.randint(1,4) == 4 and dane[3] > 0:
    password += string.punctuation[random.randint(0,31)]
    dane[3] -= 1
print(password)
