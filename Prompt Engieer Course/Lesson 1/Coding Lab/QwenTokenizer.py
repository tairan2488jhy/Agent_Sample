from transformers import AutoTokenizer


def analyze_tokens(text):

  # 加载 Qwen 的 tokenizer（首次运行会自动下载词表文件）
  tokenizer = AutoTokenizer.from_pretrained("Qwen/Qwen2.5-7B", trust_remote_code=True)

  token_ids = tokenizer.encode(text)
  print(f"Token count: {len(token_ids)}")

  tokens = [tokenizer.decode([id]) for id in token_ids]
  print(f"tokens: {tokens}")

  print(f"Token IDS:{token_ids}")


if __name__ == "__main__":
  
  test_text_list = ["Hello AI Agent", "internationalization", "Artificial Intelligence", "人工智能", "你好，世界"]

  for test_text_item in test_text_list:
    print(test_text_item)
    analyze_tokens(test_text_item)
    print()













