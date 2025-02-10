# PandasCSVProject

Este proyecto en Python utiliza la librería Pandas para procesar una lista de diccionarios, filtrar personas mayores de edad y generar un archivo CSV con los resultados.

## Descripción general

Este mini proyecto demuestra el uso básico de Pandas para manipular datos y generar un archivo CSV. Toma una lista de diccionarios, donde cada diccionario representa a una persona con su nombre y edad. Utiliza Pandas para crear un DataFrame, filtrar las personas mayores de edad con su nombre y edad respectivamente, guardando los resultados en un archivo CSV.

## Instalación

Para ejecutar este proyecto, necesitas tener Python instalado y la librería Pandas. Puedes instalar Pandas con pip:

```bash
pip install pandas
```

## Uso

1.  Clona este repositorio: `git clone https://github.com/macodevep/PandasCSVProject.git`
2.  Ejecuta el script: `python app.py`

El script tomará una lista de diccionarios (puedes modificarla en el código), realizará el filtrado y generará un archivo CSV llamado con los resultados.

## Ejemplo

```python
# Ejemplo de uso (puedes modificar esta lista)
personas = [
    {"nombre": "Juan", "edad": 25, "ciudad": "Madrid"},
    {"nombre": "Domingo", "edad": 15, "ciudad": "Barcelona"},
    {"nombre": "Rafael", "edad": 77, "ciudad": "Valencia"}

# El script generará un archivo CSV con las personas mayores de edad

# Funcionalidades

Filtrado de edad:Filtra una lista de personas para obtener solo las mayores de edad (18 años o más).

Manipulación con Pandas: Utiliza la librería Pandas para crear un DataFrame y realizar el filtrado de manera eficiente.

Generación de CSV: Crea un archivo CSV con los resultados del filtrado, incluyendo el nombre y la edad de las personas mayores de edad.

## Licencia

Este proyecto está bajo la licencia MIT.

## Contacto

María Pacheco - macodeveloper23@gmail.com
