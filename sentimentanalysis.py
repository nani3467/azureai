from openai import AzureOpenAI

deployment_name = "gpt-5-mini"
# Use the alternative standard Azure OpenAI resource endpoint and key from cell qh-BHZ7lOvyX
endpoint_clean = "abcd"
api_key_clean = "1234"

client = AzureOpenAI(
    azure_endpoint=endpoint_clean,
    api_key=api_key_clean,
    api_version="2024-08-01-preview"
)

response = client.chat.completions.create(
    model=deployment_name,
   messages=[
         {
            "role": "system",
            "content": "You are a sentiment analysis assistant. Determine whether the sentiment is positive, negative, or mixed. Identify the positive and negative aspects."
        },
        {
            "role": "user",
            "content": "The camera quality of this phone is amazing, but battery is terrible."
        }
    ]
)

print(f"answer: {response.choices[0].message.content}")
