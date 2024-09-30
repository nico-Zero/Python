#!/usr/bin/env python3

# All import
# from concurrent.futures import ThreadPoolExecutor
import json
import os
from pprint import pprint

import nltk
import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize
from pandas.compat import sys
from pandas.core.api import DataFrame
from wordcloud import WordCloud


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


def get_clened_data(
    directory_paths: dict,
    save_file_path: str,
    save_to_file: bool = True,
    _from: int | None = None,
    _to: int | None = None,
    _stap: int | None = None,
):
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
    return cleaned_data


def joiner(words):
    result = []
    for dd in words:
        result += dd
    return result


# Main function.
def main(
    directory_paths: dict,
    save_file_path: str,
    graph: bool = False,
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
                    print(f"This '{save_file_path}' is empty...")
                    raise
        else:
            raise
    except:
        data = get_clened_data(
            directory_paths=directory_paths,
            save_file_path=save_file_path,
            save_to_file=save_to_file,
            _from=_from,
            _to=_to,
            _stap=_stap,
        )
    else:
        data = pd.read_json(save_file_path)
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
    doc_ids_ham = data[data["CLASSIFIER"] == 0].index
    doc_ids_spam = data[data["CLASSIFIER"] == 1].index
    all_words = joiner(data["MESSAGE"])
    all_ham_words = joiner(data["MESSAGE"].loc[doc_ids_ham])
    all_spam_words = joiner(data["MESSAGE"].loc[doc_ids_spam])
    ham_word_count = pd.Series(all_ham_words).value_counts()
    spam_word_count = pd.Series(all_spam_words).value_counts()

    # print("Total ham words count:- ", len(all_ham_words))
    # print("Total spam words count:- ", len(all_spam_words))
    # print("Total words count:- ", len(all_words))
    # print("Top 10 word count in ham words:- \n", ham_word_count[:10], "\n", sep="")
    # print("Top 10 word count in spam words:- \n", spam_word_count[:10], "\n", sep="")

    word_cloud = WordCloud().generate(" ".join(all_words))
    plt.imshow(word_cloud, interpolation="bilinear")
    plt.axis("off")
    plt.show()

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

main(directory_paths=file_paths, save_file_path="./16_clened_data.json")
