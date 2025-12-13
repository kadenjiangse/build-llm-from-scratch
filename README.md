# Build a Language Model(From Scratch) notes and code implention 
## 1理解大语言模型

### 1.3构建llm的两个阶段

介绍了从零构建llm的两个阶段，分别是预训练（pretrained）和微调（fine-tuning， FT）。

预训练阶段是在没有标签的超大数据集上训练的，模型从输入数据中自己生成标签，属于自监督训练。给定一个词语，通过不断优化权重网络，来最大化网络输出正确标签（句子中的下一个词语）的概率。预训练模型具有基本的文本补全和小样本能力，是一个基础模型，例如gpt3

FT一般是在有标签的小数据集上去针对特定任务做训练，最常见的就是指令微调（instruction fine-tuning， IFT）和分类微调（classification fine-tuning， CFT）。IFT的训练数据是指令和答案对，例如（query， answer），在这种结构的数据上训练之后，可以增强模型的问答能力。CFT是的训练数据是文本及对应的标签对，例如（text， label），同样，这样的训练数据可以增强模型在分类任务的表现

### 1.4transformer架构

介绍了基本的transformer架构，以及两种不同的训练方式。GPT的transformer通过预测句子中下一个词来训练，而BERT采用掩码的方式，预测句子中间的词。

介绍了文本补全，零样本（zero-shot），小样本（few-shot）的概念。文本补全直接让大模型补全文本；零样本指的是不给大模型关于该任务的任何例子，直接让大模型执行任务；小样本是指给少量的例子给大模型，让它执行任务

```js
//补全
prompt: i like appl  
// zero-shot
prompt: 把中文翻译成英文  早餐=> 
// few-shot
prompt: 好吃=>吃好  美丽=>丽美  天气=>
```

### 1.5数据集

介绍了预训练的数据集，多个数据集总共4100亿token

### 1.6介绍多种gpt的架构

gpt  gpt3 chatgpt，突出gpt原始模型的重要性，表明本书的研究重点是gpt

gpt只用多个decoder来训练，训练任务是预测句子中的下一个词，gpt3有更多的参数并且使用encoding-decoding的架构

### 1.7构建llm的详细步骤

介绍了三个主要的构建阶段及相关细节

第一阶段：加载数据集（小一点的），编写llm的核心代码（注意力机制），训练前的准备阶段

第二阶段：预训练阶段，建立训练循环，评估网络，得到可以预测文本的base model

第三阶段：微调阶段，加载预训练模型，在问答任务和分类任务上进行微调

## 2数据准备

### 2.1理解词嵌入

讲解了为什么要进行embedding，embedding的方式（word2ec和训练阶段的特征提取网络），embedding维度的优略

word2vec采用的是固定的窗口采样训练样本对，更多的是词义的静态嵌入，没有考虑语境；而llm中的embedding输入是句子（预测句子的下一个词），利用transformer的强大上下文感知能力，可以综合语境，得到的是上下文相关的动态嵌入

byte pair encoding,

### 2.2如何将文本转换为token




