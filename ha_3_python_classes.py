class CountVectorizer():
    def fit_transform(self, corpus):
        self.corpus = corpus
        arr = []
        for str_doc in self.corpus:
            doc = str_doc.split(' ')
            for word in doc:
                arr.append(word.lower())
        self.feature_names = list(set(arr))
        arr_dict = []
        for str_doc in self.corpus:
            doc = str_doc.split(' ')
            dict_w = {}
            for word in doc:
                if dict_w.get(word.lower()) == None:
                    dict_w[word.lower()] = 0
                dict_w[word.lower()] += 1
            arr_dict.append(dict_w)
        count_vect = []
        for dict_w in arr_dict:
            arr_count = []
            for feat_name in self.feature_names:
                if dict_w.get(feat_name) == None:
                    arr_count.append(0)
                else:
                    arr_count.append(dict_w[feat_name])
            count_vect.append(arr_count)
        return count_vect
    def get_feature_names(self):
        return self.feature_names

if __name__ == '__main__':
    data = input()
    cv = CountVectorizer()
    print(cv.fit_transform(data))
    print(cv.get_feature_names())