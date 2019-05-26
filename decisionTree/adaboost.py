import numpy as np 
import math
def getPrediction(datalist,feature_index,value,cut_ops):
    num_feature = len(datalist)
    features = [data[feature_index] for data in datalist]
    prediction = [1]*num_feature
    if cut_ops == 'more':
        for i in range(num_feature):
            if features[i] >= value:
                prediction[i] = -1
    else:
        for i in range(num_feature):
            if features[i] < value:
                prediction[i] = -1
    return prediction

def create_tree(datalist,labels,weights):
    num_data = len(datalist)
    num_feature = len(datalist[0])-1
    prediction = [1]*num_data
    min_error = inf
    tree = {}
    for feature_index in range(num_feature):
        values = set([data[feature_index] for data in datalist])
        for value in values:
            for cut_ops in ['more','less']:
                prediction = getPrediction(datalist,feature_index,value,cut_ops)
                err_sum = sum([for i in len(prediction) if prediction[i]==datalist[i][-1] ])/len(prediction)
                if err_sum < min_error:
                    min_error = err_sum
                    best_cut_ops = cut_ops
                    best_prediction = prediction[:]
                    best_value = value
                    best_feature_index = feature_index
    tree['feature'] = lables[best_feature_index]
    tree['value'] = best_value
    tree['cut_ops'] = best_cut_ops
    return tree,best_prediction,min_error

def adaboost(datalist,labels,num_iter=40):
    trees = []
    num_data = len(datalist)
    weights_data = [1/num_data]*num_data
    weights_tree = []
    for i in range(num_iter):
        tree,prediction,error = create_tree(datalist,labels,weights_data)
        weight_tree = 0.5*log((1.0-error))/max(error,1e-6)
        weights_tree.append(weight_tree)
        trees.append(tree)
        for i in range(len(prediction)):
            expon = -weight_tree*datalist[-1]*prediction[i]
            weights_data[i] *= exp(expon)
    return trees,weights_tree

def adaclassify(classifiers,datalist):
    predictions = []
    for i in range(classifiers):
        prediction = getPrediction(datalist,classifiers[i]['feature'],classifiers[i]['value'],classifiers[i]['cut_ops'])
        predictions +=prediction
    for i in range(len(predictions)):
        if predictions[i] > 0:
            predictions[i] = 1
        else:
            predictions[i] = -1
    return predictions


   
        


 

        
