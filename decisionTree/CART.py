#三个停止条件
#生成决策树

#计算基尼指数
#def Gini(datalist,feature):

#切分数据集
from collections import Counter

#def createTree(datalist,lablelist,ops):
    #判断边界条件
    #对特征列表中的每个特征计算基尼指数
    #选择最小的基尼指数
    #将数据集划分到左子树和右子树
    #对左子树和右子树进行递归

def createDatalist(filename):
    datalist = []
    with open(filename,'r') as f:
        line = f.readline()
        labels = line.strip().split(' ')
        for line in f.readlines():
            curLine = line.strip().split(' ')
            datalist.append(curLine)
    return datalist,labels

def Gini(datalist):
    labeldict = {}
    gini = 0
    for data in datalist:
        label = data[-1]
        labeldict.setdefault(label,0)
        labeldict[label] += 1
    for label in labeldict.keys():
        p = labeldict[label] / len(datalist)
        gini += p*(1-p)
    return gini

def splitDatalist(datalist,feature,value):
    left_child = []
    right_child = []
    for data in datalist:
        new_data = data[:feature]
        new_data.extend(data[feature+1:])
        if data[feature] == value:
            left_child.append(new_data)
        else:
            right_child.append(new_data)
    return left_child,right_child

def isOneLabel(datalist):
    labels = set([data[-1] for data in datalist])
    if(len(labels)==1):
        return True
    return False

def getBestFeatureAndValue(datalist):
    best_feature = 0
    best_value = 0
    min_gini = 'inf'
    total_gini = Gini(datalist)
    total_num = len(datalist)
    for feature in range(len(datalist[0])-1):
        values = set([data[feature] for data in datalist])
        for value in values:
            left_child,right_child = splitDatalist(datalist,feature,value)
            if(len(left_child)==0 or len(right_child)==0 ):
                continue
            value_gini = len(left_child)/total_num *Gini(left_child) + len(right_child)/total_num *Gini(right_child)
            if value_gini < float(min_gini):
                best_feature = feature
                best_value = value
                min_gini = value_gini
    #if total_gini-float(min_gini) < 0.000001: return None,None
    return best_feature,best_value

def majorityCnt(labels):
    labels_count = Counter(labels)
    label,counts = labels_count.most_common(1)[0]
    return label

def createTree(datalist,labels):
    if len(labels)==1:
        return datalist[0][-1]
    if len(datalist[0])==1:
        return majorityCnt([data[-1] for data in datalist])
    feature,value = getBestFeatureAndValue(datalist)
    Tree = {}
    Tree['feature'] = labels[feature]
    Tree['value'] = value
    del labels[feature]
    left_child,right_child = splitDatalist(datalist,feature,value)
    Tree['left_sub_tree'] = createTree(left_child,labels)
    Tree['right_sub_tree'] = createTree(right_child,labels)
    return Tree

def classify(data,labels,tree):
    if not  isinstance(tree,dict):
        return tree
    index = labels.index(tree['feature'])
    if data[index] == tree['value']:
        subtree = tree['left_sub_tree']
    else:
        subtree = tree['right_sub_tree']
    return classify(data,labels,subtree) 


if __name__ == "__main__":
    traindata,trainlabels = createDatalist('traindata_tree.txt')
    testdata,testlabels = createDatalist('testdata_tree.txt')
    tree = createTree(traindata,trainlabels)
    print(tree)
    error = 0
    for i in range(len(testdata)):
        tag = classify(testdata[i],testlabels,tree)
        print(tag,testdata[i][-1])
        if tag != testdata[-1]:
            error += 1
    err_prob = error/len(testdata)
    print(error)
    print(err_prob)




