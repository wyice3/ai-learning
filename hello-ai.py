# 第 1 天 · 环境验证脚本
# 运行方式：在 VS Code 里按 Ctrl+F5，或终端执行  python hello-ai.py

import sys
from datetime import date

name = "淘宝女装店铺"

print(f"你好，{name}！我的转行今天开始。")
print("今天装好了 Python、VS Code 和 Git。")
print()
print("-" * 40)
print(f"Python 版本：{sys.version.split()[0]}")
print(f"解释器路径：{sys.executable}")
print(f"今天日期：  {date.today()}")
print("-" * 40)
print("环境自检通过 ✓")
