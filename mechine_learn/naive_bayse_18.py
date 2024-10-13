from pprint import pprint
from bayes_data_parse_17 import all_train_calc, all_test_calc  # type: ignore
import pandas as pd
import numpy as np


x_test: pd.DataFrame = all_test_calc["sub_matrix"]
y_test: pd.Series = all_test_calc["full_matrix"]["CLASSIFIER"]
propablity_of_all_token: pd.Series = all_test_calc["propablity_of_all"]
propablity_of_ham_token: pd.Series = all_test_calc["propablity_of_ham"]
propablity_of_spam_token: pd.Series = all_test_calc["propablity_of_spam"]
propablity_of_spam: int = all_test_calc["spam_percentage"]

x_test_array = x_test.to_numpy()
y_test_array = y_test.to_numpy()
joint_log_spam = x_test_array.dot(
    np.log(propablity_of_spam_token.to_numpy())
    - np.log(propablity_of_all_token.to_numpy())
) + np.log(propablity_of_spam)

joint_log_ham = x_test_array.dot(
    np.log(propablity_of_ham_token.to_numpy())
    - np.log(propablity_of_all_token.to_numpy())
) + np.log(1 - propablity_of_spam)


print(joint_log_spam)
print(joint_log_ham)
