#!/usr/bin/env python3

# All import
# from concurrent.futures import ThreadPoolExecutor
import json
import os
from pprint import pprint
import numpy as np

import nltk
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas.compat import sys
from pandas.core.api import DataFrame
from PIL import Image
from wordcloud import WordCloud

VOCAB_SIZE = 2500


def to_binary(text):
    return "".join([format(ord(t), "08b") for t in text])


def email_body(directory):
    filenames = list()
    body = str()
    for filename in os.listdir(directory):
        filenames.append(os.path.join(directory, filename))
    for filename in filenames:
        ff = filename.split("/")
        with open(filename, encoding="latin-1") as file:
            lines = file.readlines()
            for i, t in enumerate(lines):
                if t == "\n":
                    body = "".join(lines[i + 1 :])
                    break
            file.close()
        yield {"filename": ff[-1], "message": body}
        body = str()
    return None


def email_body_df(path: dict):
    body = email_body(path["path"])
    rows = list()
    row_name = list()
    for eb in body:
        rows.append({"MESSAGE": eb["message"], "CLASSIFIER": path["classifier"]})
        row_name.append(eb["filename"])
    df = pd.DataFrame(rows, index=row_name)  # type: ignore
    return df


def update_nltk():
    to_download_list = ["punkt", "punkt_tab", "stopwords"]
    for download in to_download_list:
        nltk.download(download, quiet=True)


def pre_processing(data):
    update_nltk()
    pre_processed_data = list()
    stemmer = PorterStemmer()
    stop_words = stopwords.words("english")
    data = BeautifulSoup(data, "html.parser").get_text()
    for word in set(word_tokenize(data.lower())):
        if word not in stop_words and word.isalpha():
            stemmed_word = stemmer.stem(word)
            pre_processed_data.append(stemmed_word)
    return pre_processed_data


def clean_data(data: DataFrame, save_file_path: str, save_to_file: bool = False):
    data.drop(list(set(data[data["MESSAGE"].str.len() == 0].index)), inplace=True)
    document_ids = range(len(data))
    data["DOC_ID"] = document_ids
    data["FILE_NAME"] = data.index
    data.set_index("DOC_ID", inplace=True)
    data["MESSAGE"] = data["MESSAGE"].apply(pre_processing)
    if save_to_file:
        json_data = json.loads(str(data.to_json()))
        with open(save_file_path, "w") as file:
            file.write(json.dumps(json_data, indent=4))
            file.close()
    return data


def joiner(data):
    result = {
        "WORDS": [],
        "CLASSIFIER": [],
    }
    for words, classifier in data[["MESSAGE", "CLASSIFIER"]].values:
        for word in words:
            result["WORDS"].append(word)
            result["CLASSIFIER"].append(classifier)
    return pd.DataFrame(result)


def get_data(
    directory_paths: dict,
    save_file_path: str,
    vocab_df_path: str | None = None,
    save_to_file: bool = True,
    _from: int | None = None,
    _to: int | None = None,
    _stap: int | None = None,
):
    try:
        if os.path.exists(save_file_path):
            with open(save_file_path) as file:
                content = file.read()
                if len(content.strip()) == 0:
                    raise
        else:
            raise
    except:
        print(f"This data file is empty...")
        print(f"Genrating data...")
        emails = dict()
        for path in list(directory_paths.values())[_from:_to:_stap]:
            if not os.path.exists(path["path"]):
                raise ValueError("Wrong directory path.")
            if emails.get(path["classifier"]) is None:
                emails[path["classifier"]] = email_body_df(path)
            else:
                emails[path["classifier"]] = emails[path["classifier"]]._append(
                    email_body_df(path)
                )
        all_email = pd.concat(emails.values())
        cleaned_data = clean_data(all_email, save_file_path, save_to_file=save_to_file)
    else:
        cleaned_data = pd.read_json(save_file_path)

    all_words = joiner(cleaned_data)
    doc_ids_ham = cleaned_data[cleaned_data["CLASSIFIER"] == 0].index
    doc_ids_spam = cleaned_data[cleaned_data["CLASSIFIER"] == 1].index
    all_ham_words = joiner(cleaned_data.loc[doc_ids_ham])
    all_spam_words = joiner(cleaned_data.loc[doc_ids_spam])
    ham_word_count = pd.Series(all_ham_words.WORDS).value_counts()
    ham_word_set = pd.DataFrame(
        {"WORDS": ham_word_count.index, "COUNT": ham_word_count.values},
        index=range(1, ham_word_count.shape[0] + 1),
    )
    ham_word_set.index.name = "WORD_ID"
    spam_word_count = pd.Series(all_spam_words.WORDS).value_counts()
    spam_word_set = pd.DataFrame(
        {"WORDS": spam_word_count.index, "COUNT": spam_word_count.values},
        index=range(1, spam_word_count.shape[0] + 1),
    )
    spam_word_set.index.name = "WORD_ID"
    try:
        if vocab_df_path:
            with open(vocab_df_path) as file:
                vocabs = file.read()
                if len(vocabs.strip()) == 0:
                    raise
        else:
            raise
    except:
        print(f"The vocab data file is empty...")
        print(f"Genrating data...")
        unique_words = pd.Series(all_words.WORDS).value_counts()
        vocab_set = pd.DataFrame(
            {"VOCAB_WORDS": unique_words.index, "COUNT": unique_words.values},
            index=range(1, unique_words.shape[0] + 1),
        )
        vocab_set.index.name = "WORD_ID"
        if vocab_df_path:
            vocab_set_json = json.loads(str(vocab_set.to_json()))
            with open(vocab_df_path, "w") as file:
                file.write(json.dumps(vocab_set_json, indent=4))
                file.close()

    else:
        vocab_set = pd.read_json(vocab_df_path)

    result = {
        "data": cleaned_data,
        "vocab_set": vocab_set,
        "ham_set": ham_word_set,
        "spam_set": spam_word_set,
        "all_words": all_words,
        "all_ham_wprds": all_ham_words,
        "all_spam_wprds": all_spam_words,
    }

    return result


