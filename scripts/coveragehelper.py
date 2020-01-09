from __future__ import division
import shutil
import os,sys
from xml.dom.minidom import parse
import xml.dom.minidom


JENKINS_HOME = os.getenv("JENKINS_HOME")
WORKSPACE = os.getenv("WORKSPACE")
ignoreFilePath = '/Users/admin/ec/ignorefile.txt'

diffFile_path = []

def copy_ecfile():
    ecfile_path = "/sdcard/coverage"
    dest_path = "/Users/admin/ec"

    copy_cmd = "adb pull "+ecfile_path+" "+dest_path
    print os.popen(copy_cmd).read()

def sendBroadcast():
    broadcast_cmd = "adb shell am broadcast -a android.intent.action.CodeCoverageReceiver"
    print os.popen(broadcast_cmd).read()

def connect_via_wifi():
    print os.popen("adb connect 192.168.7.65").read()

def make_coverage_dir():
    jenkins_home = os.getenv("JENKINS_HOME")
    build_path = jenkins_home + "/workspace/BuildLSTForCodeCoverage"
    os.chdir(build_path)
    coverage_dir =build_path+ "/app/build/outputs/code-coverage/connected/flavors/"
    if not os.path.exists(coverage_dir):
        os.makedirs(coverage_dir)

def mergeJacoco():
    print os.popen("gradle mergeReport").read()

def generateReport():
    print os.popen("gradle -Dfile.encoding=UTF-8 jacocoTestReport").read()



def getFileListHasDiff(old_commitid,new_commitid):
    print "start get diff file list"
    cmd = "git diff "+ old_commitid +" " + new_commitid +" --stat "
    print "cmd for git diff is:",cmd
    cmd_result = os.popen(cmd).read()
    print cmd_result,type(cmd_result)
    path_filename = {}
    for line in cmd_result.splitlines():
        pos = line.find(".java")
        if pos>0:
            #print line[:pos+5]
            temp = line[:pos+5]
            p = temp.rfind("/")
                
            filename = line[p+1:pos+5]
            filepath = line[line.find("/"):pos+5]
            #print filename
            print filepath
            path_filename[filepath] = filename
                
    return path_filename
#findFile(fileList)


def getDiffFileList(old_commitid,new_commitid):
    print "start get diff file list"
    filename = "diff.txt"
    cmd = "git diff "+ old_commitid +" " + new_commitid +" --stat "+">"+filename
    print "cmd for git diff is:",cmd
    print os.popen(cmd).read()
    fileList = []
    with open(filename) as f:
        for line in f:
            print 'diff.txt line, ',line
            pos = line.find(".java")
            if pos>0:
                print line[:pos+5]
                temp = line[:pos+5]
                p = temp.rfind("/")
                java_file = line[p+1:pos+5]
                print java_file
                fileList.append(java_file.replace("java","java.html"))
                diffFile_path.append(line[line.find("/"):pos+5])
                return fileList
                       
def findFile(fileList):
    search_path = os.getenv("WORKSPACE")+"/app/build/reports/jacoco/jacocoTestReport/html"
    print "search_path:",search_path
    print "search_file:",fileList
    #htmlList = [f.replace("java.html","html") for f in fileList]
    htmlList = [f.replace("java","html") for f in fileList]
    fileList = [f.replace("java","java.html") for f in fileList]
    print "htmlList",htmlList
    mark_dir = False
    filelink_map = {}
    temp = [p[:p.rfind('/')].lstrip('/').replace('/','.') for p in diffFile_path]
    #print '@@@@@@@@@@',temp
    for path in os.listdir(search_path):
        #print "path:",path
        abs_path = os.path.join(search_path,path)
        if os.path.isdir(abs_path):
            for file in os.listdir(abs_path):
                #print "file:",file
                '''
                if file in fileList or file in htmlList:
                    print "found "+file+" in:",abs_path,path
                    mark_dir = True
                elif file=="index.html":
                    continue
                else:
                    os.remove(os.path.join(abs_path,file))
            
            if not mark_dir:
                for file in os.listdir(abs_path):
                    os.remove(os.path.join(abs_path,file))
                os.rmdir(abs_path)
        mark_dir = False
                '''
                
                if file in fileList:
                    found = False
                    for t in temp:
                        pos =path.find(t)
                        if pos>=0 and path[pos:]==t:
                            print 30*'&',path,t
                            found = True
                            break
                    if found:
                        print 30*'*',abs_path,path
                        filelink_map[file]=os.getenv("JOB_URL")+"HTML_Report/"+os.path.join(path,file)
    return filelink_map

def writeToHtml(fileList,summary):
    print 'writeToHtml',fileList
    filelink_map = findFile(fileList)
    html_file = open(os.getenv("WORKSPACE")+"/app/build/reports/jacoco/jacocoTestReport/html/"+"index.html","w")
    html_file.write(summary)
    table_start = "<table border=1>"
    table_title = "<tr><th>git diff list</th></tr>"
    table_end = "</table>"
    
    html_file.write(table_start)
    html_file.write(table_title)
    print 'filelink_map',filelink_map
    with open(ignoreFilePath,'r') as f:
        ignores = [line.strip('\n') for line in f]
        ignores = [f.replace(".java",".java.html") for f in ignores]
        print 'ignores,',ignores
    for file,link in filelink_map.items():
        print link
        if file not in ignores:
            html_file.write("<tr><td><a href={filelink}>{filename}</a></td></tr>".format(filelink=link,filename=file))
    
    html_file.write(table_end)
    html_file.close()

