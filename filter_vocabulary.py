from nltk.stem.snowball import SnowballStemmer
from nltk.corpus import stopwords
import pymorphy2
import re

class FilterVocabulary:
    def __init__(self):
        self.lem_voc = []
        self.stem_voc = []
        self.vocabulary = []
        self.lemmatizer = pymorphy2.MorphAnalyzer() 
        self.stemmer = SnowballStemmer(language="russian")
        self.stopwords = stopwords.words('russian')
        self.stopwords = list(filter(lambda x: len(x)>2, self.stopwords))

    def create(self,filename = "vocabulary.txt"):
        tmp = []
        try:
            with open(filename, "r",encoding='utf-8') as f:
                tmp = f.read()
        except IOError:
            return "Возникли ошибки при попытке открыть файл"
        self.vocabulary = list(filter(lambda x: not x == "",re.sub('\s+', ' ',re.sub(r'[\t\n\r]'," ",str.lower(tmp))).split(' ')))   
        for i in self.vocabulary:
            if len(re.findall(r'[A-Za-z]',i))>0:
                return "Файл содержит буквы английского алфавита"
        for word in self.vocabulary:
            for p in self.lemmatizer.parse(word):
                norm_p = p.normal_form
                if not norm_p in self.lem_voc:
                    if 'ё' in norm_p:
                        if not norm_p.replace('ё','е') in self.lem_voc:
                            self.lem_voc.append(norm_p.replace('ё','е'))
                    self.lem_voc.append(norm_p)
            stem = self.stemmer.stem(word)       
            if not stem in self.stem_voc: 
                if 'ё' in word:
                    if not self.stemmer.stem(word.replace('ё','е')) in self.stem_voc: 
                        self.stem_voc.append(self.stemmer.stem(word.replace('ё','е')))
                self.stem_voc.append(self.stemmer.stem(word))

censFilter = FilterVocabulary()
