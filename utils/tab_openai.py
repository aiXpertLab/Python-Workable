import streamlit as st,  openai, os

def init():
    client = openai.OpenAI()
    model="gpt-3.5-turbo-0125"
    model_v = "gpt-4-turbo"
    return client, model, model_v

def openai_general(para):
    st.code("""
        pass
    """)

def openai_vision():
    client, model, model_v = init()
    print(13)

    response = client.chat.completions.create(
        model=model_v,
        messages=[
            {
            "role": "user",
            "content": [
                {"type": "text", "text": "What’s in this image?"},
                {
                "type": "image_url",
                "image_url": {
                    "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/d/dd/Gfp-wisconsin-madison-the-nature-boardwalk.jpg/2560px-Gfp-wisconsin-madison-the-nature-boardwalk.jpg",
                },
                },
            ],
            }
        ],
        max_tokens=300,
    )

    st.text(response.choices[0])    
    
def openai_textcompletion():
    print(14)

    client, model, model_v = init()
    response = client.chat.completions.create(
        model = model,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Who won the world series in 2020?"},
            {"role": "assistant", "content": "The Los Angeles Dodgers won the World Series in 2020."},
            {"role": "user", "content": "Where was it played?"}
        ]
    )
    st.text(response.choices[0])
    st.info(response.choices[0].message)
    st.success(response.choices[0].message.content)
    st.write(response.id)
    st.write(response.model)
    st.write(response.usage)
    st.write(response.usage.total_tokens)   
