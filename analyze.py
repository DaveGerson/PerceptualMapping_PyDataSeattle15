# -*- coding: utf-8 -*-
#Inspired from http://okomestudio.net/biboroku/?p=2357

print(__doc__)
import numpy as np

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA
import pandas as pd




n_samples = 20
seed = np.random.RandomState(seed=3)

df = pd.io.parsers.read_csv('output.csv')
df = df.set_index('names')
df.apply(lambda c: c / c.sum() * 100, axis=0)

df = df.ix[:,0:50]


dataMatrix = df.as_matrix()
dataMatrix -= dataMatrix.mean()
similarities = euclidean_distances(dataMatrix)

print df.describe()
print df.head()
print "Test Here"

mds = manifold.MDS(n_components=2, max_iter=3000, eps=1e-9, random_state=seed,
                   dissimilarity="precomputed", n_jobs=1)
pos = mds.fit(similarities).embedding_

nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=seed, n_jobs=1,
                    n_init=1)
npos = nmds.fit_transform(similarities)

npos *= np.sqrt((dataMatrix ** 2).sum()) / np.sqrt((npos ** 2).sum())

# Rescale the data
npos *= np.sqrt((dataMatrix ** 2).sum()) / np.sqrt((npos ** 2).sum())

# Rotate the data
clf = PCA(n_components=2)
X_true = clf.fit_transform(dataMatrix)

npos = clf.fit_transform(npos)

fig = plt.figure(1)
ax = plt.axes([0., 0., 1., 1.])

plt.scatter(npos[:, 0], npos[:, 1], s=20, c='b')
plt.legend(('NMDS'), loc='best')

similarities = similarities.max() / similarities * 100
similarities[np.isinf(similarities)] = 0

print "\n\n\n\n\n\n\n\n"
print npos[:, 0]
print npos[:, 1]

for i, txt in enumerate(list(df.index)):
    ax.annotate(txt, (npos[:, 0][i], npos[:, 1][i]))

plt.show()