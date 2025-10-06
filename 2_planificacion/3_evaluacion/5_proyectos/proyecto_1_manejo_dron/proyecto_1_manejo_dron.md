

Responsables para el sábado 4 de octubre 2025:  

1. Rivaldo José
2. Yanine
3. Erlinda
4. Gabriela
5. Marisol. 
6. Mariana. ¿Cómo se obtienen los datos del Drone? 
   

   # Tareas para todos 

   1. Estuidiar el manual del Drone para el sábado 20 de Septiembre. 
   2. Diseñar una guia de exploración para el manejo del dron
7.  

# Prompt para el diseño de esta Guía Didáctica de exploración del Dron  

Diséñame, por favor, una guía didáctica para aprender a manejar el dron que te indico en el manual que te adjunto. Pero te pido, por favor, que esta guía didáctica lleve a mis estudiantes a vincular la Geometría Vectorial y el Álgebra Lineal a las Ciencias Agrarias de los estudiantes de Ingeniería Agropecuaria en el Bajo Cauca Antioqueño.   


Este es un diseño de una **guía didáctica** que no solo enseña a manejar el dron, sino que también conecta su uso con **Geometría Vectorial** y **Álgebra Lineal**, orientada a la **Ingeniería Agropecuaria en el Bajo Cauca Antioqueño**.

---

# Guía Didáctica: Manejo del Drone Tello y Aplicaciones de la Geometría Vectorial en Ciencias Agrarias

### 1. Propósito formativo

Que los estudiantes de **Ingeniería Agropecuaria** comprendan el manejo seguro y básico del dron **Tello** como herramienta para el monitoreo agrícola, vinculando su control con conceptos de **geometría vectorial y álgebra lineal**, fundamentales para la modelación y análisis en ciencias agrarias.

---

### 2. Secuencia didáctica

#### Fase 1: Familiarización con el dron

* **Actividad práctica**:

  * Identificar en el dron Tello sus partes: hélices, cámara, sistema de posicionamiento visual, batería.
  * Encender, conectar vía Wi-Fi con la aplicación Tello y realizar el primer despegue automático.
* **Conexión matemática**:

  * Representar la posición inicial del dron como el **vector nulo** en un sistema de coordenadas cartesianas.
  * Establecer el plano $xy$ como campo de vuelo horizontal y el eje $z$ como altitud.

---

#### Fase 2: Control manual y vectores de desplazamiento

* **Actividad práctica**:

  * Usar los joysticks virtuales (modo 2):

    * Palanca izquierda: altitud (eje $z$) y giro (rotación en el plano $xy$).
    * Palanca derecha: traslación en $x$ e $y$.
* **Conexión matemática**:

  * Cada movimiento del dron es un **vector de desplazamiento**:

    $$
    \vec{d} = (x, y, z)
    $$
  * Proponer a los estudiantes operaciones vectoriales:

    * **Suma de vectores**: secuencia de trayectorias.
    * **Magnitud del vector**: distancia recorrida.
    * **Producto escalar**: relación entre la dirección del dron y la del viento.

---

#### Fase 3: Vuelo planificado y álgebra lineal

* **Actividad práctica**:

  * Programar trayectorias rectilíneas (líneas de cultivo).
  * Definir puntos de interés (nodos de observación) y desplazarse entre ellos.
* **Conexión matemática**:

  * Representar posiciones como **vectores columna**:

    $$
    P = \begin{bmatrix} x \\ y \\ z \end{bmatrix}
    $$
  * Aplicar **matrices de rotación** para giros de 90° o 180°.
  * Usar **sistemas de ecuaciones lineales** para modelar vuelos en cuadrículas agrícolas.

---

#### Fase 4: Aplicaciones agropecuarias

* **Monitoreo de cultivos**:

  * Tomar imágenes aéreas para analizar uniformidad del cultivo.
  * Relacionar las trayectorias del dron con mallas vectoriales en el terreno.
* **Estimación de áreas**:

  * Usar la proyección del vuelo sobre el plano $xy$ para calcular áreas de parcelas.
  * Aplicar determinantes para calcular áreas de polígonos definidos por puntos de observación.
* **Modelación ambiental**:

  * Asociar el vector velocidad del dron con la dirección y magnitud de vientos locales en Caucasia.

---

### 3. Evaluación

* **Práctica**:

  * Los estudiantes deben realizar un vuelo en cuadrícula sobre una zona delimitada (representando un cultivo).
  * Registrar los vectores de desplazamiento y reconstruir la trayectoria en papel o software.
