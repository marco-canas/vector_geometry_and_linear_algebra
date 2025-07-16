# geometria_vectorial  

Promp de diseño de este curso:   

Dame un programa preliminar de enseñanza del álgebra lineal para el programa de Ingeniería agropecuaria de la Facultad de Ciencias Agrarias de la Universidad de Antioquia en el Campus Caucasia para el semestre 2025-2 con un enfoque hacia la ciencia de datos que le permita al futuro ingeniero optimizar los procesos agrícolas. Donde busque brindar todo lo que Aurelien Geron considera necesario para hacerse un científico de datos en su libro Hans On Machine Learning with sklearn, keras and tensorflow https://github.com/ageron/handson-ml3  

# **Programa Preliminar de Álgebra Lineal para Ingeniería Agropecuaria con Enfoque en Ciencia de Datos**  
**Universidad de Antioquia - Facultad de Ciencias Agrarias, Campus Caucasia**  
**Semestre 2025-2**  

---

## **1. Fundamentación**  
Este curso integra **álgebra lineal** con **ciencia de datos aplicada a la agricultura**, siguiendo los lineamientos de Aurélien Géron en *"Hands-On Machine Learning"* . Los contenidos se orientan a:  
- Optimizar procesos agropecuarios mediante modelos predictivos (ej: rendimiento de cultivos, gestión de recursos).  
- Desarrollar habilidades en **Python**, **Scikit-learn**, y **TensorFlow** para análisis de datos agrícolas.  

---

## **2. Objetivos**  
### **2.1. Objetivos Generales**  
- Aplicar conceptos de álgebra lineal (matrices, vectores, descomposiciones) en problemas agrícolas.  
- Implementar algoritmos de machine learning (*Random Forest*, *SVM*) para optimización de cultivos.  

### **2.2. Objetivos Específicos**  
- Modelar sistemas de riego usando **regresión lineal múltiple**.  
- Clasificar plagas con **PCA** y **k-means** (reducción de dimensionalidad).  
- Predecir rendimientos con **redes neuronales** (TensorFlow/Keras).  

---

## **3. Contenidos por Módulos**  
### **Módulo 1: Fundamentos de Álgebra Lineal**  
- **Temas:**  
  - Vectores y matrices en Python (`NumPy`).  
  - Sistemas de ecuaciones lineales para balance nutricional de suelos.  
  - Transformaciones lineales en imágenes de cultivos (OpenCV).  
- **Actividad:** Simulación de fertilización óptima con `np.linalg.solve()`.  

### **Módulo 2: Descomposiciones Matriciales**  
- **Temas:**  
  - **SVD** para análisis de sensores agrícolas.  
  - **Autovalores/Autovectores** en patrones climáticos.  
- **Actividad:** Predicción de sequías usando PCA (`sklearn.decomposition`).  

### **Módulo 3: Machine Learning Agrícola**  
- **Temas:**  
  - Regresión logística para diagnóstico de enfermedades en plantas.  
  - Árboles de decisión para gestión de inventarios.  
- **Dataset:** MNIST adaptado a hojas de cultivo (clasificación de estrés hídrico).  

### **Módulo 4: Redes Neuronales**  
- **Temas:**  
  - Perceptrones para monitoreo de crecimiento vegetal.  
  - CNN en imágenes multiespectrales (drones agrícolas).  
- **Herramientas:** `TensorFlow` + `Keras`.  

---

## **4. Metodología**  
- **Aprendizaje Basado en Proyectos (ABP):**  
  - **Proyecto 1:** Optimización de riego con matrices de covarianza.  
  - **Proyecto 2:** Clasificación de suelos usando SVM y kernels.  
- **Herramientas:**  
  - **Cocodrilo Clips:** Circuitos lógicos para sensores de humedad .  
  - **Jupyter Notebooks:** Tutoriales interactivos con `ipywidgets`.  

---

## **5. Evaluación**  
| **Componente**          | **Peso** | **Herramientas**                |  
|--------------------------|----------|----------------------------------|  
| Talleres prácticos       | 30%      | Python (Pandas, Matplotlib)      |  
| Proyecto final           | 40%      | Scikit-learn, TensorFlow         |  
| Quiz teóricos            | 20%      | SymPy (ej: $\text{SVD} = U\Sigma V^T$) |  
| Participación            | 10%      | Foros en GitHub Classroom        |  

**Ejemplo de Quiz:**  
*"¿Cómo justificarías que la matriz de confusión de tu modelo de plagas es razonable?"*  

---

## **6. Recursos**  
- **Libro base:** *"Hands-On Machine Learning"* (Géron) [GitHub](https://github.com/ageron/handson-ml3).  
- **Datasets:**  
  - [AgroClimatic Data](https://rproject-udea.netlify.app/) (UdeA) .  
  - MNIST modificado para agricultura.  

---

## **7. Cronograma (Semestral)**  
| **Semana** | **Tema**                          | **Tecnología**           |  
|------------|------------------------------------|--------------------------|  
| 1-4        | Vectores y sistemas lineales       | NumPy                    |  
| 5-8        | PCA y clustering                   | Scikit-learn             |  
| 9-12       | Redes neuronales                   | TensorFlow               |  
| 13-16      | Proyecto integrador                | Todo lo anterior         |  

Horario: Martes de 2 a 5 PM. 

Empezamos el curso el 5 de Agosto. 
---

## **8. Habilidades Blandas**  
- **Trabajo en equipo:** Desarrollo colaborativo en GitHub.  
- **Comunicación:** Presentación de resultados a agricultores locales.  

--- 

**Nota:** Este programa alinea los contenidos con los grupos de investigación UdeA como [*"Analítica e Investigación para la Toma de Decisiones (ALIADO)"*](https://www.udea.edu.co/wps/portal/udea/web/inicio/investigacion/grupos-investigacion/ingenieria-tecnologia/aliado) , asegurando pertinencia en el sector agropecuario.
