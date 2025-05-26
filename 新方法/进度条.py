import time
import math


def progress_bar(total_time, bar_width=30, fill_char='█', empty_char=' '):
    """
    可设定时间的加载进度条（精确到0.1秒）

    参数：
    total_time  - 总加载时间（秒）
    bar_width   - 进度条宽度（字符数）
    fill_char   - 填充字符
    empty_char  - 空白字符
    """
    steps = max(math.ceil(total_time * 10), 1)  # 每0.1秒更新一次
    step_time = total_time / steps
    start_time = time.time()

    for i in range(steps + 1):
        # 计算实际进度（0.0~1.0）
        progress = min(i / steps, 1.0)

        # 绘制进度条
        filled = int(round(bar_width * progress))
        bar = fill_char * filled + empty_char * (bar_width - filled)

        # 计算动态剩余时间
        elapsed = time.time() - start_time
        remaining = max(total_time - elapsed, 0)

        # 格式化输出
        print(f"\r|{bar}| {progress * 100:6.2f}% 剩余: {remaining:.1f}s", end='')

        # 动态调整等待时间
        target_time = start_time + (i + 1) * step_time
        sleep_time = max(target_time - time.time() - 0.001, 0)
        if sleep_time > 0:
            time.sleep(sleep_time)

    print("\n完成！")


# 使用示例（3秒的加载条）
progress_bar(total_time=5, bar_width=40, fill_char='L', empty_char='（')