# Prompt para el diseño de este cronograma  utilizando DeepSeek  

Dame el cronograma clase a clase para el curso de "vector geometry_and_linear_algebra" de acuerdo al programa que te adjunto y la secuencia sobre algebra lineal para ciencia de datos seguida por Aurélien Géron en: https://github.com/ageron/handson-ml3/blob/main/math_linear_algebra.ipynb y en https://github.com/ageron/handson-ml3/blob/main/tools_numpy.ipynb. Por favor ten en cuenta para el diseño de este cronograma que: 1. el curso es de 64 horas presenciales teóricas; 2. se realizarán 4 parciales de dos horas cada uno para un total de 8 horas de las 64 horas del curso; 3. se realizarán 6 quices de media hora cada uno para un total de 3 horas de las 64 del curso; el curso empieza el martes 5 de agosto de 2025 y cada clase es de 3 horas por semana para un total de 21 clases presenciales en el semestre. Pero dame este cronograma en idioma español.    



# **Cronograma Detallado: Vector Geometry and Linear Algebra**

**Universidad de Antioquia - Facultad de Ciencias Agrarias**  
**Campus Caucasia - 2025-2**  
**Horario:** Martes 2:00 PM - 5:00 PM (3 horas semanales)  
**Total horas presenciales:** 64 horas (16 semanas)  
**Inicio:** Martes 5 de agosto de 2025  
**Finalización:** Martes 25 de noviembre de 2025  

---

