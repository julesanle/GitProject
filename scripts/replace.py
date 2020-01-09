#! /usr/bin/env
# 脚本用env启动的原因，是因为脚本解释器在linux中可能被安装于不同的目录，env可以在系统的PATH目录中查找。同时，env还规定一些系统环境变量。
#coding=utf-8

#说明: 现在测试良师通的安卓和iOS没有问题,需要确定所要替换的文件路径和文件名  另外,易学易练的路径没有写,用的话,需要写上~~~~


import sys, shutil, os, string

#Jenkins config file
jenkins_path = '/Users/rts/.jenkins/jenkins_config'
workspace = os.getenv("WORKSPACE")

#sxy new config file
app_path_sxy =os.path.join(workspace,"app/src/main/assets")
app_path_ios_sxy =os.path.join(workspace,"ShangXueYuan/ShangXueYuan")

#配置文件名称

#sxy
#app -config
app_ios_sxy ='env_config.json'
app_android_sxy ='env_config.json'
#jenkins-config
ios_test_sxy = 'config_test.json'
ios_release_sxy ='config_rel.json'
ios_dev_sxy ='config_dev.json'
android_test_sxy ='config_test.json'
android_release_sxy = 'config_rel.json'
android_dev_sxy ='config_dev.json'


def copy_file(app_ios_config,ios_release_file,app_file_path):
    # 直接判断文件 / 文件夹是否存在  env_config.json
    if not os.path.exists(app_ios_config):
        # config_test.json    ShangXueYuan/ShangXueYuan
        shutil.copy(ios_release_file,app_file_path)
    else:
        # config_test.json    env_config.json
        shutil.copy(ios_release_file,app_ios_config)


def choose_config(app,system,package):
    jenkins_file_path = jenkins_path+'/'+app+'/'+system

    if app =='sxy':
        if system == 'ios' and package == 'test':
            ios_test_file = jenkins_file_path+'/'+ios_test_sxy
            app_ios_config = app_path_ios_sxy+'/'+app_ios_sxy
            copy_file(app_ios_config, ios_test_file, app_path_ios_sxy)
            #shutil.copy(ios_test_file,app_ios_config) #新文件，旧文件
        elif system == 'ios' and package == 'release':
            ios_release_file = jenkins_file_path+'/'+ios_release_sxy
            app_ios_config = app_path_ios_sxy+'/'+app_ios_sxy
            copy_file(app_ios_config, ios_release_file, app_path_ios_sxy)
            #shutil.copy(ios_release_file,app_ios_config)
        elif system == 'ios' and package == 'dev':
            ios_dev_file = jenkins_file_path+'/'+ios_dev_sxy
            app_ios_config = app_path_ios_sxy+'/'+app_ios_sxy
            copy_file(app_ios_config, ios_dev_file, app_path_ios_sxy)
        elif system == 'android'and package == 'test':
            android_test_file = jenkins_file_path+'/'+android_test_sxy
            app_android_config = app_path_sxy+'/'+app_android_sxy
            copy_file(app_android_config, android_test_file, app_path_sxy)
            #shutil.copy(android_test_file,app_android_config)
        elif system == 'android' and package == 'release':
            android_release_file = jenkins_file_path+'/'+android_release_sxy
            app_android_config = app_path_sxy+'/'+app_android_sxy
            copy_file(app_android_config, android_release_file, app_path_sxy)
            #shutil.copy(android_release_file,app_android_config)
        elif system == 'android' and package == 'dev':
            android_dev_file = jenkins_file_path+'/'+android_dev_sxy
            app_android_config = app_path_sxy+'/'+app_android_sxy
            copy_file(app_android_config, android_dev_file, app_path_sxy)






if __name__ == '__main__':  #定义主函数
    # sys.argv是用来获取命令行参数的,sys.argv[0]表示代码本身文件路径
    args = sys.argv
    #get app system package &&translate to lower
    app = args[1].lower()
    system = args[2].lower()
    package = args[3].lower()
    print(system,package)
    choose_config(app,system,package)
