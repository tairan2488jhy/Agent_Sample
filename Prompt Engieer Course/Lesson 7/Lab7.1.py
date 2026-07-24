from transformers import AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained(
  "Qwen/Qwen2.5-7B-Instruct"
)

message = [
  {
    "role": "system",
    "content": "Your are helpful assistant."
  },
  {
    "role": "user",
    "content": "Explain Transformer."
  }
]

text = tokenizer.apply_chat_template(
  message,
  tokenize = False
)

print(text)