
# Módulo 1 — Fundamentos de Visión por Computador para Ingeniería Agropecuaria

## Desarrollo conceptual (resumen)
Este módulo introduce los conceptos básicos para trabajar con imágenes digitales en aplicaciones agropecuarias: adquisición, representación, preprocesado simple, extracción de características y visualización. El enfoque es práctico y orientado a Jupyter notebooks, usando OpenCV, NumPy, pandas, Matplotlib e ipywidgets para aprender traduciendo entre registros semióticos (visual, simbólico y computacional).

### Conceptos clave
- **Imagen digital**: matriz de píxeles; cada píxel puede representarse como un vector en \\(\\mathbb{R}^3\\) (RGB) o como valor escalar en escala de grises.
- **Espacio de color**: RGB, BGR (OpenCV), HSV; conversión entre espacios y utilidad para segmentación.
- **Geometría vectorial en imágenes**: píxeles como vectores, norma, producto punto, distancia euclidiana (usada en clustering y búsqueda de similitud).
- **Operaciones puntuales**: umbral, escala de grises, transformaciones lineales (contraste/brightness).
- **Filtrado espacial**: suavizado (gaussiano), detección de bordes (Sobel, Canny).
- **Segmentación simple**: umbral global/adaptativo, clustering k-means en color.
- **Medidas simplificadas para agricultura**: índices espectrales simulados (cuando no hay NIR se puede aproximar), detección de manchas foliares con segmentación de color, conteo de objetos con contornos.
- **Representación y registros (Duval)**: paso desde la imagen visual al vector numérico (arrays), a la representación algorítmica (código) y a la explicación verbal/manual.

### Herramientas propuestas
- OpenCV (`cv2`)
- NumPy
- pandas (para tablas de metadatos)
- Matplotlib (visualización)
- ipywidgets (interactividad)
- scikit-learn (k-means) — opcional

---

## Actividades y scripts (uso en Jupyter / VS Code - celdas delimitadas con `# %%`)

Los scripts incluidos en este paquete están pensados para abrirse en VS Code como "Python Interactive" o como notebook (cada `# %%` define una celda).

Archivos incluidos:
- `activities_module1.py` : script principal con actividades y funciones.
- `README.md` (este archivo).
