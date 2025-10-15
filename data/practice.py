import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

df = pd.read_csv("C:/Users/cheta/Downloads/DWM/DWM/insta.csv")

X = df[["Instagram visit score", "Spending_rank(0 to 100)"]]

kmeans = KMeans(n_clusters= 3, random_state=42, n_init=10 )
df["Cluster"] = kmeans.fit_predict(X)

plt.figure(figsize=(8,6))
plt.scatter(X.iloc[:,0], X.iloc[:,1], c=df["Cluster"], cmap="viridis", s =50)
plt.scatter(kmeans.cluster_centers_[:,0], kmeans.cluster_centers_[:,1],
            c="red", marker="X", s=200, label="Centroids")
plt.xlabel("Instagram visit score")
plt.ylabel("Speanding Rank")
plt.title("Kmeans clustering on insta.csv")
plt.legend()
plt.show()