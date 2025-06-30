import os
from openai import OpenAI

model = "gpt-4o-mini"

client = OpenAI()


conversation=[
    {
               "role":"system",
               "content":"you are an expert advisor that works in a travel agency and know everything about France. You speak in a concise manner."
    },
    { 
        "role":"user",
        "content":"What is the most famous landmark in Paris?"
    },
    {
        "role":"assistant",
        "content":"The most famous landmark in Paris is the Eiffel Tower."
    },]
questions=[
    "How far away is the Louvre from the Eiffel Tower (in driving miles)?",
    "Where is the Arc de Triomphe?",
    "What are the must-see artworks at the Louvre Museum?",
]
for question in questions:
    input_dict = {"role": "user", "content": question}
    
    conversation.append(input_dict)  
    response = client.chat.completions.create(
        model=model,
        messages=conversation,
        temperature=0.0,
        max_tokens=100
    )
    
    resp = response.choices[0].message.content
    print(resp)

    resp_dict = {"role": "assistant", "content": resp}
    
    conversation.append(resp_dict)