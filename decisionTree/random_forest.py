import CART
from collections import Counter
import random
import math

def baggingDatalist(datalist,labels,num_features):
    indexlist = [i for i in range(len(datalist[0])-1)]
    random_index = random.sample(indexlist,num_features)
    random_datalist = []
    random_labels = []
    for i in len(datalist):
        random_data = []
        for index in random_index:
            random_data.append(datalist[i][index])
        random_data.append(datalist[-1])
        random_datalist.append(random_data)
        random_labels.append(labels[i])
    random_labels.append(labels[-1])
    return random_datalist,random_labels


def getForest(datalist,labels,num_tree):
    forest = []
    for i in range(num_tree):
        random_datalist,random_labels = baggingDatalist(datalist,labels,math.sqrt(len(datalist)-1))
        tree = CART.createTree(random_datalist,random_labels)
        forest.append(tree)
    return forest

def randomForestClassify(datalist,labels,forest):
    label_pred = []
    for data in datalist:
        label_tree = []
        for tree in forest:
            label = CART.classify(data,labels,tree)
            label_tree.append(label)
        max_label,num = (Counter(label_tree)).most_common(1)
        label_pred.append(max_label)
    return label_pred




            
        


