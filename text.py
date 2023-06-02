import os
import openai
openai.api_key = "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"
input_prompt = input("Enter prompt:\n")

while input_prompt != '0':
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": input_prompt}]
    )
    response = completion.choices[0].message['content']
    print("GPT: ",response)

    input_prompt = input("Enter prompt:\n")
