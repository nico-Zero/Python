#!/usr/bin/env python3

# All import
# from concurrent.futures import ThreadPoolExecutor
import json
import os
from pprint import pprint
from tkinter import Message
import numpy as np
from copy import deepcopy

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
from pandas.core.common import random_state
from pandas.io.formats.format import save_to_buffer
from wordcloud import WordCloud
from sklearn.model_selection import train_test_split

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
    pre_processed_data = list()
    stemmer = PorterStemmer()
    stop_words = stopwords.words("english")
    data = BeautifulSoup(data, "html.parser").get_text()
    for word in set(word_tokenize(data.lower())):
        if word not in stop_words and word.isalpha():
            stemmed_word = stemmer.stem(word)
            pre_processed_data.append(stemmed_word)
    return pre_processed_data


def clean_data(
    data: DataFrame,
    clean_save_file_path: str,
    unclean_save_file_path: str,
    save_to_file: bool = False,
):
    data.drop(list(set(data[data["MESSAGE"].str.len() == 0].index)), inplace=True)
    document_ids = range(len(data))
    data["DOC_ID"] = document_ids
    data["FILE_NAME"] = data.index
    data.set_index("DOC_ID", inplace=True)
    unclened_data = deepcopy(data)
    data["MESSAGE"] = data["MESSAGE"].apply(pre_processing)
    if save_to_file:
        clean_json_data = json.loads(str(data.to_json()))
        with open(clean_save_file_path, "w") as cfile:
            cfile.write(json.dumps(clean_json_data, indent=4))
            cfile.close()
        unclean_json_data = json.loads(str(unclened_data.to_json()))
        with open(unclean_save_file_path, "w") as ufile:
            ufile.write(json.dumps(unclean_json_data, indent=4))
            ufile.close()
    return (unclened_data, data)


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


def get_train_test_data(data, target):
    x_train, x_test, y_train, y_test = train_test_split(
        data, target, test_size=0.3, random_state=42
    )
    return (x_train, x_test, y_train, y_test)


def get_data(
    directory_paths: dict,
    clean_save_file_path: str,
    unclean_save_file_path: str,
    vocab_df_path: str | None = None,
    save_to_file: bool = True,
    _from: int | None = None,
    _to: int | None = None,
    _stap: int | None = None,
):
    try:
        if os.path.exists(clean_save_file_path) and os.path.exists(
            unclean_save_file_path
        ):
            with open(clean_save_file_path) as cfile:
                content = cfile.read()
                if len(content.strip()) == 0:
                    print(f"{clean_save_file_path} is Empty...")
                    raise
            with open(unclean_save_file_path) as ufile:
                content = ufile.read()
                if len(content.strip()) == 0:
                    print(f"{unclean_save_file_path} is Empty...")
                    raise
        else:
            print(f"{clean_save_file_path} | {unclean_save_file_path} Not Found...")
            raise
    except:
        print(f"Gatherings data...")
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
        data = clean_data(
            all_email,
            clean_save_file_path,
            unclean_save_file_path,
            save_to_file=save_to_file,
        )
        unclened_data = data[0]
        cleaned_data = data[1]
    else:
        unclened_data = pd.read_json(unclean_save_file_path)
        cleaned_data = pd.read_json(clean_save_file_path)

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
            with open(vocab_df_path) as cfile:
                vocabs = cfile.read()
                if len(vocabs.strip()) == 0:
                    print(f"{vocab_df_path} is Empty...")
                    raise
        else:
            print(f"{vocab_df_path} Not Found...")
            raise
    except:
        print(f"Gatherings data...")
        unique_words = pd.Series(all_words.WORDS).value_counts()
        vocab_set = pd.DataFrame(
            {"VOCAB_WORDS": unique_words.index, "COUNT": unique_words.values},
            index=range(1, unique_words.shape[0] + 1),
        )
        vocab_set.index.name = "WORD_ID"
        if vocab_df_path:
            vocab_set_json = json.loads(str(vocab_set.to_json()))
            with open(vocab_df_path, "w") as cfile:
                cfile.write(json.dumps(vocab_set_json, indent=4))
                cfile.close()

    else:
        vocab_set = pd.read_json(vocab_df_path)

    top_words = all_words["WORDS"].value_counts()[:VOCAB_SIZE]
    top_ham_words = all_ham_words["WORDS"].value_counts()[:VOCAB_SIZE]
    top_spam_words = all_spam_words["WORDS"].value_counts()[:VOCAB_SIZE]

    vocab_class_count_data = deepcopy(cleaned_data[["MESSAGE", "CLASSIFIER"]].explode("MESSAGE").value_counts(["MESSAGE", "CLASSIFIER"]).reset_index())  # type: ignore
    vocab_class_count_data.rename(
        columns={"MESSAGE": "WORDS", "count": "COUNT"}, inplace=True
    )

    top_words_index = top_words.index  # type: ignore
    top_ham_words_index = top_ham_words.index  # type: ignore
    top_spam_words_index = top_spam_words.index  # type: ignore

    word_sheet = pd.DataFrame.from_records(cleaned_data["MESSAGE"].tolist())
    x_train, x_test, y_train, y_test = get_train_test_data(
        cleaned_data["MESSAGE"], cleaned_data["CLASSIFIER"]
    )

    train_sparse_matrix = make_sparse_matrix(x_train, y_train, top_words_index)  # type: ignore
    test_sparse_matrix = make_sparse_matrix(x_test, y_test, top_words_index)  # type: ignore

    with open("16_train_data.json", "w") as tfile:
        train_json_data = json.loads(str(train_sparse_matrix.to_json()))
        tfile.write(json.dumps(train_json_data, indent=4))
        tfile.close()
    with open("16_test_data.json", "w") as tfile:
        test_json_data = json.loads(str(test_sparse_matrix.to_json()))
        tfile.write(json.dumps(test_json_data, indent=4))
        tfile.close()

    result = {
        "unclean_data": unclened_data,
        "clean_data": cleaned_data,
        "vocab_set": vocab_set,
        "ham_set": ham_word_set,
        "spam_set": spam_word_set,
        "all_words": all_words,
        "all_ham_words": all_ham_words,
        "all_spam_words": all_spam_words,
        "top_words": top_words,
        "top_ham_words": top_ham_words,
        "top_spam_words": top_spam_words,
        "top_words_index": top_words_index,
        "top_ham_words_index": top_ham_words_index,
        "top_spam_words_index": top_spam_words_index,
        "vocab_class_count_data": vocab_class_count_data,
        "word_sheet": word_sheet,
        "train_data": {
            "x_train": x_train,
            "y_train": y_train,
            "train_sparse_matrix": train_sparse_matrix,
        },
        "test_data": {
            "x_test": x_test,
            "y_test": y_test,
            "test_sparse_matrix": test_sparse_matrix,
        },
    }

    return result


