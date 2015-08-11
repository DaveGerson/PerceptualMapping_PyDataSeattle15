__author__ = 'gerson64'
# Based on work by Nelle Varoquaux <nelle.varoquaux@gmail.com>
# Licence: BSD

import numpy as np

from matplotlib import pyplot as plt
from matplotlib.collections import LineCollection

from sklearn import manifold
from sklearn.metrics import euclidean_distances
from sklearn.decomposition import PCA

X_true = seed.randint(0, 20, 2 * n_samples).astype(np.float)
X_true = X_true.reshape((n_samples, 2))
# Center the data
X_true -= X_true.mean()

seed = np.random.RandomState()
nmds = manifold.MDS(n_components=2, metric=False, max_iter=3000, eps=1e-12,
                    dissimilarity="precomputed", random_state=seed, n_jobs=1,
                    n_init=1)
similarities = euclidean_distances(X_true)
npos = nmds.fit_transform(similarities, init=pos)