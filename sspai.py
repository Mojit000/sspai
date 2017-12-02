import time
import json
import os
import requests

base_url = 'https://sspai.com/api/v1/articles?offset={offset}&limit=10&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'

false_url = 'https://sspai.com/api/v1/articles?offset=9980&limit=10&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'


def get_html(url):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Paw/3.1.5 (Macintosh; OS X/10.12.6) GCDHTTPRequest',
    }
    req = requests.get(url, headers=headers)
    return req.text


def parse_article_json(json_data):
    """
    获取单页面文章列表数据：链接 标题
    解析JSON数据，提取需要的字段：链接 标题 
    """
    result = json.loads(json_data)
    for i in result.get('list'):
        article_info = {
            'article_url': 'https://sspai.com/post/{id}'.format(id=i.get('id')),
            'article_title': i.get('title'),
        }
        # print(article_info)
        with open('sspai_info.md', mode='a', encoding='utf-8') as fw:
            fw.write('* [ ] [{Title}]({Link})：{Tags}'.format(Title=article_info.get(
                'article_title'), Link=article_info.get('article_url'), Tags='None') + os.linesep)


def initSQL():
    """
    初始化数据库
    """
    pass


def saveData(db):
    """
    保存数据到数据库
    """
    pass


def isDataExist(data, db):
    """
    判断数据库中是否已经存在data数据
    """
    pass


def deleteData(data, db):
    """
    删除数据库中的data数据
    """
    pass


def generateMarkdown():
    """
    生成Markdown文档
    """
    pass


def get_time(timestamp):
    """
    功能：将Unix时间戳转换成时间
    """
    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)


def main():
    page_num = 0
    while True:
        # 循环遍历获取每一页文章列表信息
        url = base_url.format(offset=page_num * 10)
        json_data = get_html(url)
        if len(json_data) <= 11:
            print('错误页面：', page_num)
            break
        print('爬取第{}页'.format(page_num + 1))
        parse_article_json(json_data)
        page_num = page_num + 1


def test():
    json_data = get_html(false_url)
    print(len(json_data))


if __name__ == '__main__':
    main()
    # test()
