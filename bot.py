import openai
openai.api_key = "sk-XXXXXXXXXX"  # 你的 OpenAI API Key

# create a completion
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", \
                                       messages=[{"role": "user", "content": "如何评价《三体》这部小说？"}])

# print the completion
print(completion.choices[0].message.content)
