def ctf(celsius):
    return (celsius * 9/5) + 32

def ftc(fahrenheit):
    return (fahrenheit - 32) * 5/9
 
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = ctf(celsius)
print(fahrenheit)
fahrenhei = float(input("Enter temperature in Fahrenheit: "))
celsiu = ftc(fahrenhei)
print(celsiu)
