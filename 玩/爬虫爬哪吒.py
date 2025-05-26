import requests
from bs4 import BeautifulSoup
import time
import random
import csv

# 目标网站（猫眼电影，你可以根据需要更换）
BASE_URL = "https://maoyan.com/films/1209027"  # 哪吒之魔童降世的电影ID
COMMENT_URL = "https://maoyan.com/review/v2/comments.json?movieId=1209027&offset={}&startTime={}"

# 设置请求头，模拟浏览器访问
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Referer': BASE_URL
}

# 设置时间戳
START_TIME = int(time.time() * 1000)  # 当前时间戳

# 定义存储评论的列表
comments = []

def get_comments(offset):
    """
    获取指定offset的评论数据
    """
    url = COMMENT_URL.format(offset, START_TIME)
    try:
        response = requests.get(url, headers=HEADERS)
        response.raise_for_status()  # 检查HTTP请求是否成功
        data = response.json()

        if data and data['data'] and data['data']['comments']:
            for comment_data in data['data']['comments']:
                comment = {
                    'user_name': comment_data.get('nickName', '匿名用户'),
                    'comment_text': comment_data.get('content', ''),
                    'score': comment_data.get('score', 0),  # 添加评分信息
                    'comment_time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(comment_data.get('startTime')/1000)) # 添加评论时间信息
                }
                comments.append(comment)
            return True # 返回True表示还有数据
        else:
            return False # 返回False表示没有数据了

    except requests.exceptions.RequestException as e:
        print(f"请求错误: {e}")
        return False # 返回False，防止程序中断
    except Exception as e:
        print(f"解析错误: {e}")
        return False # 返回False，防止程序中断


def save_comments_to_csv(filename, comments):
    """
    将评论保存到CSV文件中
    """
    fieldnames = ['user_name', 'comment_text', 'score', 'comment_time'] # 添加评分和评论时间
    with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(comments)
    print(f"评论已保存到 {filename}")


def main(num_pages=10):  # 可以设置爬取的页数，默认为10页
    """
    主函数，控制爬取流程
    """
    offset = 0
    page = 1
    has_more_data = True
    while has_more_data and page <= num_pages:
        print(f"正在爬取第 {page} 页评论...")
        has_more_data = get_comments(offset)
        if has_more_data:
            offset += 15 # 猫眼电影每页15条评论
            page += 1
            time.sleep(random.uniform(1, 3))  # 暂停1-3秒，防止被反爬
        else:
            print("没有更多评论了")
            break


if __name__ == "__main__":
    main(num_pages=50)  # 爬取50页评论，可以根据需要修改
    save_comments_to_csv("nezha_comments.csv", comments) # 将结果保存到csv文件中
    print("爬取完成！")