import openai
openai.api_key = "sk-XXXXXXXXXX"  # 你的 OpenAI API Key

# create a completion
completion = openai.Completion.create(model="gpt-3.5-turbo", \
                                       messages=[{"role": "user", "content": "What is the OpenAI mission?"}], \
                                        api_base="https://api.openai.com/v1/chat")

# print the completion
print(completion.choices[0].message.content)