# encoding:utf-8
import requests
import os
import time
import sys
import importlib
importlib.reload(sys)
# reload(sys)
sys.setdefaultencoding('utf-8')

USER_KEY = "4ab4f755fe23f9f0415e7ef89c279c84"
API_KEY = "c0db5f948b82e1d8d7da34f5ff6017e8"
PGYER_UPLOAD_URL = "https://www.pgyer.com/apiv2/app/upload"


def getQRCode(path, url):
    result = requests.request('get', url)  # 获取网页
    if result.status_code == 200:
        with open(path, 'wb') as f:  # 打开写入到path路径里-二进制文件，返回的句柄名为f
            f.write(result.content)  # 往f里写入r对象的二进制文件
        f.close()
    else:
        print
        "error: ", result


def uploadToPgyer(AppPath, QRCodePath, updateDescription):
    print
    "Begin to upload apk to Pgyer: %s" % AppPath
    headers = {'enctype': 'multipart/form-data'}
    postDate = {
        'uKey': USER_KEY,
        '_api_key': API_KEY,
        'buildInstallType': '1',  # (选填)应用安装方式，值为(1,2,3，4)。1：公开，2：密码安装，3：邀请安装，4：回答问题安装。默认为1公开
        'updateDescription': updateDescription,  # (选填) 版本更新描述，请传空字符串，或不传。
    }
    try_times = 0
    while try_times < 3:
        try:
            print
            "uploading ..."
            appfile = {'file': open(AppPath, 'rb')}
            print
            postDate
            r = requests.post(PGYER_UPLOAD_URL,
                              headers=headers,
                              files=appfile,
                              data=postDate
                              )
            break
        except requests.exceptions.ConnectionError:
            print
            "requests.exceptions.ConnectionError occured!"
            time.sleep(5)
            print
            "try again ..."
            try_times += 1
        except Exception as e:
            print
            "Exception occured: %s" % str(e)
            time.sleep(5)
            print
            "try again ..."
            try_times += 1

    if r.status_code == requests.codes.ok:
        result = r.json()
        print
        "result is", result
        resultCode = result['code']
        if resultCode == 0:
            print
            "Upload Success"
            QRCodeUrl = result['data']['buildQRCodeURL']
    else:
        print
        'HTTPError, response: %s' % r.content
    return QRCodeUrl


if __name__ == '__main__':
    # buildId = os.getenv("BUILD_ID")
    workspace = "/Users/rts/.jenkins/workspace/"
    if sys.argv[1] == "Student":
        appname = os.path.join(workspace, "Rxt_IOS/YanXiuStudentApp/build/app.ipa")
        # 二维码
        QRCodePath = os.path.join(workspace, "Rxt_IOS/YanXiuStudentApp/build/QRCode.jpg")
    elif sys.argv[1] == "Teacher":
        appname = os.path.join(workspace, "ShangXueYuan_IOS/ShangXueYuan/build/sxy.ipa")
        QRCodePath = os.path.join(workspace, "ShangXueYuan_IOS/ShangXueYuan/build/QRCode.jpg")
        # 上传应用
    QRCodeUrl = uploadToPgyer(appname, QRCodePath, sys.argv[1])
    print
    "QRCodeUrl is :", QRCodeUrl
    # 获取二维码
    getQRCode(QRCodePath, QRCodeUrl)