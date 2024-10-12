from pprint import pprint
from bayes_data_parse_17 import all_train_calc, all_test_calc  # type: ignore
import pandas as pd
import numpy as np


x_test: pd.DataFrame = all_test_calc["sub_matrix"]
y_test: pd.Series = all_test_calc["full_matrix"]["CLASSIFIER"]
propablity_of_all: pd.Series = all_test_calc["propablity_of_all"]
propablity_of_ham: pd.Series = all_test_calc["propablity_of_ham"]
propablity_of_spam: pd.Series = all_test_calc["propablity_of_spam"]

x_test_array = x_test.to_numpy()
y_test_array = y_test.to_numpy()

print(x_test_array)
print(x_test_array)
