from comm.tool import Tools

tool = Tools()
number = tool.lottery_data_source()


# number = ['01488', '00236', '34301', '00001', '87363']  # ['00227','00236','34301','00001','87363']
# number = [ '00444']  #'00109', '00009', '81626', '98399',


def san_gong_right_idle(nums):
    ls = []
    for num in set(nums):
        left_idle = str(sum(list(map(int, num[0:3]))) % 10)
        right_idle = str(sum(list(map(int, num[-3:]))) % 10)
        if left_idle == '0' or right_idle == '0':
            new_left_idle = left_idle.replace('0', '10')
            new_right_idle = right_idle.replace('0', '10')
            if int(new_right_idle)>int(new_left_idle):
                ls.append(num)
        elif int(right_idle) > int(left_idle):
            ls.append(num)
    return ls


bet_detail = "[{\"numbers\":\"右闲\",\"betPrice\":50}]"
api_results = tool.get_split_api_double_sided('txffc', '20_11_10', bet_detail)
test_result = san_gong(number)
test_split_result = list({}.fromkeys(test_result).keys())

print('test_split_result', test_split_result)

# print('api_results', api_results)
api_split_result = []
for i in api_results[1]:
    lis = i.replace(',', '')
    api_split_result.append(lis)
api_split_result.sort()
print('api_split_result',api_split_result)
print('len', len(test_split_result))
print('len', len(api_split_result))

isTure = tool.check_split_equal(list(test_result),list(api_split_result))
print(isTure)
print(len(isTure[1]))
