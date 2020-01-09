import shutil
import os


mergeTask = '''
    
    task removeOldMergeEc(type: Delete) {
    delete "$buildDir/mergedcoverage.ec"
    }
    
    task mergeReport(type:JacocoMerge,dependsOn:removeOldMergeEc){
    group = "Reporting"
    description = "merge jacoco report."
    destinationFile= file("$buildDir/outputs/code-coverage/connected/flavors/coverage.ec")
  
    FileTree tree = fileTree("/Users/admin/ec") {
    include '**/*.ec'
    }
    executionData = tree
    }
    '''

def updateManifiestFile(manifest):
    matchText = "</application>"

    str = '''
    <receiver android:name="com.yanxiu.yxtrain_android.test.CodeCoverageReceiver">
    <intent-filter>
        <action android:name="android.intent.action.CodeCoverageReceiver" />
        <category android:name="android.intent.category.DEFAULT"></category>
    </intent-filter>
   </receiver>
    '''

    replaceText = str + matchText
    # print chanelContent
    modifyFile(manifest, matchText, replaceText)

def copyBroadcastFile(targetSource):
    try:
    
        os.mkdir(targetSource)
    except:
        pass
    src = os.getenv("JENKINS_HOME")+"/scripts/CodeCoverageReceiver.java"
    shutil.copy(src,targetSource)



def modifyFile(filename, matchText, replaceText):
    print "start to modify file:" + filename
    with open(filename, 'r') as file:
        content = file.readlines()
        i = 0
        for line in content:

            if line.strip().startswith(matchText):
                text = line.replace(matchText, replaceText)
                content[i] = text
                break
            i = i + 1
        # print content

        with open(filename, "w+") as file:
            file.writelines(content)
        print "end to modify file:" + filename

#only for test code coverage usage, remove contraintlayout line since with this line, cannot launch app for testing
def updategrale(filename):
    print "start to modify file:" + filename
    with open(filename, 'r') as file:
        content = file.readlines()
        i = 0
        for line in content:

            if line.strip().find('com.android.support.constraint:constraint-layout')>=0:

                content[i] = ''
                break
            i = i + 1
        # print content

        with open(filename, "w+") as file:
            file.writelines(content)
            file.writelines(mergeTask)
        print "end to modify file:" + filename


if __name__ == '__main__':
    fileofManifest = os.getenv("WORKSPACE")+"/app/src/main/AndroidManifest.xml"
    targetSource = os.getenv("WORKSPACE")+"/app/src/main/java/com/yanxiu/yxtrain_android/test"
    updateManifiestFile(fileofManifest)
    copyBroadcastFile(targetSource)
    fileOfBuildGradle = os.getenv("WORKSPACE") + "/app/build.gradle"
    updategrale(fileOfBuildGradle)
