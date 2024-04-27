from openai import OpenAI
import os

client = OpenAI()
    
models = client.models.list()

print(models)