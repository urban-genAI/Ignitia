import openai

openai.api_key = "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"

input_image_prompt = input("Enter prompt:\n")

# Generate an image based on text prompt
response = openai.Image.create(
  prompt=input_image_prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)
