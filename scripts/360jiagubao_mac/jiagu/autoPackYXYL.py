#!/usr/bin/env python
# coding= utf-8

import os
import subprocess
def autoPack(versionName):


    tool_jiagu ='java -jar /Users/rts/.jenkins/scripts/360jiagubao_mac/jiagu/jiagu.jar'
    login =' -login '   # 登录
    importsign =' -importsign '  # 上传签名
    jiagu =' -jiagu '   # 加固
    autosign=' -autosign'  # 重签名

    userName='18333646084'
    pwd =' fan1993'
    key_name = '/Users/rts/.jenkins/scripts/android.keystore'
    key_pwd = ' yanxiusrt1qaz@wsx'
    alise = ' zuoyebaoandroid.keystore'
    alise_pwd = ' yanxiusrt1qaz@wsx'
#    apk_name_real = '/Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk/rxt_'+versionName+'-shoujizhushou360.apk'

#    apk_path=' /Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk'

    apk_name_real = '/Users/rts/.jenkins/workspace/Rxt_Android_release/phone/app/build/outputs/apk/sanrenxing_xuesheng_'+versionName+'-shoujizhushou360.apk'

    apk_path=' /Users/rts/.jenkins/workspace/Rxt_Android_release/phone/app/build/outputs/apk'
    print apk_path
    #命令行实现360加固
    cmd_login =tool_jiagu+ login+ userName + pwd
    cmd_importsign =tool_jiagu+ importsign + key_name+ key_pwd + alise+ key_pwd
    cmd_jiagu =tool_jiagu +jiagu +apk_name_real+ apk_path+autosign

    os.system(cmd_login)
    os.system(cmd_importsign)
    os.system(cmd_jiagu)

def getVersionFromGradle(gradle_path):
    print 'find version from build gradle file:',gradle_path
    with open(gradle_path,'r') as f:
        for line in f.readlines():
            if line.find('versionName')>=0:
                versionName = line.strip(' \n').split(' ')[0]
                if versionName != 'versionName':
                    continue
                versionName = line.strip(' \n').split(' ')[1].strip('"')
    return versionName


if __name__ == '__main__':  #定义主函数
#   apk_name = '/Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk/rxt_shoujizhushou360.apk'
    gradle_path = os.getenv("WORKSPACE") + '/phone/app/build.gradle'
    versionName =getVersionFromGradle(gradle_path)
    apk_name = '/Users/rts/.jenkins/workspace/Rxt_Android_release/phone/app/build/outputs/apk/sanrenxing_xuesheng_'+versionName+'-shoujizhushou360.apk'
    print apk_name
    if os.path.exists(apk_name):
        autoPack(versionName)
        os.remove(apk_name)
        print("remove success")
    else:
        print("find no apk")

