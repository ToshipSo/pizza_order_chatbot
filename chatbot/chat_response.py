import pickle
import nltk
from string import punctuation

nltk.download('punkt')
from nltk.tokenize import word_tokenize

word_feature_file = open('media/wordFeature.pickle', 'rb')
word_features = pickle.load(word_feature_file)
word_feature_file.close()
classifier_file = open('media/classifier.pickle', 'rb')
classifier = pickle.load(classifier_file)
classifier_file.close()


def process_text(text):
    text = text.lower()
    text = word_tokenize(text)
    return [word for word in text if word not in punctuation]


def extract_features(text):
    text_words = set(text)
    features = {}
    for word in word_features:
        features['contains(%s)' % word] = (word in text_words)
    return features


def get_response(text):
    processed_text = process_text(text)
    features = extract_features(processed_text)
    label = classifier.classify(features)
    x = classifier.prob_classify(features).prob(label)
    if x < 0.80 or (x < 0.95 and label == '0'):
        return 10
    return int(label)
    # return x

# while True:
#     n = input()
#     res = get_response(n)
#     print(res)
