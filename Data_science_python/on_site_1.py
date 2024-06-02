prices = [15,12,11,10,3]

def cal_profit(prices):
    result = {"buying":0,"selling":0,"profit":0}
    for index,buy in enumerate( prices ):
        for sell in prices[index:]:
            if buy < sell and sell - buy > result["profit"]:
                result["buying"],result["selling"],result["profit"] = buy,sell,sell-buy
    return result

print(cal_profit(prices))
