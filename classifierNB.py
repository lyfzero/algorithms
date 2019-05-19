from collections import Counter
import re
import os
import random
def cutwords(text):
    with open ('stopwords.txt') as f:
        stopwords = f.read()
    stopwords = set(stopwords.split('\n'))
    #cutter = re.compile('\W*')
    wordlist = [word.lower() for word in text.split() if word.isalpha() if word not in stopwords]
    return wordlist


class classifier():
    def __init__(self,getfeatures):
        self.tag_dic = {}
        self.vocab_dic = {}
        self.vocab_dic_all = Counter()
        self.p_tag = {}
        self.p_word = {}
        self.getfeatures = getfeatures

    def train(self,text,tag):
        wordlist = self.getfeatures(text)
        wordcount = Counter(wordlist)
        self.tag_dic.setdefault(tag,0)
        self.tag_dic[tag] += 1
        if tag in self.vocab_dic:
            self.vocab_dic[tag] += wordcount
        else:
            self.vocab_dic[tag] = wordcount
    
    def get_text_num(self):
        return sum(self.tag_dic.values())

    def get_tags(self):
        return self.tag_dic.keys()

    def get_text_tag_num(self,tag):
        if tag in self.tag_dic.keys():
            return self.tag_dic[tag]
        else:
            return 0
    
    def get_word_tag_num(self,word,tag):
        if tag in self.vocab_dic and word in self.vocab_dic[tag]:
            return self.vocab_dic[tag][word]
        else:
            return 0
    
    def get_p_word_tag(self,weight=1):
        self.p_tag = {tag:(self.tag_dic[tag]+weight)/sum(self.tag_dic.values())*(1+weight)  for tag in self.tag_dic}
        for tag in self.vocab_dic:
            self.vocab_dic_all += self.vocab_dic[tag]
        print(self.vocab_dic_all)
        self.p_word = {}
        for tag in self.vocab_dic:
            p_word_tag={}
            for word in self.vocab_dic_all.keys():
                p_word_tag.setdefault(word,(self.vocab_dic[tag][word]+weight) / sum(self.vocab_dic_all.values())*(1+weight))
            self.p_word.setdefault(tag,p_word_tag)
        return self.p_tag,self.p_word




class classifierNB(classifier):
    def __init__(self,getfeatures):
        classifier.__init__(self,getfeatures)
    
    def textprob(self,text,tag):
        wordlist = self.getfeatures(text)
        p=1
        pwords = self.p_word[tag]
        print(pwords)
        for word in wordlist:
            p*=pwords[word]
        return p

    def prob(self,text,tag):
        tagprob = self.p_tag[tag]
        textprob = self.textprob(text,tag)
        return tagprob*textprob           
    
    def classify(self,text):
        maxp = 0.0
        probs = {}
        for tag in self.tag_dic.keys():
            probs[tag] = self.prob(text,tag)
            if probs[tag] >maxp:
                maxp = probs[tag]
                text_tag = tag
        return text_tag
 
 

def readFile(filename):
    fopen = open(filename,'r') 
    for eachLine in fopen:
        print(eachLine)
    fopen.close()

def eachFile(filepath):
    wordlists = []
    pathDir = os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join('%s\\%s'%(filepath,allDir))
        with open(child,'r') as f:
            wordlist = cutwords(f.read())
            wordlists.append(wordlist)
    print(wordlists)
    return wordlists

def get_text_data2():
    train_data = []
    test_data = []
    filePath1 = "C:\\Users\\yanyuzero\\Desktop\\python\\\\aclImdb\\train\\neg"
    filePath2 = "C:\\Users\\yanyuzero\\Desktop\\python\\\\aclImdb\\train\\pos"
    filePath3 = "C:\\Users\\yanyuzero\\Desktop\\python\\\\aclImdb\\test\\neg"
    filePath4 = "C:\\Users\\yanyuzero\\Desktop\\python\\\\aclImdb\\test\\pos"
    train_data.append(readFile(filePath1))
    train_data.append(readFile(filePath2))
    test_data.append(readFile(filePath3))
    test_data.append(readFile(filePath4))
    random.shuffle(train_data)
    random.shuffle(test_data)
    return train_data,test_data   


if __name__=='__main':
    cl=classifierNB(cutwords)
    train_data,test_data = get_text_data2()
    print(len(train_data))
    for text,tag in train_data:
        cl.train(text,tag)
    predicts=[]
    count=0
    for text,tag in test_data:
        predict = cl.classify(text)
        if predict == tag:
            count+=1
        predicts.append(predict)
    print(count/len(test_data))
            

        