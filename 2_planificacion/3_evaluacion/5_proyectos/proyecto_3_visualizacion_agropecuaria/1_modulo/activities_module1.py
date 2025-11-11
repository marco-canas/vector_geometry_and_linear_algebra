
# activities_module1.py
# Módulo 1 - Actividades y funciones para Jupyter (OpenCV para Ing. Agropecuaria)
# Cada bloque `# %%` está pensado como una celda independiente en VS Code / Jupyter.

# Requisitos (instalar si no están):
# pip install numpy pandas matplotlib opencv-python ipywidgets scikit-learn

# %% [markdown]
# # Actividad 1 - Cargar y visualizar una imagen agrícola
# Objetivos:
# - Practicar la lectura de una imagen con OpenCV.
# - Entender representación RGB vs BGR (OpenCV usa BGR por defecto).
# - Mostrar la imagen con Matplotlib (RGB correcto).

# %%
import cv2
import numpy as np
import matplotlib.pyplot as plt
from IPython.display import display
import os

def load_image_rgb(path):
    """Carga con OpenCV y devuelve imagen en RGB (float 0-1)."""
    img_bgr = cv2.imread(path, cv2.IMREAD_COLOR)
    if img_bgr is None:
        raise FileNotFoundError(f"Imagen no encontrada: {path}")
    img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
    return img_rgb.astype(np.float32)/255.0

def show_image(img, title="Imagen", figsize=(8,6)):
    plt.figure(figsize=figsize)
    plt.imshow(img)
    plt.title(title)
    plt.axis('off')
    plt.show()

# %% ejemplo de uso (descomentar y colocar la ruta local)
# img = load_image_rgb("ruta/a/tu/imagen.jpg")
# show_image(img, "Imagen agrícola")

# %% [markdown]
# # Actividad 2 - Píxel como vector en R^3 y estadísticas básicas
# Objetivos:
# - Mostrar que cada píxel es un vector 3D (R,G,B), cálculo de media y covarianza.
# - Presentar histograma de canales.

# %%
import pandas as pd

def pixel_statistics(img):
    """Devuelve media y covarianza de los vectores píxel en RGB."""
    h,w,_ = img.shape
    pixels = img.reshape(-1,3)
    mean = pixels.mean(axis=0)
    cov = np.cov(pixels, rowvar=False)
    return mean, cov

def plot_histograms(img, bins=64):
    plt.figure(figsize=(8,4))
    colors = ['r','g','b']
    labels = ['R','G','B']
    for i,c,l in zip(range(3), colors, labels):
        plt.hist(img[:,:,i].ravel(), bins=bins, color=c, alpha=0.5, label=l)
    plt.legend()
    plt.title("Histogramas por canal (valores 0-1)")
    plt.show()

# %% [markdown]
# # Actividad 3 - Conversión a escala de grises y filtrado
# - Grayscale, suavizado Gaussiano, detección de bordes (Canny).

# %%
def to_grayscale(img):
    """Convierte imagen RGB (0-1) a escala de grises (0-1)."""
    gray = cv2.cvtColor((img*255).astype(np.uint8), cv2.COLOR_RGB2GRAY)
    return gray.astype(np.float32)/255.0

def gaussian_blur(img_gray, ksize=5, sigma=1.0):
    k = int(ksize)
    return cv2.GaussianBlur((img_gray*255).astype(np.uint8), (k,k), sigma)

def canny_edges(img_gray_uint8, thresh1=100, thresh2=200):
    edges = cv2.Canny(img_gray_uint8, thresh1, thresh2)
    return edges

# %% [markdown]
# # Actividad 4 - Segmentación por color (umbral HSV) y k-means
# - Convertir a HSV y seleccionar rango para detectar verdes (hojas).
# - Alternativa: k-means en espacio Lab o RGB para segmentación no supervisada.

# %%
def segment_hsv(img_rgb, lower_hsv, upper_hsv):
    """Segmenta por rango HSV. img_rgb en 0-1"""
    img_bgr = cv2.cvtColor((img_rgb*255).astype(np.uint8), cv2.COLOR_RGB2BGR)
    hsv = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv, lower_hsv, upper_hsv)
    return mask

from sklearn.cluster import KMeans

def kmeans_segment(img_rgb, k=3, sample=10000, random_state=0):
    h,w,_ = img_rgb.shape
    pixels = (img_rgb.reshape(-1,3)*255).astype(np.uint8)
    if pixels.shape[0] > sample:
        idx = np.random.choice(pixels.shape[0], sample, replace=False)
        sample_pixels = pixels[idx]
    else:
        sample_pixels = pixels
    kmeans = KMeans(n_clusters=k, random_state=random_state).fit(sample_pixels)
    labels = kmeans.predict(pixels)
    segmented = labels.reshape(h,w)
    return segmented, kmeans.cluster_centers_

