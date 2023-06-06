from sklearn.cluster import KMeans
import time
def clustering(feature_vect, img_df):
    # KMeans: 5 
    start=time.process_time()
    km_cluster = KMeans(n_clusters=5, max_iter=10000, random_state=0)
    km_cluster.fit(feature_vect)

    #k mean clustering
    cluster_label = km_cluster.labels_
    #cluster_centers = km_cluster.cluster_centers_

    img_df['cluster_label'] = cluster_label
    end=time.process_time()
    print("Clustering Process_time: ", end-start, "seconds")


