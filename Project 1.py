# # Nikolas Reuter
# # Big Data Analytics
# # Project 1
#
# # Applying PCA to the Wine dataset from UCI Database
#
# # Load all libraries
# from sklearn.datasets import load_wine
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# import seaborn as sns
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d  # noqa: F401
#
# # Load the Wine dataset
# wine = load_wine(as_frame=True)
#
#
# # Rename classes using the wine target names
# wine.frame["target"] = wine.target_names[wine.target]
# _ = sns.pairplot(wine.frame, hue="target")
#
# # Standardize the data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(wine.data)
#
# # Apply PCA
# pca = PCA(n_components=3)
# X_reduced = pca.fit_transform(X_scaled)
#
# # 3D Visualization
# fig = plt.figure( figsize=(12, 9))
# ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)
# #ax.view_init(elev=20, azim=45)
#
# scatter = ax.scatter(
#     X_reduced[:, 0],
#     X_reduced[:, 1],
#     X_reduced[:, 2],
#     c=wine.target,
#     s=250,
# )
#
# #ax.set(
#  #   title="First Three Principal Components (Wine Dataset)",
#  #   xlabel="1st Principal Component",
#  #   ylabel="2nd Principal Component",
#   #  zlabel="3rd Principal Component",
# #)
# ax.set_title("First Three Principal Components (Wine Dataset)", fontsize=44, pad=40)
# ax.set_xlabel("1st Principal Component", fontsize=40, labelpad=36)
# ax.set_ylabel("2nd Principal Component", fontsize=40, labelpad=36)
# ax.set_zlabel("3rd Principal Component", fontsize=40, labelpad=36)
#
# ax.xaxis.set_ticklabels([])
# ax.yaxis.set_ticklabels([])
# ax.zaxis.set_ticklabels([])
#
# legend = ax.legend(
#     scatter.legend_elements()[0],
#     wine.target_names.tolist(),
#     loc="upper right",
#     title="Classes",
#     fontsize=40,
#     title_fontsize=42,
# )
# ax.add_artist(legend)
#
# plt.show()




# # Nikolas Reuter
# # Big Data Analytics
# # Project 1
# # Applying PCA to the Wine dataset from UCI Database
#
# # Load libraries
# from sklearn.datasets import load_wine
# from sklearn.preprocessing import StandardScaler
# from sklearn.decomposition import PCA
# from sklearn.linear_model import LogisticRegression
# from sklearn.model_selection import train_test_split
# from sklearn.metrics import accuracy_score
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
# import mpl_toolkits.mplot3d  # noqa: F401
#
# # Load the Wine dataset
# wine = load_wine(as_frame=True)
#
# # Rename classes
# wine.frame["target"] = wine.target_names[wine.target]
#
# # Pairplot
# _ = sns.pairplot(wine.frame, hue="target")
#
# # Standardize the data
# scaler = StandardScaler()
# X_scaled = scaler.fit_transform(wine.data)
#
# # FULL PCA
# pca_full = PCA()
# X_full = pca_full.fit_transform(X_scaled)
#
# # print("Explained Variance Ratio:")
# # print(pca_full.explained_variance_ratio_)
# # print("\nCumulative Explained Variance:")
# # print(pca_full.explained_variance_ratio_.cumsum())
#
# # # Scree Plot
# # plt.figure(figsize=(8,6))
# # plt.plot(pca_full.explained_variance_ratio_, marker='o')
# # plt.title("Scree Plot")
# # plt.xlabel("Principal Component")
# # plt.ylabel("Explained Variance Ratio")
# # plt.grid()
# # plt.show()
#
# # # Cumulative Variance Plot
# # plt.figure(figsize=(8,6))
# # plt.plot(pca_full.explained_variance_ratio_.cumsum(), marker='o')
# # plt.title("Cumulative Explained Variance")
# # plt.xlabel("Number of Components")
# # plt.ylabel("Cumulative Explained Variance")
# # plt.grid()
# # plt.show()
#
# # PCA with 3 Components
# pca = PCA(n_components=3)
# X_reduced = pca.fit_transform(X_scaled)
#
# # # PCA Loadings
# # loadings = pd.DataFrame(
# #     pca.components_,
# #     columns=wine.feature_names,
# #     index=["PC1", "PC2", "PC3"]
# # )
#
# # print("\nPCA Loadings:")
# # print(loadings)
#
# # 2D Visualization
# plt.figure(figsize=(8,6))
# plt.scatter(X_reduced[:,0], X_reduced[:,1], c=wine.target)
# plt.title("2D PCA Projection (Wine Dataset)")
# plt.xlabel("PC1")
# plt.ylabel("PC2")
# plt.show()
#
# # 3D Visualization
# fig = plt.figure(figsize=(8, 6))
# ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)
#
# scatter = ax.scatter(
#     X_reduced[:, 0],
#     X_reduced[:, 1],
#     X_reduced[:, 2],
#     c=wine.target,
#     s=100,
# )
#
# ax.set_title("3D PCA Projection (Wine Dataset)")
# ax.set_xlabel("PC1")
# ax.set_ylabel("PC2")
# ax.set_zlabel("PC3")
#
# legend = ax.legend(
#     scatter.legend_elements()[0],
#     wine.target_names.tolist(),
#     loc="upper right",
#     title="Classes",
# )
# ax.add_artist(legend)
#
# plt.show()
#
# # # Classification Comparison
# # # Train-test split WITHOUT PCA
# # X_train, X_test, y_train, y_test = train_test_split(
# #     X_scaled, wine.target, test_size=0.3, random_state=42
# # )
# #
# # model = LogisticRegression(max_iter=5000)
# # model.fit(X_train, y_train)
# # y_pred = model.predict(X_test)
# #
# # print("\nAccuracy without PCA:", accuracy_score(y_test, y_pred))
# #
# # # Train-test split WITH PCA (2 components)
# # pca_2 = PCA(n_components=2)
# # X_pca_2 = pca_2.fit_transform(X_scaled)
# #
# # X_train_pca, X_test_pca, y_train, y_test = train_test_split(
# #     X_pca_2, wine.target, test_size=0.3, random_state=42
# # )
# #
# # model_pca = LogisticRegression(max_iter=5000)
# # model_pca.fit(X_train_pca, y_train)
# # y_pred_pca = model_pca.predict(X_test_pca)
# #
# # print("Accuracy with PCA (2 components):", accuracy_score(y_test, y_pred_pca))