# %% [markdown]
# # Actividad 5 - Medición simple: estimar área de cobertura foliar
# - A partir de la máscara (segmentación de hojas), calcular porcentaje de píxeles verdes.

# %%
def coverage_percentage(mask):
    """mask: binaria 0/255"""
    total = mask.size
    covered = np.count_nonzero(mask)
    return covered/total*100

# %% [markdown]
# # Actividad 6 - Detección y conteo de objetos (manchas/hojas)
# - Usar contornos en OpenCV para contar objetos y obtener bounding boxes.

# %%
def count_contours(mask, min_area=50):
    """Retorna número de contornos y lista de bounding boxes"""
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    boxes = []
    count = 0
    for c in contours:
        area = cv2.contourArea(c)
        if area >= min_area:
            x,y,w,h = cv2.boundingRect(c)
            boxes.append((x,y,w,h,area))
            count += 1
    return count, boxes

# %% [markdown]
# # Actividad 7 - Interactividad con ipywidgets
# - Slider para ajustar umbral HSV y ver la máscara en tiempo real
# (este bloque funciona mejor en JupyterLab/VS Code con soporte de widgets)

# %%
from ipywidgets import interact, IntSlider, Dropdown

def interactive_hsv_demo(img_rgb):
    # valores iniciales típicos para verde en OpenCV (H 35-85)
    def show(h_low=35, s_low=40, v_low=40, h_high=85, s_high=255, v_high=255):
        lower = np.array([h_low, s_low, v_low])
        upper = np.array([h_high, s_high, v_high])
        mask = segment_hsv(img_rgb, lower, upper)
        plt.figure(figsize=(10,4))
        plt.subplot(1,2,1)
        plt.imshow(img_rgb)
        plt.title("Original")
        plt.axis('off')
        plt.subplot(1,2,2)
        plt.imshow(mask, cmap='gray')
        plt.title("Mascara HSV")
        plt.axis('off')
        plt.show()
    interact(show,
             h_low=IntSlider(35, min=0, max=179),
             s_low=IntSlider(40, min=0, max=255),
             v_low=IntSlider(40, min=0, max=255),
             h_high=IntSlider(85, min=0, max=179),
             s_high=IntSlider(255, min=0, max=255),
             v_high=IntSlider(255, min=0, max=255))

# %% [markdown]
# # Actividad 8 - Exportar resultados y metadatos (pandas)
# - Guardar máscaras, medidas y tablas con pandas.

# %%
import pandas as pd

def save_results_csv(results, filename="results_module1.csv"):
    """results: lista de dicts con metadatos; guarda CSV"""
    df = pd.DataFrame(results)
    df.to_csv(filename, index=False)
    return filename

# %% [markdown]
# # Ejemplo de flujo de trabajo (pipeline)
# 1. Cargar imagen
# 2. Visualizar y calcular estadísticas
# 3. Segmentar (HSV o k-means)
# 4. Calcular cobertura y contar objetos
# 5. Guardar resultados

# %%
def pipeline_example(path):
    img = load_image_rgb(path)
    show_image(img, "Original")
    mean, cov = pixel_statistics(img)
    print("Media RGB:", mean)
    plot_histograms(img)
    gray = to_grayscale(img)
    blurred = gaussian_blur(gray, ksize=5, sigma=1.2)
    edges = canny_edges(blurred, 50, 150)
    plt.figure(figsize=(10,4))
    plt.subplot(1,2,1); plt.imshow(gray, cmap='gray'); plt.title('Gray'); plt.axis('off')
    plt.subplot(1,2,2); plt.imshow(edges, cmap='gray'); plt.title('Edges'); plt.axis('off')
    plt.show()
    # Demo de segmentacion (valores por defecto)
    lower = np.array([35,40,40])
    upper = np.array([85,255,255])
    mask = segment_hsv(img, lower, upper)
    print("Cobertura (%) de máscara verde:", coverage_percentage(mask))
    ccount, boxes = count_contours(mask)
    print("Objetos detectados:", ccount)
    return {"mean": mean, "cov": cov, "coverage": coverage_percentage(mask), "count": ccount}

# %% [markdown]
# # Recomendaciones de entrega
# - Cada estudiante sube un notebook con: código, resultados, imágenes, interpretación y un archivo CSV con resultados.
# - Incluir un pequeño informe (README.md) explicando decisiones de umbral y parámetros.
