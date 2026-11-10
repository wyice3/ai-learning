import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# 同一需求的三种问法：A 随口问 / B 加角色+对象 / C 完整五要素
# 注意：今天比较的是"问法"，不是稳定性，所以用官方默认 temperature=1.0（不设这个参数）
asks = [
    ("A 随口问",
     "帮我写几条加绒打底裤的卖点"),

    ("B 加角色+对象",
     "你是有10年经验的淘宝女装主播。给怕冷的上班族女生写5条加绒打底裤卖点短句，"
     "每条不超过15字，口语化，突出轻、暖、不臃肿"),

    ("C 完整五要素",
     "你是淘宝女装直播间的资深主播兼文案，负责为冬季爆款写口播短句。\n"
     "任务：给加绒打底裤写卖点短句，用于直播口播。\n"
     "目标人群：25-35岁上班族女生，怕冷又不想穿得臃肿。\n"
     "输出格式：严格输出5行，每行一条，行首带序号1-5，每条不超过15字，口语化，不加其他解释。\n"
     "示例：1. 0度天出门，腿上像贴了暖宝宝\n"
     "约束：只围绕轻、暖、不臃肿三个卖点展开；不出现'最'、'第一'这类极限词；不用书面语。"),
]

for name, prompt in asks:
    resp = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "user", "content": prompt},
        ],
    )
    print(f"\n{'='*50}\n[{name}]\n{'='*50}")
    print(resp.choices[0].message.content)
