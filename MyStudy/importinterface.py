from pyquery import PyQuery as pq

swagger_url='http://10.7.95.221:20040/swagger-ui.html'

def get_interface_list():
    doc = pq(swagger_url,parser="html")
   # print(doc)
    print(doc('div').find('div'))
    center_list = doc('option')
    for data in center_list:
        print(pq(data).html())
    for i in center_list:
        print(i+'=====')
    # doc111=pq('https://www-dev.3ren.cn/')
    # print(doc111('.username').text())
    print(center_list)


    #将列表写入文件
    # with open('center_list.txt', 'w+', encoding='utf-8') as f:
    #     f.write(center_list)
    return center_list
def importlist():
    return 0

if __name__ == '__main__':
    # 获取swagger中的center列表
    get_interface_list()

    # 从list中选择center进行导入
    importlist()
    # 导入完将接口的url中 域名改下