## **Estructura General**
- **16 sesiones** (4 horas cada una, divididas en: 1h teoría, 2h práctica, 1h evaluación/quices)  
- **4 parciales** (integrados en las clases, 2 horas cada uno)  
- **6 quices** (30 minutos cada uno, durante las clases)  
- **Proyectos aplicados** (basados en 
  * [los notebooks de Géron](https://github.com/ageron/handson-ml3/blob/main/tools_numpy.ipynb) y datasets agrícolas)  

---

## **Cronograma por Semanas**

### **Módulo 1: Fundamentos de Álgebra Vectorial**  
*(Semanas 1-4, basado en Capítulos 1-3 del material de Géron)*  

| **Sem** | **Fecha**       | **Contenidos**                                                                 | **Actividades/Evaluación**                                                                 |  
|---------|-----------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|  
| **1**   | 5 ago 2025      | - Vectores en $\mathbb{R}^2$ y $\mathbb{R}^3$: definición y operaciones.<br>- Normas y producto punto.<br>- Aplicación: Análisis de parcelas agrícolas. | - **Quiz 1:** Propiedades vectoriales.<br>- **Práctica:** Visualización con `matplotlib` (datos de Agronet). |  
| **2**   | 12 ago 2025     | - Matrices: representación, suma y multiplicación.<br>- Sistemas de coordenadas en drones agrícolas. | - **Práctica:** Operaciones matriciales con NumPy (datos climáticos IDEAM). |  
| **3**   | 19 ago 2025     | - Transformaciones lineales: rotación, escalado.<br>- Caso aplicado: Ajuste de imágenes satelitales. | - **ABP Inicio:** Diseño de herramienta para mapeo de cultivos. |  
| **4**   | 26 ago 2025     | - **Parcial 1** (Vectores y matrices).<br>- **Entrega ABP 1:** Visualización de parcelas con Plotly. | - Retroalimentación con cooperativas arroceras. |  

---

### **Módulo 2: Sistemas Lineales y Optimización**  
*(Semanas 5-8, basado en Capítulos 4-6 de Géron)*  

| **Sem** | **Fecha**       | **Contenidos**                                                                 | **Actividades/Evaluación**                                                                 |  
|---------|-----------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|  
| **5**   | 2 sep 2025      | - Sistemas $Ax = b$: interpretación geométrica.<br>- Métodos de solución (eliminación gaussiana).<br>- Aplicación: Balance de nutrientes en suelos. | - **Quiz 2:** Resolución de sistemas.<br>- **Práctica:** Uso de `scipy.linalg.solve`. |  
| **6**   | 9 sep 2025      | - Matriz inversa y determinantes.<br>- Caso: Optimización de mezclas de fertilizantes. | - **Práctica:** Simulación con datos reales de Agrosavia. |  
| **7**   | 16 sep 2025     | - Factorización LU.<br>- Aplicación: Predicción de rendimientos con variables climáticas. | - **ABP Avance:** Modelo de optimización de riego. |  
| **8**   | 23 sep 2025     | - **Parcial 2** (Sistemas lineales).<br>- **Entrega ABP 2:** Informe técnico + código GitHub. | - Validación con ingenieros agrónomos. |  

---

### **Módulo 3: Descomposición Matricial y Aplicaciones**  
*(Semanas 9-12, basado en Capítulos 7-9 de Géron)*  

| **Sem** | **Fecha**       | **Contenidos**                                                                 | **Actividades/Evaluación**                                                                 |  
|---------|-----------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|  
| **9**   | 30 sep 2025     | - Valores y vectores propios.<br>- Caso: Estabilidad de suelos en pendientes. | - **Quiz 3:** Cálculo con `numpy.linalg.eig`. |  
| **10**  | 7 oct 2025      | - Descomposición SVD.<br>- Aplicación: Compresión de imágenes multiespectrales. | - **Práctica:** Análisis de imágenes de drones (dataset SIATA). |  
| **11**  | 14 oct 2025     | - PCA para reducción de dimensionalidad.<br>- Detección de estrés hídrico. | - **Quiz 4:** Interpretación de componentes principales. |  
| **12**  | 21 oct 2025     | - **Parcial 3** (Descomposiciones matriciales).<br>- **Entrega ABP 3:** PCA aplicado a cultivos. | - Socialización con agricultores. |  

---

### **Módulo 4: Integración y Proyecto Final**  
*(Semanas 13-16, integración de contenidos)*  

| **Sem** | **Fecha**       | **Contenidos**                                                                 | **Actividades/Evaluación**                                                                 |  
|---------|-----------------|--------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------|  
| **13**  | 28 oct 2025     | - Repaso de conceptos clave.<br>- Tutorías para proyecto final. | - **Práctica:** Debugging colaborativo en GitHub. |  
| **14**  | 4 nov 2025      | - Integración de herramientas: NumPy, SciPy, Pandas.<br>- Caso: Análisis integral de finca modelo. | - **Quiz 5:** Flujo de trabajo con datos reales. |  
| **15**  | 18 nov 2025     | - **Parcial 4** (Evaluación integral).<br>- Revisión de portafolios GitHub. | - **Entrega ABP 4:** Solución tecnológica para cooperativa. |  
| **16**  | 25 nov 2025     | - **Exposición Final:** Presentación de proyectos ante comunidad académica y socios agrícolas.<br>- Cierre y reflexión IAE. | - Autoevaluación y rúbricas de impacto social. |  

---

## **Recursos Clave por Módulo**
- **GitHub de Géron:**  
  - [Álgebra Lineal para ML](https://github.com/ageron/handson-ml3/blob/main/math_linear_algebra.ipynb)  
  - [NumPy para Ciencia de Datos](https://github.com/ageron/handson-ml3/blob/main/tools_numpy.ipynb)  
- **Datasets:**  
  - [Agronet](https://www.agronet.gov.co) (rendimientos agrícolas)  
  - [IDEAM](https://www.ideam.gov.co) (datos climáticos)  

---

## **Evaluaciones Sumativas**
| **Evaluación**       | **Fecha**               | **Contenido**                                                                 |  
|-----------------------|-------------------------|-------------------------------------------------------------------------------|  
| Parcial 1             | 26 de agosto 2025       | Vectores, matrices y transformaciones lineales.                               |  
| Parcial 2             | 23 de septiembre 2025   | Sistemas lineales y optimización.                                             |  
| Parcial 3             | 21 de octubre 2025      | Descomposición matricial (SVD, PCA).                                          |  
| Parcial 4             | 18 de noviembre 2025    | Integración de conceptos en proyecto agrícola.                                |  

---

### **Notas:**  
1. Todas las prácticas usan Python (Jupyter Notebook) con bibliotecas como NumPy, Matplotlib y SciPy.  
2. Los proyectos ABP se desarrollan en equipos multidisciplinares (estudiantes + agricultores).  
3. El cronograma sigue la secuencia pedagógica de Géron, adaptada al contexto agrícola del Bajo Cauca.  

**"Las matemáticas no son abstractas cuando se usan para predecir una cosecha o salvar un cultivo"**