def checker(word, df_in, column):
    top_2500 = set(df_in[column][:VOCAB_SIZE].values)
    if word in top_2500:
        print(f"Yes : {word}")
    else:
        print(f"No  : {word}")
    return None


def make_graph(data):
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


def make_sparse_matrix(data: pd.Series, target: pd.Series, index: pd.Index):
    result = (
        pd.DataFrame(
            {"MESSAGE_ID": data.index, "MESSAGE": data.values, "CLASSIFIER": target}
        )
        .explode("MESSAGE")
        .value_counts(["MESSAGE_ID", "MESSAGE", "CLASSIFIER"])
        .reset_index()
    )
    result.rename(
        columns={"MESSAGE": "WORD_ID", "count": "COUNT"},
        inplace=True,
    )
    result["WORD_ID"] = result["WORD_ID"].map({word: i for i, word in enumerate(index.tolist())})  # type: ignore
    result.dropna(subset=["WORD_ID"], inplace=True)
    result["WORD_ID"] = result["WORD_ID"].astype(int)
    result.sort_values(["MESSAGE_ID", "WORD_ID", "CLASSIFIER", "COUNT"], inplace=True)
    result.reset_index(drop=True, inplace=True)
    return result


# Main function.
def main(
    directory_paths: dict,
    clean_save_file_path: str,
    unclean_save_file_path: str,
    vocab_df_path: str | None = None,
    graph: bool = False,
    save_to_file: bool = True,
    _from: int | None = None,
    _to: int | None = None,
    _stap: int | None = None,
):

    all_data = get_data(
        directory_paths=directory_paths,
        clean_save_file_path=clean_save_file_path,
        unclean_save_file_path=unclean_save_file_path,
        save_to_file=save_to_file,
        vocab_df_path=vocab_df_path,
        _from=_from,
        _to=_to,
        _stap=_stap,
    )

    unclened_data = all_data["unclean_data"]
    cleaned_data = all_data["clean_data"]
    vocab_set = all_data["vocab_set"]
    ham_set = all_data["ham_set"]
    spam_set = all_data["spam_set"]
    all_words = all_data["all_words"]
    top_words = all_data["top_words"]
    top_ham_words = all_data["top_ham_words"]
    top_spam_words = all_data["top_spam_words"]
    vocab_class_count_data = all_data["vocab_class_count_data"]
    top_words_index = all_data["top_words_index"]
    top_ham_words_index = all_data["top_ham_words_index"]
    top_spam_words_index = all_data["top_spam_words_index"]
    train_data = all_data["train_data"]
    test_data = all_data["test_data"]
    train_sparse_matrix = all_data["train_data"]["train_sparse_matrix"]
    test_sparse_matrix = all_data["test_data"]["test_sparse_matrix"]

    if graph:
        make_graph(cleaned_data)

    # ham_set print("X Train data:- ", train_data["x_train"])  # type: ignore
    # print("X Train data:- ", train_data["y_train"])  # type: ignore
    # print("X Test data:- ", test_data["x_test"])  # type: ignore
    # print("X Test data:- ", test_data["y_test"])  # type: ignore

    # print(top_words)
    # print(vocab_class_count_data)
    # print(top_words_index)
    # print(data)
    # print(vocab_set)

    print(train_sparse_matrix)
    print(test_sparse_matrix)
    # print(top_words_index[309])
    # print(top_words_index[884])
    # print(top_words_index[96])

    return None


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
    clean_save_file_path="./16_clean_data.json",
    unclean_save_file_path="./16_unclean_data.json",
    vocab_df_path="./16_vocab_dataframe.json",
    graph=False,
)
