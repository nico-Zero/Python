import typing
from pprint import pprint

import numpy as np
import pandas as pd
from pandas.io.parsers.readers import csv
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, root_mean_squared_error


class ValidationSystem:
    def __init__(
        self,
        data_path: str,
        target_axis: str,
        data_drop: list = [],
        data_drop_axis=1,
        target_function=None,
        feature_function=None,
        default_prediction_feature: typing.Literal["mean", "max", "min"] = "mean",
        prediction_feature: dict | None = None,
        high_confidence=False,
        low_confidence=False,
    ):
        self.data = pd.read_csv(data_path)
        self.target = (
            pd.DataFrame(target_function(self.data[target_axis]), columns=[target_axis])  # type: ignore
            if target_function
            else self.data[target_axis]
        )
        self.feature = (
            feature_function(
                self.data.drop([target_axis, *data_drop], axis=data_drop_axis)
            )
            if feature_function
            else self.data.drop([target_axis, *data_drop], axis=data_drop_axis)
        )
        self.data_droped = data_drop
        self.data_droped_axis = data_drop_axis
        self.to_predict = {}
        self.all_axis = list(self.feature.keys())

        # making the predection values for predecting the target values and combining it with the default predection values
        for name in self.all_axis:
            self.to_predict[name] = round(
                eval(f"self.feature['{name}'].{default_prediction_feature}()"), 3
            )
        for name, value in prediction_feature.items() if prediction_feature else {}:
            if name in self.all_axis:
                self.to_predict[name] = value

        self.to_predict_values = pd.DataFrame(self.to_predict, index=[0])  # type: ignore
        self.high_confidence = high_confidence
        self.low_confidence = low_confidence

    def values_head(self):
        values = {"target": self.target.head(), "feature": self.feature.head()}
        return values

    def values(self):
        values = {"target": self.target, "feature": self.feature}
        return values

    def describe(self):
        values = {"target": self.target.describe(), "feature": self.feature.describe()}
        return values

    def info(self):
        values = {
            "data_dropped": self.data_droped,
            "data_dropped_axis": self.data_droped_axis,
            "target": self.target.describe(),
            "feature": self.feature.describe(),
            "to_predict": self.to_predict,
        }
        return values

    def shape(self):
        values = {"target": self.target.shape, "feature": self.feature.shape}
        return values

    def __regression_fit(self):
        regr = LinearRegression().fit(self.feature, self.target)
        return regr

    def prediction(self, high_confidence=False, low_confidence=False):
        regr = self.__regression_fit()

        today_doller = 8.11

        # pridecting the price
        predict = regr.predict(self.to_predict_values)[0][0]
        predicted_value = round((np.e ** (predict)) * 1000 * today_doller, 3)

        # fitting all the features as predection
        fitted_values = regr.predict(self.feature)

        # mean square error
        mse = mean_squared_error(self.target, fitted_values)

        # root mean square error
        rmse = np.sqrt(mse)
        high_confidence = high_confidence or self.high_confidence

        # calculating range of pridection.
        if high_confidence is True:
            high_confidence_range = {
                "upper_bound": round(
                    ((np.e ** (predict + 2 * rmse)) * 1000 * today_doller), 3
                ),
                "lower_bound": round(
                    ((np.e ** (predict - 2 * rmse)) * 1000 * today_doller), 3
                ),
                "percentile": 95,
            }
        else:
            high_confidence_range = None

        if low_confidence is True:
            low_confidence_range = {
                "upper_bound": round(
                    ((np.e ** (predict + rmse)) * 1000 * today_doller), 3
                ),
                "lower_bound": round(
                    ((np.e ** (predict - rmse)) * 1000 * today_doller), 3
                ),
                "percentile": 68,
            }
        else:
            low_confidence_range = None

        result = {
            "predicted": predicted_value,
            "mse": mse,
            "rmse": rmse,
            "high_confidence_range": high_confidence_range,
            "low_confidence_range": low_confidence_range,
        }
        return result


def main():
    """
        CRIM     ZN       CHAS    NOX     RM       DIS       RAD    TAX       PTRATIO    B        LSTAT
    0   0.00632  18.0     0       0.538   6.575    4.0900    1      296.0     15.3       396.90   4.98
    1   0.02731   0.0     0       0.469   6.421    4.9671    2      242.0     17.8       396.90   9.14
    2   0.02729   0.0     0       0.469   7.185    4.9671    2      242.0     17.8       392.83   4.03
    3   0.03237   0.0     0       0.458   6.998    6.0622    3      222.0     18.7       394.63   2.94
    4   0.06905   0.0     1       0.458   7.147    6.0622    3      222.0     18.7       396.90   5.33
    """
    predect_feature = {"RM": 1, "PTRATIO": 1, "CRIM": 10}
    validation_system = ValidationSystem(
        data_path="./boston.csv",
        target_axis="PRICE",
        data_drop=["INDUS", "AGE"],
        target_function=np.log,
        default_prediction_feature="mean",
        prediction_feature=predect_feature,
    )
    pridected_value = validation_system.prediction(
        high_confidence=True, low_confidence=True
    )

    # print("predicted Value:- $", pridected_value, sep="")
    pprint(pridected_value)


main()
