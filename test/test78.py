import time

from ruamel import yaml

from comm.tool import Tools
import itertools as it
_tool = Tools()
_yaml = _tool.get_yaml()
start = time.time()
# PROJECT = 'nac'
# BET_CODE = '16_11_10'
# print('BET_CODE',BET_CODE)
# BET_DETAIL = _yaml['detail'].get(PROJECT + '_' + BET_CODE)
# print('BET_DETAIL', BET_DETAIL)


# desired_caps = {
#   'platformName':'Android哈哈哈',#移动设备系统IOS或Android
#   'platformVersion':'7.1.2',#Android手机系统版本号
#   'deviceName':'852',#手机唯一设备号
#   'app':'C:\\Users\\wangli\\Desktop\\kbgz-v5.9.0-debug.apk',#APP文件路径
#   'appPackage':'com',#APP包名
#   'appActivity':'cui.setup.SplashActivity',#设置启动的Activity
#     'noReset':'True',#每次运行不重新安装APP
#   'unicodeKeyboard':'True', #是否使用unicode键盘输入，在输入中文字符和unicode字符时设置为true
#   'resetKeyboard':'True',#隐藏键盘
#     'autoGrantPermissions':'True',
#     'autoAcceptAlerts':["python","c++","java"],
#     'chromeOptions': {'androidProcess': 'com.tencent.mm:tools'}
#   }
numss = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cs = []
# for i in set(it.permutations(numss, 10)):
#     # print('i',i)
#     if i[0]==1:
#         cs.append(i)
# # print('cs',cs)
# desired_caps = {
#   'platformName':str(cs),#移动设备系统IOS或Android
#   }
# with open("test.yaml","w",encoding="utf-8") as f:
#     yaml.dump(desired_caps,f,Dumper=yaml.RoundTripDumper)

with open('test.yaml', 'r', encoding='utf-8') as f:
  print(yaml.load(f.read(),Loader=yaml.Loader))
print(time.time() - start)