def checker(word, df_in, column):
    top_2500 = set(df_in[column][:VOCAB_SIZE].values)
    if word in top_2500:
        print(f"Yes : {word}")
    else:
        print(f"No  : {word}")


# Main function.
def main(
    directory_paths: dict,
    save_file_path: str,
    vocab_df_path: str | None = None,
    graph: bool = False,
    save_to_file: bool = True,
    _from: int | None = None,
    _to: int | None = None,
    _stap: int | None = None,
):

    all_data = get_data(
        directory_paths=directory_paths,
        save_file_path=save_file_path,
        save_to_file=save_to_file,
        vocab_df_path=vocab_df_path,
        _from=_from,
        _to=_to,
        _stap=_stap,
    )

    data = all_data["data"]
    vocab_set = all_data["vocab_set"]
    ham_set = all_data["ham_set"]
    spam_set = all_data["spam_set"]
    all_words = all_data["all_words"]

    if graph:
        amount_of_ham = data["CLASSIFIER"].value_counts()[0]
        amount_of_spam = data["CLASSIFIER"].value_counts()[1]
        print(amount_of_spam)
        print(amount_of_ham)
        category_name = ["Spam", "Legit Mails"]
        sizes = [amount_of_spam, amount_of_ham]
        custom_colors = [
            "#9b59b6",
            "#2ecc71",
        ]
        plt.pie(
            sizes,
            labels=category_name,
            textprops={"fontsize": 15},
            startangle=90,
            autopct="%1.0f%%",
            colors=custom_colors,
            pctdistance=0.8,
            # explode=[0, 0.05],
        )
        circle = plt.Circle((0, 0), radius=0.5, color="white")  # type: ignore
        plt.gca().add_artist(circle)
        plt.show()

    all_words2 = joiner(data)
    print(all_words2.value_counts().reset_index())
    print(all_words2["WORDS"].value_counts().reset_index())

    # words = ["mechine", "learning", "fun", "learn", "data", "science", "app", "brewery"]
    # for word in words:
    #     checker(word, vocab_set, "VOCAB_WORDS")

    # print(vocab_set)

    # print(data.MESSAGE.apply(len).max())

    return data


directorys = [
    ("./SpamData/01_Processing/spam_assassin_corpus/easy_ham_1/", 0),
    ("./SpamData/01_Processing/spam_assassin_corpus/easy_ham_2/", 0),
    ("./SpamData/01_Processing/spam_assassin_corpus/spam_1/", 1),
    ("./SpamData/01_Processing/spam_assassin_corpus/spam_2/", 1),
]

cwd = os.getcwd()
file_paths = {
    path.split("/")[-2]: {"path": os.path.join(cwd, path[2:]), "classifier": classifier}
    for path, classifier in directorys
}

main(
    directory_paths=file_paths,
    save_file_path="./16_clened_data.json",
    vocab_df_path="./16_vocab_dataframe.json",
)
