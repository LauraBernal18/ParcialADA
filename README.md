# Parcial Práctico: Solución "Big Sorting" (HackerRank)

Este repositorio contiene la solución óptima en Python para el problema **"Big Sorting"** de HackerRank, correspondiente a la sección de **Sorting / Search** del parcial práctico.

## Cómo poner a funcionar el programa

Existen dos formas de ejecutar y probar este código:

### Opción 1: Ejecución Directa en HackerRank (Recomendado)
1. Copia el código fuente completo del archivo `solucion.py` de este repositorio.
2. Ve al problema [Big Sorting en HackerRank](https://hackerrank.com).
3. Selecciona **Python 3** como lenguaje en el editor de HackerRank.
4. Pega el código y presiona el botón **"Submit Code"**. Pasará todos los casos de prueba inmediatamente.

### Opción 2: Ejecución Local (Línea de comandos)
Para correr el script en tu computadora, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone <LINK_DE_TU_REPOSITORIO>
   cd <NOMBRE_DE_TU_CARPETA>
   ```

2. **Preparar el entorno:**
   Este programa utiliza la librería estándar de Python 3, por lo que **no requiere instalar ninguna dependencia de terceros**. Asegúrate de tener instalado Python 3.x de forma global en tu sistema.

3. **Configurar variable de entorno (Simulación de HackerRank):**
   El bloque principal utiliza una variable de entorno llamada `OUTPUT_PATH` para escribir el archivo de salida. Debes definirla antes de ejecutar el programa:
   * **En Linux / macOS:**
     ```bash
     export OUTPUT_PATH="resultado.txt"
     ```
   * **En Windows (PowerShell):**
     ```powershell
     $env:OUTPUT_PATH="resultado.txt"
     ```

4. **Ejecutar el script:**
   Inicia el programa pasando los datos manualmente o mediante una redirección de archivo:
   ```bash
   python solucion.py
   ```

5. **Formato de Entrada Manual (Ejemplo):**
   Una vez ejecutado, escribe en la consola la cantidad de elementos y las cadenas (presionando Enter por línea):
   ```text
   6
   31415926535897932384626433832795
   1
   3
   10
   3
   5
   ```
   El programa creará un archivo llamado `resultado.txt` con los valores ordenados numéricamente de menor a mayor.

---
