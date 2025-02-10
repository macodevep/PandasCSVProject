import pandas as pd

personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Domingo", "edad": 15, "ciudad": "Barcelona"},
    {"nombre": "Rafael", "edad": 77, "ciudad": "Valencia"},
    {"nombre": "Alejandro", "edad": 23, "ciudad": "Granada"},
    {"nombre": "Norma", "edad": 43, "ciudad": "Málaga"},
    {"nombre": "Iker", "edad": 45, "ciudad": "Sevilla"},
    {"nombre": "Hugo", "edad": 34, "ciudad": "Gerona"},
    {"nombre": "José", "edad": 29, "ciudad": "Bilbao"},
    {"nombre": "Lucio", "edad": 17, "ciudad": "La coruña"},
    {"nombre": "María", "edad": 18, "ciudad": "Pamplona"},
    {"nombre": "Andrea", "edad": 16, "ciudad": "Alicante"},
    {"nombre": "Valentina", "edad": 54, "ciudad": "Madrid"},
    {"nombre": "Alicia", "edad": 63, "ciudad": "Barcelona"},
    {"nombre": "Sofía", "edad": 52, "ciudad": "Zaragoza"},
    {"nombre": "Adrián", "edad": 37, "ciudad": "Barcelona"},
    {"nombre": "Luis", "edad": 30, "ciudad": "Valencia"}
]


for persona in personas:
    if persona["edad"] > 18:
        print(f"Nombre: {persona['nombre']}, Edad: {persona['edad']}")



df = pd.DataFrame(personas)
df.to_csv('personas.csv', index=False)



def promedio_edades(personas):
    edades = [p["edad"] for p in personas]
    return sum(edades) / len(edades)

print(f"Promedio de edades: {promedio_edades(personas)}")