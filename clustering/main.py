import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
import sys
import numpy as np
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import csv
from collections import Counter
from k_means import K_Means
from evaluate import Evaluate
import matplotlib.cm as cm


def plot_data(data):

    pca = PCA(n_components=2)
    principalComponents = pca.fit_transform(data)

    plt.scatter(principalComponents[:,0], principalComponents[:,1], s=30)

    plt.show()

embeddings = np.round(np.load("embeddings/test/embeddings.npy"), decimals=6)
t_labels = np.load("embeddings/test/labels.npy")
label_strings = np.load("embeddings/test/label_strings.npy")

# 3 classes and 15 images
# subset_embeddings = embeddings[:15]
# subset_labels = t_labels[:15]

# Clustering
X = np.round(embeddings[:-1], decimals=6)
#X = subset_embeddings
# label: names
names = label_strings[:-1]

# KMeans from sklearn
kmeans = KMeans(n_clusters=10).fit(X)
print(kmeans.labels_)
# print("\n")
# print(kmeans.cluster_centers_)
# print("\n")
# y = embeddings[-1].reshape(1, -1)
# p = kmeans.predict(y)
# print(p)

# KMeans implementation
model1 = K_Means(num_clusters=10)
model1.fit(X)

model2 = K_Means(num_clusters=10, k_means_plus_plus=True)
model2.fit(X)

#print(model.centroids)
# print("\n")
print(model1.labels)

print(model2.labels)
# print("\n")
# print(model.label_feature)

# label_names = model.get_cluster_labels(model.labels, names)

# # output cluster results in csv file
# with open("cluster_output2.csv","w+") as my_csv:
#     csvWriter = csv.writer(my_csv, delimiter=',')
#     csvWriter.writerows(label_names)

# ####### Evaluation of Clusters ###################
# ev = Evaluate(label_names)

# # True lables with number of images for each label
# true_labels = ev.get_true_labels("datasets/test/")

#print(true_labels)

# Evaluation metric

# precsion, recall, f_measure = ev.compute_metric()

# print(precsion)
# print(recall)
# print(f_measure)

########### Prediction ###################

# print("\n")
# print(model.predict(embeddings[-1].reshape(1, -1)))

########### Plotting ####################

#plot_data(X)
#model2.plot_clusters(X, model2.labels, model2.centroids)


########3 Plot example ##################
# n = ['Ariel_Sharon', 'Arnold_Schwarzenegger','Colin_Powell']

# for i in subset_labels:
#   color = colors[i]
#   for feature in subset_embeddings[subset_labels == i]:
#       plt.scatter(feature[0], feature[1], marker="o", color=color, s=20, label=color)

# leg = plt.legend(n, loc="lower right")
# c=["g","r","c"]

# for i, j in enumerate(leg.legendHandles):
#     j.set_color(c[i])

# plt.show()

##for unknown in unknowns:
##    classification = model.predict(unknown)
##    plt.scatter(unknown[0], unknown[1], marker="*", color=colors[classification], s=150, linewidths=5)

