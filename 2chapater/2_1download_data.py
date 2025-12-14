from code import interact
import tokenize
import urllib.request
import os
# 下载数据集
url = ("https://raw.githubusercontent.com/rasbt/"
        "LLMs-from-scratch/main/ch02/01_main-chapter-code/"
        "the-verdict.txt")

file_path = "./2chapater/the-verdict.txt"

# 如果文件不存在则下载文件
if not os.path.exists(file_path):
  print(f"Downloading file from {url} to {file_path}")
  urllib.request.urlretrieve(url, file_path)
else:
  print(f"File {file_path} already exists")

with open(file_path, 'r') as file:
  document = file.read()

# 可视化
print(f"total number of document: {len(document)}")
print(f"type of document: {type(document)}")
print(document[:99])

# 手动构建分词器tokenizer
import re
text = "Hello, world. Is this-- a test?"
# 根据标点符号和空格分割
# result = re.split(r'([,.:;?_!"()\']|--|\s)', text)
# result = [item for item in result if item.strip()]
# print(result)

# 对document进行分词操作
preprocessed = re.split(r'([,.:;?_!"()\']|--|\s)', document)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(len(preprocessed))
print(preprocessed[:100])

# 创建一个词汇表，对每一个token生成一个unique id
all_words = sorted(set(preprocessed)) # 创建一个set
vocab_size = len(all_words)
print(type(all_words))
print(vocab_size)

vacab = {token:integer for integer, token in enumerate(all_words)}
for i, item in enumerate(vacab.items()):
  print(item)
  if (i > 50):
    break

# 将token2id, id2token的操作抽象为一个类
class SimpleTokenizerV1:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s,i in vocab.items()}

  # 获取token对应的id列表，
  def encode(self, text):
    preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in  preprocessed if item.strip()]
    ids = [self.str_to_int[s] for s in preprocessed]

    return ids
  # 获取id列表对应的token
  def decode(self, ids):
    text = " ".join(self.int_to_str[id] for id in ids)
    text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
    return text

tokenizer = SimpleTokenizerV1(vacab)

text = """It's the last he painted, you know," Mrs. Gisburn said with pardonable pride."""

ids = tokenizer.encode(text)
print(ids)

print(tokenizer.decode(ids))

# 增加两种token标记，用于区分不同文档和不在训练集中的token

all_tokens = sorted(list(set(preprocessed)))
all_tokens.extend(["<|endoftext|>", "<|unk|>"])

vocab = {token:integer for integer, token in enumerate(all_tokens)}

print(len(vocab.items()))

for item in enumerate(list(vocab.items())[-5:]):
  print(item)

class SimpleTokenizerV2:
  def __init__(self, vocab):
    self.str_to_int = vocab
    self.int_to_str = {i:s for s,i in vocab.items()}

  # 获取token对应的id列表，
  def encode(self, text):
    preprocessed = re.split(r'([,.?_!"()\']|--|\s)', text)
    preprocessed = [item.strip() for item in  preprocessed if item.strip()]
    preprocessed = [item if item in self.str_to_int
                    else "<|unk|>" for item in preprocessed]
    ids = [self.str_to_int[s]  for s in preprocessed]

    return ids
  # 获取id列表对应的token
  def decode(self, ids):
    text = " ".join(self.int_to_str[id] for id in ids)
    text = re.sub(r'\s+([,.?!"()\'])', r'\1', text)
    return text

text1 = "Hello, do you like tea?"
text2 = "In the sunlit terraces of the palace."
text = " <|endoftext|> ".join((text1, text2))

tokenizer = SimpleTokenizerV2(vocab)
print(tokenizer.encode(text))
print(tokenizer.decode(tokenizer.encode(text)))

