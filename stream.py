import os
import time

from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

question = "帮我把这条差评归因：衣服颜色和图片差太多，客服还不理我"

t0 = time.time()
first_token_at = None

stream = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个电商运营助理"},
        {"role": "user", "content": question},
    ],
    stream=True,  # 关键：不是等全部算完，而是一边算一边给
)

for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta

    # 思考过程（有的模型会返回，不是正文，单独用浅色打出）
    reasoning = getattr(delta, "reasoning_content", None)
    # if reasoning:
    #     if first_token_at is None:
    #         first_token_at = time.time()
    #         print(f"[首字延迟 {first_token_at - t0:.2f}s]\n")
    #     print(reasoning, end="", flush=True)

    # 正文
    if delta.content:
        if first_token_at is None:
            first_token_at = time.time()
            print(f"[首字延迟 {first_token_at - t0:.2f}s]\n")
        print(delta.content, end="", flush=True)

print(f"\n\n---- 总耗时 {(time.time() - t0):.2f}s")
