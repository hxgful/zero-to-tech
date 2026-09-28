import requests

url = "https://api.deepseek.com/chat/completions"

headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer sk-e12efb426f284d97939bcdce18374bf7" # 👈 请在这里填入你新生成的 Key
}

data = {
    "model": "deepseek-chat", # 这里是模型名字，如果你要专门用轻量级可以用 "deepseek-flash"
    "messages": [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "你好，请用一句话介绍你自己！"}
    ],
    "stream": False
}

try:
    print("正在向 DeepSeek 发送请求...")
    response = requests.post(url, headers=headers, json=data)
    
    # 检查状态码
    if response.status_code == 200:
        result = response.json()
        ai_reply = result["choices"][0]["message"]["content"]
        print("\n✅ API 调用成功，AI 回复如下：")
        print(ai_reply)
    else:
        print(f"\n❌ 请求失败，状态码: {response.status_code}")
        print("错误信息:", response.text)

except Exception as e:
    print("\n❌ 发生网络异常:")
    print(e)
