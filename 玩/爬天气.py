import requests
from lxml import etree
import csv
import time
import random

# 请求URL
BASE_URL = "http://www.weather.com.cn/weather1d/"

# 城市代码列表 (例如：北京、上海)
CITY_CODES = ["101010100", "101020100"]  # 北京, 上海

# 请求头部
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# 解析页面函数
def parse_html(html):
    try:
        selector = etree.HTML(html)

        city = selector.xpath('//*[@id="around"]/div/div[1]/div[1]/h1/text()')
        if city:
            city = city[0]
        else:
            print("未能找到城市名称")
            city = None

        temperature = selector.xpath('//*[@id="around"]/div/div[1]/div[1]/p/i/text()')
        if temperature:
            temperature = temperature[0]
        else:
            print("未能找到温度")
            temperature = None

        weather = selector.xpath('//*[@id="around"]/div/div[1]/div[1]/p/@title')
        if weather:
            weather = weather[0]
        else:
            print("未能找到天气")
            weather = None

        wind = selector.xpath('//*[@id="around"]/div/div[1]/div[1]/p/span/text()')
        if wind:
            wind = wind[0]
        else:
            print("未能找到风力")
            wind = None

        return city, temperature, weather, wind
    except Exception as e:
        print(f"解析 HTML 时发生错误：{e}")
        return None, None, None, None

# 保存数据函数
def save_data(data, filename="weather_data.csv"):
    try:
        with open(filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['城市', '温度', '天气', '风力'])  # 写入标题行
            writer.writerows(data)  # 写入多行数据
        print(f"数据已成功保存到 {filename}")
    except Exception as e:
        print(f"写入 CSV 文件时发生错误：{e}")


def main():
    all_weather_data = []  # 用于存储所有城市的天气数据

    for city_code in CITY_CODES:
        url = BASE_URL + city_code + ".shtml"
        try:
            response = requests.get(url, headers=headers, timeout=10)
            response.raise_for_status()

            # 检查是否成功获取到内容
            if not response.text:
                print(f"未能获取城市代码为 {city_code} 的网页内容")
                continue

            city, temperature, weather, wind = parse_html(response.text)

            if city and temperature and weather and wind:
                all_weather_data.append([city, temperature, weather, wind])
            else:
                print(f"未能成功提取城市代码为 {city_code} 的天气数据。")

        except requests.exceptions.RequestException as e:
            print(f"请求城市代码为 {city_code} 的 URL 时发生错误：{e}")
        except Exception as e:
            print(f"处理城市代码为 {city_code} 的数据时发生未知错误：{e}")

        # 随机延迟，模拟人类行为
        delay = random.uniform(1, 3)  # 随机暂停 1 到 3 秒
        print(f"暂停 {delay:.2f} 秒...")
        time.sleep(delay)

    if all_weather_data:
        save_data(all_weather_data)  # 保存所有城市的数据
    else:
        print("未能成功提取任何城市的天气数据。")


if __name__ == '__main__':
    main()