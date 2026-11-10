# Convert an entered Celsius temperature to Fahrenheit and Kelvin.

'''The purpose of this code is to convert Celsius to Fahrenheit and Fahrenheit to Celsius.'''


def celsius_fahrenheit(celsius):
    conversao = (celsius * (9/5)) + 32
    return conversao

def celsius_kelvin(celsius):
    conversao = celsius + 273,15
    return conversao

temp = float(input('Digite a temperatura em celcius: '))

fahrenheit = celsius_fahrenheit(temp)
kelvin = celsius_kelvin(temp)

print(f'{temp} graus é equivalente a {fahrenheit} Fahrenheit e {kelvin} em Kelvin')