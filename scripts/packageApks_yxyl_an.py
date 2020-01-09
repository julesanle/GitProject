import os
import shutil
import zipfile


if __name__ == '__main__':
    outputDir = os.getenv("WORKSPACE")+"/phone/app/build/outputs/apk/"
    #outputDir = r"C:\Users\Administrator\.jenkins\jobs\BuildMultiChanelApk\workspace\app\build\outputs\apk"
    os.chdir(outputDir)
    if(os.path.exists("app")):
        shutil.rmtree("app")
    os.mkdir("app")
    files = os.listdir(outputDir)
    for file in files:
        name = os.path.basename(file)
        
        if (name.startswith("sanrenxing_xuesheng")):
          
            shutil.copy(file,outputDir+"/app")
    z = zipfile.ZipFile('packages.zip', 'w', zipfile.ZIP_DEFLATED)
    
    for dirpath, dirnames, filenames in os.walk(outputDir+"/app"):
        print dirpath
        for filename in filenames:
            print filename
            z.write(filename)
    z.close()
    
