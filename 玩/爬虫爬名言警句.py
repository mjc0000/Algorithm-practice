import requests
from bs4 import BeautifulSoup
import csv

# 目标网站 URL
TARGET_URL = "http://quotes.toscrape.com/"

def fetch_data(url):
    """
    从指定的 URL 获取页面内容.
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()  # 检查 HTTP 状态码
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None

def parse_quotes(html_content):
    """
    从 HTML 内容中提取名言警句、作者和标签.
    """
    soup = BeautifulSoup(html_content, 'html.parser')
    quotes = []

    quote_elements = soup.find_all('div', class_='quote')  # 找到所有名言的 div

    for quote_element in quote_elements:
        text = quote_element.find('span', class_='text').text  # 提取名言内容
        author = quote_element.find('small', class_='author').text  # 提取作者
        tags = [tag.text for tag in quote_element.find_all('a', class_='tag')]  # 提取标签列表

        quotes.append({
            'text': text,
            'author': author,
            'tags': tags
        })

    return quotes

def save_to_csv(data, filename="quotes.csv"):
    """
    将数据保存到 CSV 文件.
    """
    if not data:
        print("没有数据可写入 CSV 文件。")
        return

    fieldnames = data[0].keys()

    try:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"数据已成功保存到 {filename}")
    except Exception as e:
        print(f"写入 CSV 文件时发生错误：{e}")

def main():
    """
    主函数，执行爬取、解析和保存操作.
    """
    all_quotes = []  # 用于存储所有页面的名言

    # 循环爬取所有页面，直到没有下一页链接
    page_num = 1
    while True:
        url = TARGET_URL + f"page/{page_num}/" if page_num > 1 else TARGET_URL # 构建 URL
        html_content = fetch_data(url)

        if html_content:
            quotes = parse_quotes(html_content)
            if quotes:
                all_quotes.extend(quotes)  # 将当前页面的名言添加到总列表中
            else:
                print(f"在第 {page_num} 页未找到名言。")
                break # 如果本页没有，说明到头了

            # 检查是否有下一页链接
            soup = BeautifulSoup(html_content, 'html.parser')
            next_page_link = soup.find('li', class_='next')
            if not next_page_link:
                print("没有找到下一页链接，爬取结束。")
                break # 没有下一页了

            page_num += 1 # 准备爬取下一页
            print(f"正在爬取第 {page_num} 页...") # 输出爬取进度
        else:
            print(f"无法获取第 {page_num} 页的内容。")
            break

    if all_quotes:
        save_to_csv(all_quotes)  # 保存到 CSV 文件
        print("抓取到的名言数据：")
        for quote in all_quotes:
            print("-" * 40)
            for key, value in quote.items():
                print(f"{key}: {value}")
            print("-" * 40)
    else:
        print("未找到任何名言数据。")


if __name__ == "__main__":
    main()