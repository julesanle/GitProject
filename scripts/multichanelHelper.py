# -*- coding: utf8-*-
import os
import shutil
import re
import datetime

apktoolPath = os.getenv("JENKINS_HOME")+"/scripts/apktool.jar"
apkDir = os.getenv("WORKSPACE")+"/app/build/outputs/apk/"

def decodeApk():
    print "start decode apk"
    othersChanelApkPath = 'yx_train_vothers.apk'
    cmd = "java -jar " + apktoolPath + " d -f " + othersChanelApkPath + " -o build"
    print os.popen(cmd).read()

def updateManifest(chanel_value):
    manifest = "build/AndroidManifest.xml"
    pattern = r'(<meta-data\s+android:name="UMENG_CHANNEL"\s+android:value=")(\S+)("/>)'
    replacement = r"\g<1>{channel}\g<3>".format(channel=chanel_value)
    text = open(manifest,'r').read()
    content = re.sub(pattern, replacement, text)
    with open(manifest,"w+") as file:
        file.writelines(content)


def repackApk(chanel_value):
    print 'start repack apk'
    cmd = 'java -jar '+apktoolPath+' b build -o yx_train_v{chanel}.apk'.format(chanel=chanel_value)
    print os.popen(cmd).read()

def resignApk(chanel_value):
    print 'start resign apk'
    cmd  = 'jarsigner -sigalg SHA1withRSA -digestalg SHA1 -keystore yanxiuandroid.keystore -storepass yanxiusrt1qaz@wsx -signedjar yx_train_v{chanel}.apk yx_train_v{chanel}.apk android.keystore'.format(chanel=chanel_value)
    print os.popen(cmd).read()

def copyKeyFile():
    jenkinsHome = os.getenv("JENKINS_HOME")
    workspace = os.getenv("WORKSPACE")
    filename =  os.path.join(jenkinsHome,"scripts/yanxiuandroid.keystore")
    print "start to copy keystore file"
    cmd_copy = "cp "+ filename +" "+ apkDir
    print cmd_copy
    print os.popen(cmd_copy).read()




if __name__ == "__main__":
    
    startTime = datetime.datetime.now()
    os.chdir(apkDir)
    copyKeyFile()
    if os.path.exists("build"):
        shutil.rmtree("build")
    decodeApk()


    chanels = ["baidushoujizhushou","huaweihuizhi","jifengshichang","lenovomm","oppo","sanxing","shoujizhushou360","txyingyongbao","vivo","wandoujia","xiaomi","yanxiu_com","yingyonghui"]
    for chanel in chanels:
        print chanel
        updateManifest(chanel)
        repackApk(chanel)
        resignApk(chanel)
    if os.path.exists("build"):
        shutil.rmtree("build")
    endTime = datetime.datetime.now()
    print "total run:%s s" % (endTime - startTime).seconds
