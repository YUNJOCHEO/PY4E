Q3.
import operator

# 손익(%) = (판매가 * 100 / 구매가) - 100

stocks = "삼성전자/10/85000,카카오/15/130000,LG화학/3/820000,NAVER/5/420000"
sells = [82000, 160000, 835000, 410000]


def stock_profit_loss(my_stocks, my_sells):
    stocks_list = my_stocks.split(',')
    profit_loss = {}
    for stock in range(len(stocks_list)):
        name, quantity, price = stocks_list[stock].split('/')
        profit_loss[name] = round((my_sells[stock] * 100 / int(price)) - 100, 2)

    sor_pro_loss = sorted(profit_loss.items(), key=operator.itemgetter(1), reverse=True)

    for name, per in sor_pro_loss:
        print(f'{name}의 수익률 {per}')


stock_profit_loss(stocks, sells)