from pprint import pprint
from bayes_data_parse_17 import all_train_calc, all_test_calc  # type: ignore
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns


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
simplify_joint_log_spam = x_test_array.dot(
    np.log(propablity_of_spam_token.to_numpy())
) + np.log(propablity_of_spam)
simplify_joint_log_ham = x_test_array.dot(
    np.log(propablity_of_ham_token.to_numpy())
) + np.log(1 - propablity_of_spam)

propability = joint_log_spam > joint_log_ham
simplify_propability = simplify_joint_log_spam > simplify_joint_log_ham

# print(
#     "Is spam propability is grater then the ham propability",
#     sum(propability) - len(propability) > sum(propability),
# )
# print(
#     "Is ham propability is grater then the spam propability",
#     sum(propability) - len(propability) < sum(propability),
# )
# print(
#     "Is simplify_spam propability is grater then the simplify_ham propability",
#     sum(simplify_propability) - len(simplify_propability) > sum(simplify_propability),
# )
# print(
#     "Is simplify_ham propability is grater then the simplify_spam propability",
#     sum(simplify_propability) - len(simplify_propability) < sum(simplify_propability),
# )

# print(joint_log_ham)
# print(joint_log_spam)
# print(simplify_joint_log_ham)
# print(simplify_joint_log_spam)


## Metrics and evalution of the model of spam classifire.
correct_docs = (y_test.to_numpy() == propability).sum()
number_of_wrong = len(y_test) - correct_docs

accuracy = correct_docs / len(x_test)
unaccurate = number_of_wrong / len(x_test)

# print("Correct Docs Number:- ", corract_docs)
# print("Incorrect Docs Number:- ", number_of_wrong)
# print("Out of:- ", len(y_test))

# print(f"The accuracy of predection is {accuracy*100:.2f}")
# print(f"The unaccuracy of predection is {unaccurate*100:.2f}")


yaxis_lable = "P(X | Spam)"
xaxis_lable = "P(X | Non-Spam)"
linedata = np.linspace(start=-14000, stop=1, num=1000)


def pyplot_show():
    plt.subplot(1, 2, 1)
    plt.xlabel(xaxis_lable, fontsize=14)
    plt.ylabel(yaxis_lable, fontsize=14)
    plt.xlim([-14000, 1])
    plt.ylim([-14000, 1])
    plt.scatter(
        simplify_joint_log_ham, simplify_joint_log_spam, color="navy", alpha=0.4, s=25
    )
    # plt.scatter(joint_log_ham, joint_log_spam, color="navy")
    plt.plot(linedata, linedata, color="orange")
    plt.subplot(1, 2, 2)
    plt.xlabel(xaxis_lable, fontsize=14)
    plt.ylabel(yaxis_lable, fontsize=14)
    plt.xlim([-2000, 1])
    plt.ylim([-2000, 1])
    plt.scatter(
        simplify_joint_log_ham, simplify_joint_log_spam, color="navy", alpha=0.4, s=3
    )
    # plt.scatter(joint_log_ham, joint_log_spam, color="navy")
    plt.plot(linedata, linedata, color="orange")
    plt.show()


def seabor_show():
    sns.set_style("whitegrid")
    labels = "Actual Category"
    summry_df = pd.DataFrame(
        {
            yaxis_lable: simplify_joint_log_spam,
            xaxis_lable: simplify_joint_log_ham,
            labels: y_test,
        }
    )
    sns.lmplot(
        x=xaxis_lable,
        y=yaxis_lable,
        data=summry_df,
        fit_reg=False,
        scatter_kws={"alpha": 0.4, "s": 25},
        hue=labels,
        markers=["o", "x"],  # type: ignore
        # palette="hls",
        legend=False,
    )
    plt.xlim([-2000, 1])
    plt.ylim([-2000, 1])
    plt.plot(linedata, linedata, color="black")
    plt.legend(
        (
            "Non-Spam",
            "Spam",
            "Decision Boundary",
        ),
        loc="lower right",
        fontsize=14,
    )
    plt.show()
    return None


# pyplot_show()
# seabor_show()

# unique_propability = np.unique(propability, return_counts=True)
# print(unique_propability)

# Emall said to be SPAM but found to be SPAM.
true_pos = (y_test_array == 1) & (propability == 1)
true_pos_sum = true_pos.sum()

# Emall said to be SPAM but found to be NOT-SPAM.
true_neg = (y_test_array == 1) & (propability == 0)
true_neg_sum = true_neg.sum()

# Emall said to be SPAM but found to be NOT-SPAM.
false_pos = (y_test_array == 1) & (propability == 0)
false_pos_sum = false_pos.sum()

# Emall said to be NOT-SPAM but found to be SPAM.
false_neg = (y_test_array == 0) & (propability == 1)
false_neg_sum = false_neg.sum()

print("True pos sum:- ", true_pos_sum)
print("True neg sum:- ", true_neg_sum)
print("False pos sum:- ", false_pos_sum)
print("False neg sum:- ", false_neg_sum)

recall_score = true_pos_sum / (true_pos_sum + false_neg_sum)
print(f"Recall score:- {recall_score:.3f}")

precision_score = true_pos_sum / (true_pos_sum + false_pos_sum)
print(f"Precision scroe:- {precision_score:.3f}")

f_score = 2 * (precision_score * recall_score) / (precision_score + recall_score)
print(f"F score:- {f_score:.3f}")
