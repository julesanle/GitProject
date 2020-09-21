#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser


class ConfigParser():
    conf = configparser.ConfigParser()  # 创建对象

    def get_config(self, config_path, sector, item):
        try:
            self.conf.read(config_path)  # 读取配置文件，直接读取ini文件内容encoding='UTF-8' E:\default.ini
            return self.conf.get(sector, item)
        except configparser.NoOptionError as exp:
            return -1

    def write_config(self, config_path, sector, item, con):
        try:
            self.conf.read(config_path)
            self.conf.set(sector, item.strip(), con.strip())
            self.conf.write(open(config_path, "w+"))
        except configparser.NoOptionError as exp:
            return -1

if __name__ == '__main__':
    con = ConfigParser()
    url='https://www-dev.3ren.cn/um/schoolCenter/activity/4689252406238896128/detail.do'
    # res = con.get_config('E:\\default.ini', '研修中心', 'act_name')
    res = con.write_config('E:\\default.ini', '研修中心', 'url',url)
    print(res)
