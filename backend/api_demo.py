import os
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()
api_key = os.getenv("DEEPSEEK_API_KEY")

if not api_key:
    print("❌ 错误：未找到 API Key，请检查 .env 文件是否正确配置。")
    exit()

url = "https://api.deepseek.com/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}

# 初始化对话历史。多轮对话的关键就是维护这个列表！
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

print("=========================================")
print("🤖 DeepSeek 终端聊天助手已启动！")
print("输入你的问题，按回车发送。输入 'exit'、'quit' 或 'q' 退出。")
print("=========================================\n")

while True:
    # 1. 接收用户输入
    user_input = input("👤 你: ")
    
    # 检查是否要退出
    if user_input.lower() in ['exit', 'quit', 'q']:
        print("👋 再见！")
        break
    
    # 如果用户输入为空，跳过本次循环
    if not user_input.strip():
        continue

    # 2. 把用户的问题加入历史记录
    messages.append({"role": "user", "content": user_input})

    # 3. 准备发给 API 的数据
    data = {
        "model": "deepseek-chat", 
        "messages": messages, # 👈 注意这里发送的是整个聊天历史
        "stream": False
    }

    # 4. 发送请求
    try:
        response = requests.post(url, headers=headers, json=data)
        
        if response.status_code == 200:
            result = response.json()
            ai_reply = result["choices"][0]["message"]["content"]
            
            print(f"\n🤖 AI: {ai_reply}\n")
            
            # 5. 非常重要：把 AI 的回答也加入历史记录，否则 AI 会失忆
            messages.append({"role": "assistant", "content": ai_reply})
            
        else:
            print(f"\n❌ 请求失败，状态码: {response.status_code}")
            print("错误信息:", response.text)
            # 如果请求失败，把刚才加入的用户问题删掉，避免污染历史记录
            messages.pop()

    except Exception as e:
        print("\n❌ 发生网络异常:")
        print(e)
        messages.pop()