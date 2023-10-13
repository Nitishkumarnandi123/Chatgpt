import openai
openai.api_key = "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"
model="text-davinci-003"
user=input("enter your question")
completion = openai.Completion.create(model= "text-davinci-003",
    prompt = user,
    max_tokens = 1024,
    temperature = 0.5,
    n=1,
    stop= None)
response = completion.choices[0].text
print(response)
