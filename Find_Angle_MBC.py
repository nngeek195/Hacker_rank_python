import math

y = input()
y = float(y)
x = input()
x = float(x)

hypo = (math.sqrt(pow(x,2)+ pow(y,2)))/2

tan_angle = float(y/x)

angle = math.atan(tan_angle)

Tan_thita = (math.sin(angle)*hypo)/(x-hypo*math.cos(angle))

Final_angle = math.atan(Tan_thita)

final = round(math.degrees(Final_angle))

print(f"{final}\u00b0")
