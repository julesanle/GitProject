#!/usr/bin/python
# -*- coding: UTF-8 -*-
import configparser


class ConfigParser():

    def get_config(self,config_path,sector,item):
        try:

            cf = configparser.ConfigParser()  # 创建对象
            cf.read(config_path)  # 读取配置文件，直接读取ini文件内容encoding='UTF-8' E:\default.ini
        except KeyError as exp:
             print(exp)
        finally:
            return cf.get(sector,item)


if __name__ == '__main__':
    con = ConfigParser()
    res = con.get_config('E:\\default.ini','LoginElement','local_driver')
    print(res)
