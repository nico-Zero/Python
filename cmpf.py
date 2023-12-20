import pandas as pd

test = {
    "1996": {"pf":2519,"interest": 0.12},
    "1997": {"pf":4988,"interest": 0.12},
    "1998": {"pf":5549,"interest": 0.12},
    "1999": {"pf":5751,"interest": 0.12},
    "2000": {"pf":6242,"interest": 0.12},
    "2001": {"pf":7084,"interest": 0.11},
    "2002": {"pf":12364, "interest":0.095},
    "2003": {"pf":10811,"interest": 0.09},
    "2004": {"pf":11465,"interest": 0.08},
    "2005": {"pf":13888, "interest":0.085},
    "2006": {"pf":15642,"interest": 0.08},
    "2007": {"pf":23717, "interest":0.085},
    "2008": {"pf":23769, "interest":0.085},
    "2009": {"pf":25381, "interest":0.085},
    "2010": {"pf":43804, "interest":0.085},
    "2011": {"pf":42922, "interest":0.085},
    "2012": {"pf":48520, "interest":0.085},
    "2013": {"pf":71266, "interest":0.085},
    "2014": {"pf":72546, "interest":0.085},
    "2015": {"pf":90265, "interest":0.085},
    "2016": {"pf":95048, "interest":0.085},
    "2017": {"pf":92844, "interest":0.086},
    "2018": {"pf":99141, "interest":0.085},
    "2019": {"pf":134952, "interest":0.086},
    "2020": {"pf":127359, "interest":0.085},
    "2021": {"pf":134346, "interest":0.085},
    "2022": {"pf":165111,"interest": 0.08},
}


total = 0

for i,j in test.items():
    print(i,total,sep="  -  ")
    interest = j["interest"] * total
    total += (j["pf"] * 2) + interest

print(total)