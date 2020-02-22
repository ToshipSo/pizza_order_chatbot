import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import csv
import pickle


class PreProcessText:
    def __init__(self):
        self._stopwords = set(stopwords.words('english'))

    def processText(self, list_of_texts):
        processedText = []
        for text in list_of_texts:
            processedText.append((self._processText(text["text"]), text["label"]))
        return processedText

    def _processText(self, text):
        text = text.lower()
        text = word_tokenize(text)
        return [word for word in text if word not in self._stopwords]


def buildVocabulary(preprocessedTrainingSet):
    all_words = []

    for (words, sentiment) in preprocessedTrainingSet:
        all_words.extend(words)

    word_features = list(set(all_words))
    return word_features


def extract_features(text):
    text_words = set(text)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text_words)
    return features


trainingData = []
f = open('trainingSet.csv', 'r')
reader = csv.reader(f)
for i in reader:
    d = {'text': i[0], 'label': i[1]}
    trainingData.append(d)

textProcessor = PreProcessText()
preprocessedTrainingSet = textProcessor.processText(trainingData)

word_features = buildVocabulary(preprocessedTrainingSet)

trainingFeatures = nltk.classify.apply_features(extract_features, preprocessedTrainingSet)
NBayesClassifier = nltk.NaiveBayesClassifier.train(trainingFeatures)

with open('media/wordFeature.pickle', 'wb') as word_features_file:
    pickle.dump(word_features, word_features_file)

with open('media/classifier.pickle', 'wb') as classifier_file:
    pickle.dump(NBayesClassifier, classifier_file)
