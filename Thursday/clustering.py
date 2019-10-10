# time algorithm running time
import time

#for plotting
from itertools import cycle, islice
import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.use('TkAgg')
import numpy as np

# for unsupervised clustering
from sklearn import cluster, datasets
from sklearn.preprocessing import StandardScaler

# define datasets for illustration of clustering
num_pts = 3000

np.random.seed(17)
uniform = np.random.rand(num_pts, 2), None  # observe Voronoi diagram
blobs = datasets.make_blobs(n_samples=num_pts, n_features=3)  # three separated blobs
noisy_circles = datasets.make_circles(n_samples=num_pts, factor=.2, noise=.05)  # a circle inside another circle
noisy_moons = datasets.make_moons(n_samples=num_pts, noise=.05)  # two moons

datasets = [uniform, blobs, noisy_circles, noisy_moons]
num_clusters = [4, 3, 2, 2]  # number of clusters the algorithm should identify (if relevant for algorithm)

##################################################################################################################
# K Means
##################################################################################################################
fig, axs = plt.subplots(nrows=1, ncols=len(datasets),figsize=(15,15))
fig.suptitle("KMeans", size=24)
fig.set_size_inches(14, 5, forward=True)
for dataset_ctr, dataset in enumerate(datasets):
    x, _ = dataset  # don't need label
    x = StandardScaler().fit_transform(x)

    # choose unsupervised clustering algorithm
    alg = cluster.KMeans(n_clusters=num_clusters[dataset_ctr])

    # fit and time the execution
    t0 = time.time()
    alg.fit(x)
    t1 = time.time()

    # get predicted labels
    y_pred = alg.predict(x)

    colors = np.array(list(islice(cycle(['red', 'green', 'blue', 'orange', 'cyan', 'magenta', 'yellow', 'coral', 'lime']), int(max(y_pred)+1))))  # select as many colors as there are different clusters
    colors = np.append(colors, ['black'])  # for outliers/anomalies

    # color points according to center they belong to
    axs[dataset_ctr].scatter(x[:, 0], x[:, 1], s=10, color=colors[y_pred])

    # give timing information
    axs[dataset_ctr].text(2.2, -2.1, ('{:1.4f}s'.format(t1 - t0).lstrip('0')), size=14, horizontalalignment='right', backgroundcolor='white')

    # plot cluster centers
    centers = alg.cluster_centers_
    axs[dataset_ctr].scatter(centers[:, 0], centers[:, 1], s=100, marker='X', edgecolors='black')

    # format the plot
    axs[dataset_ctr].set_xticks([])
    axs[dataset_ctr].set_yticks([])
    axs[dataset_ctr].set_xlim(-2.3, 2.3)
    axs[dataset_ctr].set_ylim(-2.3, 2.3)
    axs[dataset_ctr].set_aspect('equal')

plt.tight_layout()
plt.show()
plt.savefig("./KMeans.png")
plt.close()

##################################################################################################################
# Mean shift
##################################################################################################################
fig, axs = plt.subplots(nrows=1, ncols=len(datasets), figsize=(15, 15))
fig.suptitle("Mean shift", size=24)
fig.set_size_inches(14, 5, forward=True)
for dataset_ctr, dataset in enumerate(datasets):
    x, _ = dataset  # don't need label
    x = StandardScaler().fit_transform(x)

    # choose unsupervised clustering algorithm
    bandwidth = cluster.estimate_bandwidth(x, quantile=.3)
    alg = cluster.MeanShift(bandwidth=bandwidth, bin_seeding=True)

    # fit and time the execution
    t0 = time.time()
    alg.fit(x)
    t1 = time.time()

    # get predicted labels
    y_pred = alg.predict(x)

    colors = np.array(list(islice(cycle(['red', 'green', 'blue', 'orange', 'cyan', 'magenta', 'yellow', 'coral', 'lime']),int(max(y_pred) + 1))))  # select as many colors as there are different clusters
    colors = np.append(colors, ['black'])  # for outliers/anomalies

    # color points according to center they belong to
    axs[dataset_ctr].scatter(x[:, 0], x[:, 1], s=10, color=colors[y_pred])

    # give timing information
    axs[dataset_ctr].text(2.2, -2.1, ('{:1.4f}s'.format(t1 - t0).lstrip('0')), size=14, horizontalalignment='right', backgroundcolor='white')

    # plot cluster centers
    centers = alg.cluster_centers_
    axs[dataset_ctr].scatter(centers[:, 0], centers[:, 1], s=100, marker='X', edgecolors='black')

    # format the plot
    axs[dataset_ctr].set_xticks([])
    axs[dataset_ctr].set_yticks([])
    axs[dataset_ctr].set_xlim(-2.3, 2.3)
    axs[dataset_ctr].set_ylim(-2.3, 2.3)
    axs[dataset_ctr].set_aspect('equal')

