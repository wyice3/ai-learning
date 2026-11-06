import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()
client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",  # 关键：只改这一行就能用 DeepSeek
)

resp = client.chat.completions.create(
    model="deepseek-flash",  # 注意：旧名 deepseek-chat 已下线
    messages=[
        {"role": "system", "content": "你是一个电商运营助理"},
        {"role": "user", "content": "帮我把这条差评归因：衣服颜色和图片差太多，客服还不理我"},
    ],
)
print(resp.choices[0].message.content)
print("---- 本次消耗 token：", resp.usage.total_tokens)
