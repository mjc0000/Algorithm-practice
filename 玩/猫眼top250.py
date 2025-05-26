import requests
from bs4 import BeautifulSoup
import time
import random
import json
import urllib.robotparser  # 引入 robotparser 模块

# 定义 user-agent
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"  # Chrome User-Agent
BASE_URL = 'http://maoyan.com'
ROBOTS_URL = BASE_URL + '/robots.txt'

def get_one_page(url):
    """获取网页内容"""
    rp = urllib.robotparser.RobotFileParser()  # 每次都创建一个新的 RobotFileParser 对象
    rp.set_url(ROBOTS_URL)

    try:
        rp.read()  # 读取 robots.txt 文件
    except Exception as e:
        print(f"读取 robots.txt 失败: {e}")
        return None

    if not rp.can_fetch(USER_AGENT, url):  # 检查是否允许爬取
        print(f"禁止爬取: {url}")
        return None

    try:
        headers = {
            'User-Agent': USER_AGENT,
            'Referer': BASE_URL  # 添加 Referer 头部
        }
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 检查是否成功
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return None


def write_to_file(item):
    """将数据写入JSON文件"""
    with open('maoyan_top100.json', 'a', encoding='utf-8') as f:
        f.write(json.dumps(item, ensure_ascii=False) + '\n')  # 写入JSON，确保中文不乱码


def parse_one_page_bs(html):
    """使用BeautifulSoup解析页面"""
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('dd')  # 找到所有 <dd> 标签

    for item in items:
        try:
            # 使用正确的CSS选择器来查找元素
            index = item.find('i', class_='board-index').get_text() if item.find('i', class_='board-index') else 'N/A'
            image = item.find('img', class_='board-img')['data-src'] if item.find('img', class_='board-img') else 'N/A'
            title = item.find('a', attrs={'data-act': 'boarditem-click'}).get_text(strip=True) if item.find('a', attrs={'data-act': 'boarditem-click'}) else 'N/A'  # strip=True去掉空白字符
            actor = item.find('p', class_='star').get_text(strip=True)[3:].strip() if item.find('p', class_='star') else 'N/A'
            time_ = item.find('p', class_='releasetime').get_text(strip=True)[5:].strip() if item.find('p', class_='releasetime') else 'N/A'
            integer = item.find('i', class_='integer').get_text() if item.find('i', class_='integer') else '0'
            fraction = item.find('i', class_='fraction').get_text() if item.find('i', class_='fraction') else '0'
            score = integer + fraction

            yield {
                'index': index,
                'image': image,
                'title': title,
                'actor': actor,
                'time': time_,
                'score': score
            }
        except Exception as e:
            print(f"解析错误: {e}")
            continue  # 继续处理下一个item，避免程序中断


def main(offset):
    """主函数"""
    url = 'http://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    if html:  # 检查是否成功获取了网页内容
        for item in parse_one_page_bs(html):
            print(item)
            write_to_file(item)
    # 动态延迟
    time.sleep(random.uniform(3, 5)) # 延迟3-5秒


if __name__ == '__main__':
    for i in range(10):
        main(offset=i * 10)