plt.tight_layout()
plt.show()
plt.savefig("./MeanShift.png")
plt.close()


##################################################################################################################
# DBSCAN
##################################################################################################################
fig, axs = plt.subplots(nrows=1, ncols=len(datasets), figsize=(15, 15))
fig.suptitle("DBSCAN", size=24)
fig.set_size_inches(14, 5, forward=True)
for dataset_ctr, dataset in enumerate(datasets):
    x, _ = dataset  # don't need label
    x = StandardScaler().fit_transform(x)

    # choose unsupervised clustering algorithm
    alg = cluster.DBSCAN(eps=0.3)

    # fit and time the execution
    t0 = time.time()
    alg.fit(x)
    t1 = time.time()

    # get predicted labels
    y_pred = alg.labels_.astype(np.int)

    colors = np.array(list(islice(cycle(['red', 'green', 'blue', 'orange', 'cyan', 'magenta', 'yellow', 'coral', 'lime']),int(max(y_pred) + 1))))  # select as many colors as there are different clusters
    colors = np.append(colors, ['black'])  # for outliers/anomalies

    # color points according to center they belong to
    axs[dataset_ctr].scatter(x[:, 0], x[:, 1], s=10, color=colors[y_pred])

    # give timing information
    axs[dataset_ctr].text(2.2, -2.1, ('{:1.4f}s'.format(t1 - t0).lstrip('0')), size=14, horizontalalignment='right', backgroundcolor='white')

    # format the plot
    axs[dataset_ctr].set_xticks([])
    axs[dataset_ctr].set_yticks([])
    axs[dataset_ctr].set_xlim(-2.3, 2.3)
    axs[dataset_ctr].set_ylim(-2.3, 2.3)
    axs[dataset_ctr].set_aspect('equal')

plt.tight_layout()
plt.show()
plt.savefig("./DBSCAN.png")
plt.close()


##################################################################################################################
# BIRCH
##################################################################################################################
fig, axs = plt.subplots(nrows=1, ncols=len(datasets), figsize=(15, 15))
fig.suptitle("BIRCH", size=24)
fig.set_size_inches(14, 5, forward=True)
for dataset_ctr, dataset in enumerate(datasets):
    x, _ = dataset  # don't need label
    x = StandardScaler().fit_transform(x)

    # choose unsupervised clustering algorithm
    alg = cluster.Birch()

    # fit and time the execution
    t0 = time.time()
    alg.fit(x)
    t1 = time.time()

    # get predicted labels
    y_pred = alg.labels_.astype(np.int)

    colors = np.array(list(islice(cycle(['red', 'green', 'blue', 'orange', 'cyan', 'magenta', 'yellow', 'coral', 'lime']),int(max(y_pred) + 1))))  # select as many colors as there are different clusters
    colors = np.append(colors, ['black'])  # for outliers/anomalies

    # color points according to center they belong to
    axs[dataset_ctr].scatter(x[:, 0], x[:, 1], s=10, color=colors[y_pred])

    # give timing information
    axs[dataset_ctr].text(2.2, -2.1, ('{:1.4f}s'.format(t1 - t0).lstrip('0')), size=14, horizontalalignment='right', backgroundcolor='white')

    # format the plot
    axs[dataset_ctr].set_xticks([])
    axs[dataset_ctr].set_yticks([])
    axs[dataset_ctr].set_xlim(-2.3, 2.3)
    axs[dataset_ctr].set_ylim(-2.3, 2.3)
    axs[dataset_ctr].set_aspect('equal')

plt.tight_layout()
plt.show()
plt.savefig("./BIRCH.png")
plt.close()