# Nikolas Reuter
# Big Data Analytics
# Project 1
# Applying PCA to the Wine dataset from UCI Database

# Load libraries
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d  # noqa: F401

# Load the Wine dataset
wine = load_wine(as_frame=True)

# Rename classes
wine.frame["target"] = wine.target_names[wine.target]

# Pairplot (Very Large)
# _ = sns.pairplot(wine.frame, hue="target")
# _ = sns.pairplot(wine.frame, hue="target", height=1.5, aspect=1)
g = sns.pairplot(wine.frame, hue="target", height=1, aspect=1, plot_kws={"s": 10})
for ax in g.axes.flatten():
    ax.set_xlabel(ax.get_xlabel(), rotation=45, ha='right', fontsize=7)
    ax.set_ylabel(ax.get_ylabel(), rotation=45, ha='right', fontsize=7)

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(wine.data)

# FULL PCA
pca_full = PCA()
X_full = pca_full.fit_transform(X_scaled)

# PCA with 3 Components
pca = PCA(n_components=3)
X_reduced = pca.fit_transform(X_scaled)

# 2D Visualization
plt.figure(figsize=(8,6))

scatter = plt.scatter(X_reduced[:,0], X_reduced[:,1], c=wine.target)

plt.title("2D PCA Projection (Wine Dataset)")
plt.xlabel("PC1")
plt.ylabel("PC2")

plt.legend(
    scatter.legend_elements()[0],
    wine.target_names.tolist(),
    loc="lower right",
    title="Classes",
)

plt.show()


# 3D Visualization
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection="3d", elev=-150, azim=110)

scatter = ax.scatter(
    X_reduced[:, 0],
    X_reduced[:, 1],
    X_reduced[:, 2],
    c=wine.target,
    s=100,
)

ax.set_title("3D PCA Projection (Wine Dataset)")
ax.set_xlabel("PC1")
ax.set_ylabel("PC2")
ax.set_zlabel("PC3")

legend = ax.legend(
    scatter.legend_elements()[0],
    wine.target_names.tolist(),
    loc="upper right",
    title="Classes",
)
ax.add_artist(legend)

plt.show()