* **Conceptual**:

  * Resolver ejercicios de álgebra lineal (rotaciones, combinaciones lineales) asociados a trayectorias de vuelo.

---

### 4. Reflexión final

El dron Tello se convierte en un **laboratorio volante** donde los estudiantes integran teoría matemática (vectores y matrices) con la práctica agraria (monitoreo de cultivos, análisis de áreas, reconocimiento de patrones). Esto refuerza el **pensamiento matemático aplicado** en la ingeniería agropecuaria del Bajo Cauca.

---

¿Quieres que te prepare esta guía también en **formato de presentación tipo diapositivas (PowerPoint o Canva-like)** para que tus estudiantes la tengan visualmente más atractiva en clase?  

# Tareas 

* Consultar sobre el giroscopio y su uso en drones.
* Consultar sobre el acelerómetro y su uso en drones.


# Sitemas de medida para el Dron  

Te explico:

## 📏 Sistema Métrico (o Sistema Internacional de Unidades – SI)

Es el sistema de medida más usado en el mundo, basado en **múltiplos de 10**. Sus características principales:

* **Unidad de longitud**: **metro (m)**
* **Unidad de masa**: **kilogramo (kg)**
* **Unidad de volumen**: **litro (L)**
* **Unidad de temperatura**: **grado Celsius (°C)**
* **Unidad de energía**: **joule (J)**

Lo más importante es que es **decimal**, es decir, pasar de una unidad a otra solo requiere multiplicar o dividir entre 10, 100, 1000, etc.
👉 Ejemplo: 1 km = 1000 m, 1 L = 1000 mL.

Se usa en **casi todos los países** (incluido Colombia).

---

## 📐 Sistema de Medidas de Estados Unidos (US customary system)

Este sistema **no es decimal** y está basado en unidades históricas de origen inglés. Algunas características:

* **Unidad de longitud**: **pulgada (inch, in), pie (foot, ft), yarda (yard, yd), milla (mile, mi)**

  * 1 ft = 12 in, 1 yd = 3 ft, 1 mi = 1760 yd.
* **Unidad de masa/peso**: **onza (oz), libra (lb), tonelada corta (ton)**

  * 1 lb = 16 oz, 1 ton (EE.UU.) = 2000 lb.
* **Unidad de volumen**: **pinta (pint), cuarto (quart), galón (gallon)**

  * 1 gallon = 4 quarts = 8 pints.
* **Unidad de temperatura**: **grado Fahrenheit (°F)**
* **Unidad de energía**: **BTU (British Thermal Unit)**

Este sistema se usa principalmente en **Estados Unidos, Liberia y Myanmar**.

---

## 🔄 Comparación entre los dos sistemas

| Magnitud    | Sistema Métrico (SI)      | Sistema de EE.UU.            |
| ----------- | ------------------------- | ---------------------------- |
| Longitud    | metro (m), km             | pulgada, pie, yarda, milla   |
| Masa/Peso   | gramo (g), kilogramo (kg) | onza, libra, tonelada corta  |
| Volumen     | litro (L), mililitro (mL) | pinta, cuarto, galón         |
| Temperatura | grados Celsius (°C)       | grados Fahrenheit (°F)       |
| Conversión  | Decimal, múltiplos de 10  | Fracciones (12, 3, 16, etc.) |
| Uso         | Mundial                   | EE.UU., Liberia, Myanmar     |

---

## 🌡️ Ejemplos de conversión

* **Temperatura**:

  * 0 °C = 32 °F
  * 100 °C = 212 °F

* **Longitud**:

  * 1 in = 2.54 cm
  * 1 mi ≈ 1.609 km

* **Masa/Peso**:

  * 1 kg ≈ 2.204 lb

* **Volumen**:

  * 1 L ≈ 0.264 galones (US)

---

📌 En resumen:
El **sistema métrico** es más simple y universal porque es decimal. El **sistema estadounidense** es más complejo porque no sigue múltiplos de 10, pero sigue siendo parte de la cultura y la vida cotidiana en EE.UU.

¿Quieres que te prepare una **tabla de equivalencias rápidas** que tus estudiantes puedan usar como referencia práctica en clase?


# Trabajo de aprendizaje en Manejo del Dron que llegó el 4 de octubre de 2025  

1. Estamos en la etapa de carga y encendido.  
2. 