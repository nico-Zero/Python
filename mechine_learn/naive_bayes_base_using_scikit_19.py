import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from pprint import pprint
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import precision_score, recall_score, f1_score
from mimesis.locales import Locale
import mimesis

JSON_DATA_PATH = "./SpamData/01_Processing/email-text-data.json"

email_data = pd.read_json(JSON_DATA_PATH)

# # MESSAGE FILE_NAME CATEGORY
# print(email_data.tail())
# print(email_data.shape)

vectorize = CountVectorizer(stop_words="english")
all_features = vectorize.fit_transform(email_data["MESSAGE"])
# print(all_features.shape)

vocab_count = vectorize.vocabulary_
# pprint(vocab_count)

X_train, X_test, Y_train, Y_test = train_test_split(
    all_features,
    email_data["CATEGORY"],
    test_size=0.3,
    random_state=88,
)

# print(f"X_train:- {X_train.shape}")  # type: ignore
# print(f"X_test:- {X_test.shape}")  # type: ignore
# print(f"Y_test:- {Y_test.shape}")  # type: ignore
# print(f"Y_train:- {Y_train.shape}")  # type: ignore

classifier = MultinomialNB()
classifier.fit(X_train, Y_train)
predection = classifier.predict(X_test)
num_correct = (Y_test == predection).sum()
num_incorrect = Y_test.size - num_correct  # type: ignore
correct_score = classifier.score(X_test, Y_test)
incorrect_score = 1 - correct_score
recall = recall_score(Y_test, predection)
precision = precision_score(Y_test, predection)
f1 = f1_score(Y_test, predection)

# print(f"Number of Correct Prediction:- {num_correct}")
# print(f"Number of Incrrect Prediction:- {num_incorrect}")
# print(f"Corract score:- {correct_score:.3f}")
# print(f"Incorract score:- {incorrect_score:.3f}")

# print("Recall:- ", recall)
# print("Precision:- ", precision)
# print("F1:- ", f1)

text = mimesis.Text(Locale.EN)

example = [text.text(quantity=50) for _ in range(100)]

jjjj = vectorize.transform(example)

jjjjpp = classifier.predict(jjjj)

print(jjjjpp)
