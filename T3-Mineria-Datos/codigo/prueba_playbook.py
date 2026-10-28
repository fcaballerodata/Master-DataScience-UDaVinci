import numpy as np, pandas as pd
from sklearn.datasets import make_blobs, make_moons
from playbook_clustering import diagnostico_clustering as dg
rng=np.random.default_rng(0)
X1,_=make_blobs(400,centers=[[2,20],[8,60],[15,35]],cluster_std=[1.2,3,2],random_state=42)
X2,_=make_moons(400,noise=.06,random_state=0)
Xa,_=make_blobs(400,centers=3,random_state=170); X3=Xa@np.array([[0.6,-0.6],[-0.4,0.8]])
X4=np.vstack([make_blobs(400,centers=[[0,0],[6,6]],cluster_std=1,random_state=1)[0],rng.uniform(-8,14,(15,2))])
for n,X in [("blobs",X1),("lunas",X2),("elipticos",X3),("blobs+atipicos",X4)]:
    r=dg(pd.DataFrame(X,columns=["a","b"]),grafico=f"{n}.png")
    print(n,"->",r["recomendacion"],"|",r["razones"][0]); print("   ",{k:r[k] for k in ["k_silhouette","k_bic_gmm","dbscan_grupos","dbscan_ruido","ari_kmeans_gmm","ari_kmeans_dbscan","atipicos_z3","solape_convexo","dbscan_eps"]})