def generateTitle(old_commitid,new_commitid):
    old_cmd = "git log --format=%B -n 1 {commitid}".format(commitid=old_commitid)
    new_cmd = "git log --format=%B -n 1 {commitid}".format(commitid=new_commitid)

    old_message = os.popen(old_cmd).read()
    new_message = os.popen(new_cmd).read()

    return "from:"+old_commitid+":"+old_message+"<br/>"+"to:"+new_commitid+":"+new_message

def writeDiffToHtml(old_commitid,new_commitid,fileList):
    file_path = findFileFromSrc(fileList)
    filelink_map = findFile(fileList)
    print "filelink_map"
    print 30*'-'
    for k,v in filelink_map.items():
        print k,v
    print "file_path:",file_path
    for f in file_path:
        diff_content_cmd  = "git diff "+old_commitid+" "+new_commitid +" "+f
        print "diff_content_cmd:",diff_content_cmd
        diff_content = os.popen(diff_content_cmd).read()
        print "diff_content:",diff_content
        try:
            java_html = filelink_map[f[f.rfind("/")+1:]+".html"]
            java_html_path = os.getenv("WORKSPACE")+"/app/build/reports/jacoco/jacocoTestReport/html/" + java_html[java_html.find("HTML_Report")+12:]
            print "@@@@",java_html_path
            with open(java_html_path,"r") as file:
                content = file.read()
                search_str = '<pre class="source lang-java linenums">'
                content = content.replace(search_str,search_str+diff_content+"</pre>"+search_str)
            with open(java_html_path,"w") as file:
            #diff_content = diff_content.splitlines()
            # file.write("<pre class="source lang-java linenums">")
            # for line in diff_content:
            #   file.write(line+"<br/>")
            #file.write("</pre>")
                file.write(content)
        except:
            pass



def findFileFromSrc(fileList):
    print "will find file from source code,",fileList
    fileList = [f.rstrip(".html") for f in fileList]
    search_path = os.getenv("WORKSPACE")+"/app/src/main/java"
    file_path = []
    for f in fileList:
        print "will find f:",f
        if find_files(search_path,f):
            file_path.append(find_files(search_path,f))
    return file_path


def find_files(path, wanted):
    try:
       
        dir_list = os.listdir(path)
        for filename in dir_list:
            
            new_path = os.path.join(path, filename)
            
            if os.path.isdir(new_path):
                temp = find_files(new_path, wanted)
                if temp:
                    return temp
            
           
            elif os.path.isfile(new_path):
                if wanted.lower() == filename.lower():
                    
                    real_found = False
                    for p in diffFile_path:
                        if p in new_path:
                            real_found = True
                    if real_found:
                        print "found file:",(new_path)
                        return new_path

    except Exception as e:
        print(e)



def getFileListCoveredLessThan(path_filename,percent=100):
    'get file that missed instruction is less than percent'
    results = []
    print 'get file list that missed instruction is less than {percent}'.format(percent=percent)
    #print 'all diff file list is',filelist
    paths = path_filename.keys()
    refine_path = [p[1:p.find(".java")] for p in paths]
    files = path_filename.values()
    report_file = WORKSPACE+"/app/build/reports/jacoco/jacocoTestReport/jacocoTestReport.xml"
    DOMTree = xml.dom.minidom.parse(report_file)
    report = DOMTree.documentElement
    
    packages = report.getElementsByTagName("package")
    for package in packages:
        classes = package.getElementsByTagName("class")
        sources = package.getElementsByTagName("sourcefile")
        has_found = False
        for c in classes:
            classname = c.getAttribute("name")
            for p in refine_path:
                if classname.find(p)>=0 and classname.find("$")<0:
                    has_found = True
                    break
        if has_found:
            for source in sources:
                filename = source.getAttribute("name")
                        
                if filename in files:
                    print filename
                    counters = source.getElementsByTagName("counter")
                    for counter in counters:
                        if counter.getAttribute("type") == "INSTRUCTION":
                            missed = counter.getAttribute("missed")
                            covered = counter.getAttribute("covered")
                            print missed,covered
                           
                            print float(percent)/100
                            if missed!=0 and float(covered)/(float(missed)+float(covered))<float(percent)/100:
                                print 'need keep'
                            else:
                                results.append(filename)




    return results


def saveIgnoreListToFile(filepath,filelist):
    with open(filepath,'r') as f:
        current = [line.strip('\n') for line in f]
        print 'current',current
    with open(filepath,'a') as f:
        sep = os.linesep
        print 'new',filelist
        f.writelines([file+sep for file in filelist if file not in current])


if __name__ == "__main__":
    
    connect_via_wifi()
    sendBroadcast()
    copy_ecfile()
    make_coverage_dir()
    mergeJacoco()
    generateReport()
    
    print len(sys.argv)
    if len(sys.argv)==3:
        old_commitid = sys.argv[1]
        new_commitid = sys.argv[2]
        fileList = getDiffFileList(old_commitid,new_commitid)
        print "diff file path",diffFile_path
        

        path_filename = getFileListHasDiff(old_commitid,new_commitid)
        diffFile_path = path_filename.keys()
        print "file path list",path_filename.keys()
        ignoreFile = getFileListCoveredLessThan(path_filename,percent=100)
        
        saveIgnoreListToFile(ignoreFilePath,ignoreFile)

        summary = generateTitle(old_commitid,new_commitid)
        print '@@@',path_filename.values()
        writeToHtml(path_filename.values(),summary)
        writeDiffToHtml(old_commitid,new_commitid,path_filename.values())




