# ChatGPT-python-example

演示如何使用 4 行代码调用 ChatGPT 的官方API。要求 Python 版本 > 3.6 。

## 1. 安装依赖

``` bash
pip3 install openai
```

## 2. 执行demo

``` bash
python3 bot.py
```

## 3. 修改对话内容

修改第 4 行代码里的 `content` 参数即可。例如：

``` py
completion = openai.Completion.create(model="gpt-3.5-turbo", \
                                       messages=[{"role": "user", "content": "请使用 Python 实现一个二分查找算法"}])
```

## 4. 切换模型（可选）

通过修改第 4 行代码里的 `model` 参数即可指定模型。可选的模型详见 [models](https://platform.openai.com/docs/models) 。
