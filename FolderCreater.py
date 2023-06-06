
import os, shutil
def folderCreate(img_df, path):
    imgNameList = img_df["imagename"]
    clusterLabelList = img_df["cluster_label"]
    
    for img, cluster in zip(imgNameList, clusterLabelList):
        cluster_str = str(cluster)
        
        if not os.path.isdir(path+cluster_str):
            os.makedirs(path+cluster_str)

        shutil.move(path+img, path+cluster_str+"/"+img)