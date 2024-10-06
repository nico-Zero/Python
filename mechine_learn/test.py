import pandas as pd

data = pd.read_json("./16_clened_data.json")
idata = pd.read_json("./16_vocab_dataframe.json")

jj = data[["MESSAGE", "CLASSIFIER"]].explode("MESSAGE").value_counts(["MESSAGE", "CLASSIFIER"])  # type: ignore
print(jj.reset_index())
