import pandas as pd

VOCAB_LEN = 2500

clean_data_path = "clean_data_16.json"
test_data_path = "test_data_16.json"
train_data_path = "train_data_16.json"
unclean_data_path = "unclean_data_16.json"
vocab_dataframe_path = "vocab_dataframe_16.json"

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


def calc(data):
    full_matrix = make_full_matrix(data)
    x = list(full_matrix.value_counts("CLASSIFIER"))
    spam_percentage = x[1] / sum(x)

    sub_matrix = full_matrix.loc[:, full_matrix.columns != "CLASSIFIER"]
    sub_matrix.set_index("MESSAGE_ID", inplace=True)
    tokan_count = sub_matrix.sum(
        axis=0,
    )
    total_tokans = tokan_count.sum()
    propablity_of_all = tokan_count / total_tokans

    ham_messages = full_matrix[full_matrix["CLASSIFIER"] == 0]
    ham_message_length = ham_messages.shape[0]
    ham_messages = ham_messages.loc[:, ham_messages.columns != "CLASSIFIER"]
    tokan_count_ham = (
        ham_messages.set_index("MESSAGE_ID", inplace=False).sum(axis=0) + 1
    )
    total_ham_tokens = tokan_count_ham.sum()
    propablity_of_ham = tokan_count_ham / (total_ham_tokens + VOCAB_LEN)

    spam_messages = full_matrix[full_matrix["CLASSIFIER"] == 1]
    spam_message_length = spam_messages.shape[0]
    spam_messages = spam_messages.loc[:, spam_messages.columns != "CLASSIFIER"]
    tokan_count_spam = (
        spam_messages.set_index("MESSAGE_ID", inplace=False).sum(axis=0) + 1
    )
    total_spam_tokens = tokan_count_spam.sum()
    propablity_of_spam = tokan_count_spam / (total_spam_tokens + VOCAB_LEN)

    result = {
        "full_matrix": full_matrix,
        "sub_matrix": sub_matrix,
        "ham_messages": ham_messages,
        "ham_message_length": ham_message_length,
        "spam_messages": spam_messages,
        "spam_message_length": spam_message_length,
        "spam_percentage": spam_percentage,
        "total_tokans": total_tokans,
        "tokan_count ": tokan_count,
        "total_ham_tokens": total_ham_tokens,
        "tokan_count_ham": tokan_count_ham,
        "total_spam_tokens": total_spam_tokens,
        "tokan_count_spam": tokan_count_spam,
        "propablity_of_all": propablity_of_all,
        "propablity_of_ham": propablity_of_ham,
        "propablity_of_spam": propablity_of_spam,
    }
    return result


all_train_calc = calc(train_data)
all_test_calc = calc(test_data)

# print(all_train_calc)
# print(all_test_calc)
