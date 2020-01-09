import os

if __name__ == '__main__':
    workspace = os.getenv("WORKSPACE")
   # workspace = "/Users/admin/.jenkins/workspace/YanxiuUITraverseAndroid"
    candidateDir = ""
    for item in os.listdir(workspace):
        if item.startswith("android_"):
            candidateDir = item

    diff_cmd = "java -jar " + workspace + "/appcrawler-1.7.1.jar --diff --master /Users/admin/android_expected --candidate "+candidateDir +" --report diff/"
    print diff_cmd
    print os.popen(diff_cmd).read()