"""
Modelo no supervisado para analizar patrones de uso del transporte masivo.

Entrada:
    dataset_transporte_muestra.csv

Salida:
    resultados_clustering.csv
    grafico_clusters.png

Modelo:
    K-Means con estandarización de variables y evaluación mediante
    coeficiente de silueta.
"""

from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.decomposition import PCA

BASE = Path(__file__).resolve().parent
ARCHIVO_DATOS = BASE / "dataset_transporte_muestra.csv"
ARCHIVO_RESULTADOS = BASE / "resultados_clustering.csv"
ARCHIVO_GRAFICO = BASE / "grafico_clusters.png"

# 1. Cargar datos
df = pd.read_csv(ARCHIVO_DATOS, encoding="utf-8-sig")

# 2. Seleccionar variables numéricas para el aprendizaje no supervisado
variables = [
    "entradas_promedio",
    "salidas_promedio",
    "ocupacion_pct",
    "tiempo_espera_min",
    "transbordos_promedio",
    "distancia_km"
]

X = df[variables].copy()

# 3. Estandarizar
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Probar diferentes cantidades de clusters
silhouette_por_k = {}

for k in range(2, 6):
    modelo_tmp = KMeans(n_clusters=k, random_state=42, n_init=10)
    etiquetas_tmp = modelo_tmp.fit_predict(X_scaled)
    silhouette_por_k[k] = silhouette_score(X_scaled, etiquetas_tmp)

mejor_k = max(silhouette_por_k, key=silhouette_por_k.get)

# 5. Entrenar modelo final
modelo = KMeans(n_clusters=mejor_k, random_state=42, n_init=10)
df["cluster"] = modelo.fit_predict(X_scaled)

# 6. Evaluación
silhouette_final = silhouette_score(X_scaled, df["cluster"])

print("==========================================")
print(" MODELO NO SUPERVISADO - TRANSPORTE MASIVO")
print("==========================================")
print(f"Registros analizados: {len(df)}")
print(f"Variables utilizadas: {len(variables)}")
print(f"Mejor número de clusters: {mejor_k}")
print(f"Coeficiente de silueta: {silhouette_final:.4f}")
print("\nSilueta por cantidad de clusters:")
for k, score in silhouette_por_k.items():
    print(f"  k={k}: {score:.4f}")

# 7. Perfil de cada cluster
perfil = df.groupby("cluster")[variables].mean().round(2)
print("\nPerfil promedio de los clusters:")
print(perfil)

# 8. Guardar resultados
df.to_csv(ARCHIVO_RESULTADOS, index=False, encoding="utf-8-sig")

# 9. Reducir a dos dimensiones para visualizar
pca = PCA(n_components=2, random_state=42)
componentes = pca.fit_transform(X_scaled)

plt.figure(figsize=(9, 6))
plt.scatter(componentes[:, 0], componentes[:, 1], c=df["cluster"])
plt.title("Agrupación de estaciones/franjas - K-Means")
plt.xlabel("Componente principal 1")
plt.ylabel("Componente principal 2")
plt.tight_layout()
plt.savefig(ARCHIVO_GRAFICO, dpi=150)
plt.close()

print(f"\nResultados guardados en: {ARCHIVO_RESULTADOS.name}")
print(f"Gráfico guardado en: {ARCHIVO_GRAFICO.name}")
