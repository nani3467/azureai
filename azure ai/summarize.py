from openai import AzureOpenAI

deployment_name = "gpt-5-mini"
# Use the alternative standard Azure OpenAI resource endpoint and key from cell qh-BHZ7lOvyX
endpoint_clean = "https://25695a3213-7074-resource.services.ai.azure.com/"
api_key_clean = "1IXGlGyFuQDkf8VKgLbvr8Y23CpsnZoXuY2UzpriSNK0nMKvwpijJQQJ99CKACF24PCXJ3w3AAAAACOGAU2X"

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
            "content": "You are a text summarization assistant. Summarize the given text into 3-5 simple sentences. Include only the important information."
        },
        {
            "role": "user",
            "content": """
            Artificial Intelligence is a branch of computer science 
            that focuses on creating machines capable of performing 
            tasks that normally require human intelligence. AI is used 
            in healthcare, education, banking, agriculture, and transportation.
            Machine learning and deep learning are important technologies 
            used in AI applications.
            """
        }
    ]
)

print(f"answer: {response.choices[0].message.content}")