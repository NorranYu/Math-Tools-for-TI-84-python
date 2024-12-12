#program returns a quadratic function's vertex and its 'vertex form' [a(x-h)^2 + k]. 
#Useful for quick calculations and/or graphing by hand

print("\nIn the format of ax^2 + bx + c\n\n")
a = int(input("Input your 'a' value "))
b = int(input("Input your 'b' value "))
c = int(input("Input your 'c' value "))

vx = round(b / (2 * a), 3)
vy = round((b**2 - 4*a*c) / (4*a), 3)

if (vx >= 0 and vy >= 0):
    print("\n\nVertex form for graphing:\ny = " + str(float(a)) + "(x + " + str(float(vx)) + ")^2 - (" + str(float(vy)) + ")")
    print("\nVertex located at (-" + str(float(vx)) + ", -" + str(float(vy)) + ")")
elif (vx < 0 and vy < 0):
    print("\n\nVertex form for graphing:\ny = " + str(float(a)) + "(x - " + str(abs(float(vx))) + ")^2 + (" + str(abs(float(vy))) + ")")
    print("\nVertex located at (" + str(abs(float(vx))) + ", " + str(abs(float(vy))) + ")")
elif (vx >= 0 and vy < 0):
    print("\n\nVertex form for graphing:\ny = " + str(float(a)) + "(x + " + str(float(vx)) + ")^2 + (" + str(abs(float(vy))) + ")")
    print("\nVertex located at (-" + str(float(vx)) + ", " + str(abs(float(vy))) + ")")
elif (vx < 0 and vy >= 0):
    print("\n\nVertex form for graphing:\ny = " + str(float(a)) + "(x + " + str(abs(float(vx))) + ")^2 - (" + str(float(vy)) + ")")
    print("\nVertex located at (" + str(abs(float(vx))) + ", -" + str(float(vy)) + ")")

#print(f"y = {a}x + {{(b / (2 * a))**2}} - {((b**2) - (4 * a * c)) / (4 * a)}")
