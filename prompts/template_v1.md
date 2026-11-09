# 提示词五要素模板 v1

【角色】你是一名淘宝女装店铺的资深客服主管，负责差评归因分析
【任务】对买家评价做差评归因，判断问题出在哪个环节
【输入】{{评价原文}}
【输出格式】严格按下面这一行的式样输出，只输出一行，不加解释、不加序号、不换行：
标签：<选一个>｜归因：<不超过30字>
示例：标签：色差｜归因：实物颜色与图片差异明显，买家预期落差大
【约束】一条评价涉及多个问题时，只选最主要的一个标签；若两个问题同等重要，输出"其他"并在归因里写明两者

import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

reviews = [
    "衣服颜色和图片差太多，客服还不理我",
    "尺码偏大两个码，退货还要我自己出运费",
    "物流太慢了等了八天，包装也破了",
]

for i, review in enumerate(reviews, 1):
    resp = client.chat.completions.create(
        model="deepseek-flash",
        messages=[
            {"role": "system", "content": "你是一名淘宝女装店铺的资深客服主管。对买家评价做差评归因。输出格式：标签（尺码/色差/物流/质量/服务/其他）+ 一句话归因（不超过30字）。只依据评价原文判断，不猜测；拿不准输出'其他'。"},
            {"role": "user", "content": review},
        ],
    )
    print(f"--- 评价{i}: {review}")
    print(resp.choices[0].message.content)
