"""
Token Analyzer
目标：

实现你的第一个 AI 工程工具。

功能：

输入：

文本
输出：

Token数量

Token列表

Token ID
例如：

输入：

Hello AI Agent
输出：

Token count:

3


Tokens:

Hello
AI
Agent
推荐技术：

Python

安装：

pip install tiktoken
实验：

比较：

Hello
internationalization
人工智能
AI Agent Engineer
观察：

Token 数量变化。

Windows/Linux: Ctrl + Shift + P
Python: Select Interpreter 选择自己项目的编译器


"""


# 2. 创建虚拟环境： py -3 -m venv .venv

# 3. 激活： .venv\Scripts\activate

import tiktoken

def analyze_tokens(text):
  """分析输入文本的token信息"""
  """— 加载一个编码器对象。cl100k_base 是 GPT-3.5 和 GPT-4 使用的编码规则，词汇表大约 10 万个 token。"""
  encoding  = tiktoken.get_encoding("cl100k_base")
  # 2. 将文本转换为 Token ID 列表
  token_ids = encoding.encode(text)

  # 3. 打印 Token 数量
  print(f"Token count :{len(token_ids)}")

  # 4. 打印 Token 列表（将 ID 还原为可读的文本片段）
  tokens = [encoding.decode([id]) for id in token_ids]
  print(f"Tokens: {tokens}") 

  # 5.中文字节码问题
  token_bytes = [encoding.decode_single_token_bytes(id) for id in token_ids]
  print(f"Token_bytes: {token_bytes}")

  token_encode  =encoding.encode(text)
  print(f"Token_encode: {token_encode}")



if __name__ == "__main__":
  # # 测试文本
  # test_text = "Hello AI Agent"
  # analyze_tokens(test_text)

  # test_text = "Hello"
  # analyze_tokens(test_text)

  # test_text = "internationalization"
  # analyze_tokens(test_text)

  # test_text = "人工智能"
  # analyze_tokens(test_text)


  """
  对一个输出的实验结果：
Token count :3
Tokens: ['Hello', ' AI', ' Agent']

Token count :1
Tokens: ['Hello']

Token count :2
Tokens: ['international', 'ization']

Token count :5
Tokens: ['人', '工', '�', '�', '能']
  """

test_text_list2 = ["Hello AI Agent", "internationalization", "Artificial Intelligence", "人工智能", "你好，世界"]

for test_text_item in test_text_list2:
  print(test_text_item)
  analyze_tokens(test_text_item)
  print()


  



