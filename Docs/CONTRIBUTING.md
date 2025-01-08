# Contribuciones al Proyecto

¡Gracias por tu interés en contribuir a este proyecto! Por favor, sigue estas directrices para asegurarte de que tu contribución sea revisada y aceptada de manera rápida y eficiente.

## Instalacion

### **Crear un fork y clonarlo**

1. Accede a la página principal del proyecto en [GitHub](https://github.com/Egid10p/Laberinto).
2. Haz click en el botón `Fork` en la parte superior derecha de la página.
3. Clona el fork en tu máquina local con el comando:
    ```sh
    git clone https://github.com/tu/fork
    ```

### **_Crea un entorno virtual_**

Se recomienda trabajar en un entorno virtual para evitar conflictos con las librerias

Para crear un entorno virtual tienes que:

1. Ejecutar en el directorio donde clonaste el repositorio el comando
   `python -m venv venv` para asi crear el entorno virtual
2. Activar el entorno virtual con el comando `venv\Scripts\activate`o si estas en linux o macOS `source venv/bin/activate`

3. Ahora para instalar las dependencias ejecuta `pip install -r requirements.txt`

### **_Testing_**

Comprueba de que el poryecto se haya instalado sin errores.

En un terminal ejecuta el archivo `run_tests.py` que se encuestra en la carpeta `tests`

y por ultimo revisa el output

## Formateo

Estas reglas de formateo son para evitar "ruido" al hacer tu pull request, se refiere a que por ejemplo uses comillas simples ("") en vez de comillas doble ('')

El formateador utilizado en este proyecto es **Flake8**

### **_Reglas de formateo_**

-   Usar comillas dobles
-   Usar 4 espacios en la tabulacion
-   Nombrar las variables, funciones o clases en ingles
-   Nombrar las variables con snake_case
-   Nombrar las funciones con snake_case
-   Nombrar las clases con UpperCamelCase
-   Comenta tu codigo en ingles

## Documentation

Porfavor documenta tu codigo creando un archivo en el directorio `Docs`

`Example: MyClassdDoc.md`

## Calidad de Código (QA)

Una vez hecho tus cambios haz archivos de testing para tu codigo, o si ya existe actualizalo para cubrir todos lo posibles fallos.

Los archivos de testing tienen que tener el siguiente nombre
`test <Nombre de tu archivo>` por ejemplo `test_Mouse.py`

Los archivos de testing tienen que estar creados con la libreria pytest

## Pull request

Una vez que hayas hecho todos tus cambios

#### 1. **_Asegurate de que todo funcione y no haya errores_**

#### 2. **_Asegurate de seguir con las reglas de formateo y QA especificadas arriba_**

#### 3. **_Agrega al final de tu archivo el link o el ID del issue si corresponde_**
