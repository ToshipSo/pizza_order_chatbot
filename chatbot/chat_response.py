import pickle

import nltk

nltk.download('stopwords')
nltk.download('punkt')
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

word_feature_file = open('media/wordFeature.pickle', 'rb')
word_features = pickle.load(word_feature_file)
word_feature_file.close()
classifier_file = open('media/classifier.pickle', 'rb')
classifier = pickle.load(classifier_file)
classifier_file.close()


def process_text(text):
    text = text.lower()
    text = word_tokenize(text)
    return [word for word in text if word not in set(stopwords.words('english'))]


def extract_features(text):
    text_words = set(text)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text_words)
    return features


def get_response(text):
    processed_text = process_text(text)
    features = extract_features(processed_text)
    return classifier.classify(features)

