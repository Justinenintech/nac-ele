import os
import configparser
from os.path import dirname, abspath

from test_junkie.debugger import LogJunkie

LogJunkie.enable_logging(10)


class ConfigOverWrite(configparser.ConfigParser):
    def __init__(self):
        configparser.ConfigParser.__init__(self, defaults=None)

    def optionxform(self, option_str: str) -> str:
        return option_str


# 获取当前根目录路径
path = dirname(dirname(abspath(__file__)))
# 配置文件路径
conf_path = os.path.join(path, 'config.ini')
# 初始化操作配置文件实例
conf = ConfigOverWrite()
conf.read(conf_path, encoding='utf-8-sig')


class Config(object):
    @staticmethod
    def sections() -> list:
        """Return a list of section names, excluding [DEFAULT]"""
        # self._sections will never have [DEFAULT] in it
        return list(conf.sections())

    @staticmethod
    def get(section: str, option: str) -> str:
        """从配置文件中读值"""
        # 读取seciton下key的value
        try:
            config_get = conf.get(section, option)
            return config_get
        except Exception as e:
            LogJunkie.error('在section：%s下读取%s的值-失败，异常信息：%s' % (section, option, e))

    @staticmethod
    def get_int(section: str, key: str) -> str:
        """从配置文件中读值"""
        # 读取seciton下key的value
        try:
            config_get = conf.getint(section, key)
            return config_get
        except Exception as e:
            LogJunkie.error('在section：%s下读取%s的值-失败，异常信息：%s' % (section, key, e))

    @staticmethod
    def get_write(section: str, key=None, value=None):
        """往配置文件写入"""
        # 在section下写入key, value
        if key is not None and value is not None:
            conf.set(section, key, value)
            LogJunkie.info('在section：%s下新增%s=%s' % (section, key, value))
            with open(conf_path, 'w', encoding='utf-8') as f:
                conf.write(f)
        else:
            # 新增section
            conf.add_section(section)
            LogJunkie.info("新增section：%s" % section)
            with open(conf_path, 'w', encoding='utf-8') as f:
                conf.write(f)

    @staticmethod
    def get_delete(section: str, key=None):
        """从配置文件中删除"""
        # 删除section下对应key, value
        if key is not None:
            conf.remove_option(section, key)
            LogJunkie.info('删除section:%s下%s和他的值' % (section, key))
            with open(conf_path, 'w', encoding='utf-8') as f:
                conf.write(f)
        else:
            # 删除section
            conf.remove_section(section)
            LogJunkie.info('删除section:%s' % section)
            with open(conf_path, 'w', encoding='utf-8') as f:
                conf.write(f)

    @staticmethod
    def get_options(section: str) -> list:
        """读取配置文件某section下所有键"""
        try:
            username = conf.options(section)
            return username
        except Exception as e:
            LogJunkie.error('获取title失败 %s' % e)

    def get_content(self, section: str) -> dict:
        result = {}
        for option in self.get_options(section):
            value = self.get(section, option)
            result[option] = int(value) if value.isdigit() else value
        return result
