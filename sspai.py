import requests
import time
import json
import os

base_url = 'https://sspai.com/api/v1/articles?offset={offset}&limit=10&type=recommend_to_home&sort=recommend_to_home_at&include_total=false'


def get_html(url):
    headers = {
        'Content-Type': 'application/json; charset=utf-8',
        'User-Agent': 'Paw/3.1.5 (Macintosh; OS X/10.12.6) GCDHTTPRequest',
    }
    req = requests.get(url, headers=headers)
    return req.text


def parse_list():
    pass


def parse_article_json(json_data):
    """
    解析JSON数据，提取需要的字段
    """
    result = json.loads(json_data)
    for i in result.get('list'):
        article_info = {
            'article_url': 'https://sspai.com/post/{id}'.format(id=i.get('id')),
            'article_title': i.get('title'),
        }
        print(article_info)
        with open('sspai_info.md', mode='a', encoding='utf-8') as fw:
            fw.write('* [ ] [{Title}]({Link})：{Tags}'.format(Title=article_info.get('article_title'), Link=article_info.get('article_url'), Tags='None') + os.linesep)


def get_time(timestamp):
    # 功能：将Unix时间戳转换成时间

    # 转换成localtime
    time_local = time.localtime(timestamp)
    # 转换成新的时间格式(2016-05-05 20:28:54)
    return time.strftime("%Y-%m-%d %H:%M:%S", time_local)


def main():
    for i in range(100):
        url = base_url.format(offset=i*10)
        json_data = get_html(url)
        print(json_data)
        parse_article_json(json_data)


if __name__ == '__main__':
    main()
