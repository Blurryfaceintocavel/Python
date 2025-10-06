#Questões com Temperatura

# Kelvin, Farehit

cel=float  (input(f"Digite o valor em Celsius: "))
fare=(cel*1.8)+32
kel=cel+273
print (f"O valor digitado  {cel}°em celsius,e em farehit {fare}f e Kelvin é {kel}")

#Temperatura

Temp= int (input ("Digite a temperatura: "))

if Temp <15 and Temp >=0: 
  print (f"Frio 🥶 {Temp}°C")
  
elif Temp >=15 and Temp<=25:
  print (f"Ameno 😄 {Temp}°C ")
else:
    print (f"Quente 🥵 {Temp}°C ")
