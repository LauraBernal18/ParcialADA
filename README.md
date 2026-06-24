# Parcial Práctico

Este repositorio contiene la solución en Python para el problema **"Big Sorting"** y **"Insertion Sort Advanced Analysis"** de HackerRank, correspondiente a la sección del parcial práctico.

## Big Sorting

### Cómo poner a funcionar el programa

Existen dos formas de ejecutar y probar este código:

#### Opción 1: Ejecución Directa en HackerRank (Recomendado)
1. Copia el código fuente completo del archivo `solucion.py` de este repositorio.
2. Ve al problema [Big Sorting en HackerRank](https://hackerrank.com).
3. Selecciona **Python 3** como lenguaje en el editor de HackerRank.
4. Pega el código y presiona el botón **"Submit Code"**. Pasará todos los casos de prueba inmediatamente.

#### Opción 2: Ejecución Local en Visual Studio Code (Recomendado)

Sigue estos pasos para clonar el proyecto y ejecutarlo directamente en tu entorno gráfico:

1. **Clonar el repositorio desde VS Code:**
   * Abre Visual Studio Code.
   * Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en Mac) para abrir la paleta de comandos.
   * Escribe **Git: Clone** y presiona Enter.
   * Pega el enlace de este repositorio: `https://github.com/LauraBernal18/ParcialADA.git` y selecciona la carpeta en tu computadora donde deseas guardarlo.

2. **Abrir el proyecto:**
   * Cuando aparezca la notificación en la esquina inferior derecha, haz clic en **Open** (Abrir) para cargar el espacio de trabajo.

3. **Ejecutar el programa de Python:**
   * Abre el archivo `solucion.py` desde el explorador de archivos izquierdo.
   * Asegúrate de tener instalada la extensión oficial de Python en tu VS Code.
   * Haz clic en el botón de **Play** (icono de triángulo arriba a la derecha) o presiona clic derecho sobre el código y selecciona **Run Python File in Terminal** (Ejecutar archivo de Python en la terminal).

4. **Ingreso de datos de prueba:**
   * La terminal integrada de VS Code se abrirá en la parte inferior esperando la entrada de datos.
   * Copia y pega el siguiente bloque completo de una sola vez en la terminal y presiona **Enter**:
     ```text
        6
        31415926535897932384626433832795
        1
        3
        10
        3
        5
     ```
   
5. **Verificar el resultado:**
   * Verás un mensaje de éxito en la terminal confirmando que el programa terminó.
   * Automáticamente aparecerá un nuevo archivo llamado `resultado.txt` en tu explorador de VS Code con la lista de números perfectamente ordenada.

## "Insertion Sort Advanced Analysis"

Para este ejercicio se implementó una solución de complejidad O(n²) basada en el conteo directo de inversiones mediante dos ciclos anidados. Esta simplicidad permite comprender de manera clara la relación entre las inversiones del arreglo y los desplazamientos (shifts) realizados por el algoritmo Insertion Sort. Sin embargo, esta solución genera un error de Time Limit Exceeded en algunos casos de prueba. Por esta razón, la solución aceptada en HackerRank utiliza algoritmos más eficientes, como Merge Sort con conteo de inversiones, cuya complejidad es O(n log n) por lo tanto esta solucion solo podra ser implementada en Visual Studio Code, donde se pueden utilizar conjuntos de datos pequeños o medianos sin afectar significativamente el rendimiento.

### Cómo poner a funcionar el programa

### Ejecución Local en Visual Studio Code (Recomendado)

Sigue estos pasos para clonar el proyecto y ejecutarlo directamente en tu entorno gráfico:

1. **Clonar el repositorio desde VS Code:**
   * Abre Visual Studio Code.
   * Presiona `Ctrl + Shift + P` (o `Cmd + Shift + P` en Mac) para abrir la paleta de comandos.
   * Escribe **Git: Clone** y presiona Enter.
   * Pega el enlace de este repositorio: `https://github.com/LauraBernal18/ParcialADA.git` y selecciona la carpeta en tu computadora donde deseas guardarlo.

2. **Abrir el proyecto:**
   * Cuando aparezca la notificación en la esquina inferior derecha, haz clic en **Open** (Abrir) para cargar el espacio de trabajo.

3. **Ejecutar el programa de Python:**
   * Abre el archivo `solucion2.py` desde el explorador de archivos izquierdo.
   * Asegúrate de tener instalada la extensión oficial de Python en tu VS Code.
   * Haz clic en el botón de **Play** (icono de triángulo arriba a la derecha) o presiona clic derecho sobre el código y selecciona **Run Python File in Terminal** (Ejecutar archivo de Python en la terminal).

4. **Ingreso de datos de prueba:**
   * La terminal integrada de VS Code se abrirá en la parte inferior esperando la entrada de datos.
   * Copia y pega el siguiente bloque completo de una sola vez en la terminal y presiona **Enter**:
     ```text
       2  
       5  
       1 1 1 2 2  
       5  
       2 1 3 1 2
     ```
   
5. **Verificar el resultado:**
   * Verás un mensaje de éxito en la terminal confirmando que el programa terminó.
   * Automáticamente aparecerá un nuevo archivo llamado `resultado2.txt` en tu explorador de VS Code con la lista de números perfectamente ordenada.
