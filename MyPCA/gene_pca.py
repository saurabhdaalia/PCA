import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from .base import Base


class GenePCA(Base):
    def __init__(self, intensity_file, meta_file):
        super().__init__(intensity_file, meta_file)
        sns.set(style="darkgrid")

    def fit(self):
        X = self.gdf.drop(["symbol", "Unnamed: 0"], 1)
        X = X.apply(pd.to_numeric, errors='coerce')
        X = X.fillna(X.mean())
        X = X.transpose()
        sc = StandardScaler()
        X = sc.fit_transform(X)
        pca = PCA(n_components=2)
        X_fit = pca.fit_transform(X)
        self.mdf['PC1'] = X_fit[:, 0]
        self.mdf['PC2'] = X_fit[:, 1]



    def visualise(self):
        sns.relplot(x='PC1', y='PC2', hue='sIdx', sizes=(
            130, 500), height=7.5, legend='full', data=self.mdf)
        plt.show()
