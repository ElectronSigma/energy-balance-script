# El codigo resuelve el balance de energia para un sistema transitorio donde entra masa a un volumen de control para determinar la temperatura final.
# This code solves the energy balance for a dynamic system where an amount of mass enters a control volume to calculate the temperature.

def calcT(masa_inicial,temperatura_inicial,masa_entrada,temperatura_entrada):
	masa_final = masa_inicial + masa_entrada
	temperatura_final = (masa_inicial*temperatura_inicial + masa_entrada*temperatura_entrada)/(masa_final)
	return temperatura_final

mi = float(input("Ingrese la masa inicial(kg): "))
ti = float(input("Ingrese la temperatura inicial(K): "))
me = float(input("Ingrese la masa entrante(kg): "))
te = float(input("Ingrese la temperatura entrante(K): "))

print(f"La temperatura de salida es: {calcT(mi,ti,me,te)}K o {calcT(mi,ti,me,te) - 273}C")