import pandas as pd
import numpy as np

VOCAB_LEN = 2500

clean_data_path = "16_clean_data.json"
test_data_path = "16_test_data.json"
train_data_path = "16_train_data.json"
unclean_data_path = "16_unclean_data.json"
vocab_dataframe_path = "16_vocab_dataframe.json"

train_data = pd.read_json(train_data_path)
test_data = pd.read_json(test_data_path)

# How to create an empty dataframe.
pd.set_option("future.no_silent_downcasting", True)


def make_full_matrix(
    sparse_matrix: pd.DataFrame,
):
    """
    From Nd Array of Sparse matrix to a Full matrix for data processin gfor the predection of the email being a spam of not.
    """
    data = sparse_matrix.pivot_table(
        index=["MESSAGE_ID", "CLASSIFIER"],
        values="COUNT",
        columns="WORD_ID",
        fill_value=0,
    )
    data.reset_index(inplace=True)
    data.columns.name = None
    data = data.astype(int, copy=True)

    return data


full_matrix = make_full_matrix(train_data)

x = list(full_matrix.value_counts("CLASSIFIER"))
spam_percentage = x[1] / sum(x)

sub_full_matrix = full_matrix.loc[:, full_matrix.columns != "CLASSIFIER"]
# print(sub_full_matrix)
jj = sub_full_matrix.sum(
    axis=1,
)
print(jj)
