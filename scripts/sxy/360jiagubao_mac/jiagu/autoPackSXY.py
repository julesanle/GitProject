#!/usr/bin/env python
# coding= utf-8
import shutil
import os
import subprocess
def autoPack(versionName):


    tool_jiagu ='java -jar /Users/rts/.jenkins/scripts/sxy/360jiagubao_mac/jiagu/jiagu.jar'
    login =' -login '   # 登录
    importsign =' -importsign '  # 上传签名
    jiagu =' -jiagu '   # 加固
    autosign=' -autosign'  # 重签名

    userName='18333646084'
    pwd =' fan1993'
    key_name = '/Users/rts/.jenkins/scripts/sxy/shangxueyuan.jks'
    key_pwd = ' yanxiusrt1qaz@wsx'
    alise = ' shangxueyuanandroid.keystore'
    alise_pwd = ' yanxiusrt1qaz@wsx'
#    apk_name_real = '/Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk/rxt_'+versionName+'-shoujizhushou360.apk'

#    apk_path=' /Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk'

    apk_name_real = ' /Users/rts/.jenkins/workspace/ShangXueYuan_Android_Release/app/build/outputs/apk/shoujizhushou360/release/sxy_'+versionName+'-shoujizhushou360.apk'

    apk_path=' /Users/rts/.jenkins/workspace/ShangXueYuan_Android_Release/app/build/outputs/apk'
    

    #命令行实现360加固
    cmd_login =tool_jiagu+ login+ userName + pwd
    cmd_importsign =tool_jiagu+ importsign + key_name+ key_pwd + alise+ key_pwd
    cmd_jiagu =tool_jiagu +jiagu +apk_name_real+ apk_path+autosign
    print cmd_login
    print cmd_importsign
    print cmd_jiagu

    os.system(cmd_login)
    os.system(cmd_importsign)
    os.system(cmd_jiagu)


#移动生产的包到apk路径下
def moveapk(apkName,versionName):
    apk_initialPath="/Users/rts/.jenkins/workspace/ShangXueYuan_Android_release/app/build/outputs/apk/"
    shutil.move(apk_initialPath+apkName+"/release/"+"sxy_"+versionName+"-"+apkName+".apk",apk_initialPath+"/")#移动文件

def getVersionFromGradle(gradle_path):
    print 'find version from build gradle file:',gradle_path
    versionName=[]
    with open(gradle_path,'r') as f:
        for line in f.readlines():
            if line.find('versionName')>=0:
                versionName.append(line.strip(' \n').split(' ')[1])
                    #if versionName != 'versionName':
                    #continue
                versionName.append(line.strip(' \n').split(' ')[1].strip('"'))
    return versionName[0]


if __name__ == '__main__':  #定义主函数
#   apk_name = '/Users/admin/.jenkins/workspace/Rxt_Android_release/phone/MainApp/build/outputs/apk/rxt_shoujizhushou360.apk'

    gradle_path = os.getenv("WORKSPACE") + '/app/build.gradle'
    #gradle_path = '/Users/rts/.jenkins/workspace/ShangXueYuan_Android_Release/app/build.gradle'

    versionName =getVersionFromGradle(gradle_path)
    versionName=versionName.replace('"','')
    versionName=versionName.strip('\r')
    print "versionName is:"+versionName
    moveapk("baidushoujizhushou",versionName)
    moveapk("huaweihuizhi",versionName)
    moveapk("lenovomm",versionName)
    moveapk("oppo",versionName)
    moveapk("others",versionName)
    moveapk("txyingyongbao",versionName)
    moveapk("vivo",versionName)
    moveapk("wandoujia",versionName)
    moveapk("xiaomi",versionName)
    
    apk_name = '/Users/rts/.jenkins/workspace/ShangXueYuan_Android_release/app/build/outputs/apk/shoujizhushou360/release/sxy_'+versionName+'-shoujizhushou360.apk'
    #print apk_name
    if os.path.exists(apk_name):
        autoPack(versionName)
        #os.remove(apk_name)
        #print("remove success")
    else:
        print("find no apk")

