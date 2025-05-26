import requests
from bs4 import BeautifulSoup
import csv

# 目标网站 URL
TARGET_URL = "http://books.toscrape.com/"

def fetch_data(url):
    """
    从指定的 URL 获取页面内容.

    Args:
        url (str): 要抓取的 URL.

    Returns:
        str: 页面 HTML 内容，如果出现错误则返回 None.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_book_data(html_content):
    """
    从 HTML 内容中提取书籍数据.

    Args:
        html_content (str): HTML 内容.

    Returns:
        list: 包含书籍数据的列表，每个元素都是一个字典.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    book_list = []

    # 查找所有包含书籍信息的 article 元素
    articles = soup.find_all('article', class_='product_pod')

    for article in articles:
        # 提取书籍标题
        title = article.h3.a['title']

        # 提取价格
        price = article.find('p', class_='price_color').text

        # 提取评分（星级）
        star_rating = article.p['class'][1]  # 例如：'Star-Rating'

        # 提取书籍详情页链接
        detail_link = TARGET_URL + article.h3.a['href']

        book_data = {
            'title': title,
            'price': price,
            'star_rating': star_rating,
            'detail_link': detail_link
        }
        book_list.append(book_data)

    return book_list

def save_to_csv(data, filename="books.csv"):
    """
    将数据保存到 CSV 文件.

    Args:
        data (list): 要保存的数据，列表中的每个元素都是一个字典.
        filename (str): CSV 文件的名称.
    """
    if not data:
        print("没有数据可写入 CSV 文件。")
        return

    # 获取所有键作为 CSV 文件的标题行
    fieldnames = data[0].keys()

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

            # 写入标题行
            writer.writeheader()

            # 写入数据行
            writer.writerows(data)

        print(f"数据已成功保存到 {filename}")

    except Exception as e:
        print(f"写入 CSV 文件时发生错误：{e}")

def main():
    """
    主函数，执行爬取、解析和保存操作.
    """
    html_content = fetch_data(TARGET_URL)

    if html_content:
        book_data = parse_book_data(html_content)

        if book_data:
            save_to_csv(book_data)  # 保存到 CSV 文件
            print("抓取到的书籍数据：")
            for book in book_data:
                print("-" * 40)
                for key, value in book.items():
                    print(f"{key}: {value}")
            print("-" * 40)
        else:
            print("未找到书籍数据。")
    else:
        print("无法获取页面内容。")

if __name__ == "__main__":
    main()