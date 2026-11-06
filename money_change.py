n = 1000 - int(input())
coin_list = [500,100,50,10,5,1]

# 1) [iteration]
# result_coin_cnt = 0

# for coin in coin_list:
#     result_coin_cnt += n // coin
#     n %= coin

# print(result_coin_cnt)

# 2) [recursion]

def money_change(remain_money, i, coin_list):
    if i == len(coin_list):
        return 0    

    return (remain_money // coin_list[i]) + money_change(remain_money % coin_list[i], i+1, coin_list)

print(money_change(n, 0, coin_list))