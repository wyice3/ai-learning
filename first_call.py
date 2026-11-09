import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

# 提示词模板 v3：与 prompts/template_v3.md 保持一致
SYSTEM_PROMPT = """你是一名淘宝女装店铺的资深客服主管，负责差评归因分析。
任务：对买家评价做差评归因，判断问题出在哪个环节。
输出格式：严格按下面这一行的式样输出，只输出一行，不加解释、不加序号、不换行、不加句号：
标签：<选一个>｜归因：<不超过30字>
示例：标签：色差｜归因：实物颜色与图片差异明显，买家预期落差大
约束：
1. 标签只能从这六个里选一个：尺码、色差、物流、质量、服务、其他
2. 只依据评价原文判断，不猜测评价里没提的事
3. 归因优先级（按顺序取第一个命中的标签，不要因为两个问题都突出就输出其他）：
① 质量：商品本身破损、开线、有污渍、有异味
② 色差：颜色或材质与详情页不符
③ 尺码：偏大、偏小、与尺码表不符
④ 物流：发货慢、配送慢、快递磕碰（包装破损归物流，不含商品本身损坏）
⑤ 服务：客服不回复、态度差、售后推诿
⑥ 其他：以上都不命中时才用
4. 拿不准就输出其他"""

reviews = [
    "衣服颜色和图片差太多，客服还不理我",
    "尺码偏大两个码，退货还要我自己出运费",
    "物流太慢了等了八天，包装也破了",
]

for i, review in enumerate(reviews, 1):
    resp = client.chat.completions.create(
        model="deepseek-flash",
        temperature=0.0,  # 官方默认 1.0；这里设 0 是为了让多次运行可比（只能降低随机性，不能保证逐字一致）
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": review},
        ],
    )
    print(f"--- 评价{i}: {review}")
    print(resp.choices[0].message.content)
