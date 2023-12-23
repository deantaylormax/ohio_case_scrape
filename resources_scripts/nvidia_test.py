import requests

invoke_url = "https://api.nvcf.nvidia.com/v2/nvcf/pexec/functions/8f4118ba-60a8-4e6b-8574-e38a4067a4a3"

headers = {
    "Authorization": "Bearer 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",
    "accept": "text/event-stream",
    "content-type": "application/json",
}

payload = {
  "messages": [
    {
      "content": "I am going to Paris, what should I see?",
      "role": "user"
    }
  ],
  "temperature": 0.2,
  "top_p": 0.7,
  "max_tokens": 1024,
  "seed": 42,
  "stream": True
}

response = requests.post(invoke_url, headers=headers, json=payload, stream=True)

for line in response.iter_lines():
    if line:
        print(line.decode("utf-8"))