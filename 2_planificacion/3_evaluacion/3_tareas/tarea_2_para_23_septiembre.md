Para todos por parejas preparar la exposición del Ejemplo de la págian 499 del Grosmann  

# Tarea de construcción de un modelo de transformación lineal que convuerta vectores de producción en vectores de materia prima necesaria para obtener tal producción  

## Transformación de un vector de producción en un vector de materia prima (Página 499 del Álgebra Lineal de Grosmann.)  

Un fabricante elabora cuatro tipos de productos distintos, de los cuales cada uno requiere tres tipos de materiales. Se identifican los cuatro productos como P1, P2, P3 y P4, y a los materiales por R1, R2 y R3. La tabla siguiente muestra el número de unidades de cada materia prima que se requieren para fabricar una unidad de cada producto.  



||P1|P2|P3|P4|
|-|-|-|-|-|
|R1|2|1|3|4|
|R2|4|2|2|1|
|R3|3|3|1|2|  

Surge una pregunta natural: si se produce cierto número de los cuatro productos, ¿cuántas
unidades de cada material se necesitan? Sean p1, p2, p3 y p4 el número de artículos fabricados de
los cuatro productos, y sean r1, r2 y r3 el número de unidades necesario de los tres materiales.
Entonces se define  

$$ p = \begin{pmatrix}P_{1} \\ P_{2} \\ P_{3} \\ P_{4} \end{pmatrix}, \quad \quad  r = \begin{pmatrix} R_{1} \\ R_{2} \\ R_{3} \end{pmatrix} \quad \quad A = \begin{pmatrix} 2 & 1 & 3 & 4 \\ 4 & 2 & 2 & 1 \\ 3 & 3 & 1 & 2 \end{pmatrix}  $$  

Por ejemplo, suponga que $\begin{pmatrix} 10 \\ 30 \\ 20 \\ 50 \end{pmatrix}$ ¿Cuántas unidades de R1 se necesitan para producir estos números de unidades de los cuatro productos?   


En general se ve que  

$$ \begin{pmatrix} 2 & 1 & 3 & 4 \\ 4 & 2 & 2 & 1 \\ 3 & 3 & 1 & 2 \end{pmatrix}\begin{pmatrix}P_{1} \\ P_{2} \\ P_{3} \\ P_{4} \end{pmatrix} = \begin{pmatrix} R_{1} \\ R_{2} \\ R_{3} \end{pmatrix} $$  

$$A\mathbf{p} = \mathbf{r}$$  

Esto se puede ver de otra manera. Si a p se le conoce como el vector de producción y a r como
el vector de materia prima, se define la función T por r 5 T(p) 5 Ap. Esto es, T es la función
que “transforma” el vector de producción en el vector de materia prima y se hace mediante la
multiplicación de matrices ordinaria. Como se verá, esta función es también una transformación lineal.