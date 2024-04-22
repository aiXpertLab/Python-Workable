import streamlit as st,  openai, os

def init():
    client = openai.OpenAI()
    model="gpt-3.5-turbo-0125"
    model_v = "gpt-4-turbo"
    return client, model, model_v
    # openai.api_key = os.environ.get("OPENAI_API_KEY")
    # defaults to getting the key using os.environ.get("OPENAI_API_KEY")
    # if you saved the key under a different environment variable name, you can do something like:
    # client = OpenAI(
    #   api_key=os.environ.get("CUSTOM_ENV_NAME"),
    # )

def openai_general():
    st.image("./images/traditional_vector.png")
    st.code("""
        pass
    """)



def openai_mongo():
    st.code("""
        pass
    """)

def openai_postgreql():
    st.code("""
    import psycopg2,os
    uri = os.environ.get('POSTGRESQL_URI')
    def main():
        conn = psycopg2.connect(uri)
        query_sql = 'SELECT VERSION()'
        cur = conn.cursor()
        cur.execute(query_sql)
        version = cur.fetchone()[0]
        st.success(version)
    """)
   

def openai_vision():
    client, model, model_v = init()

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

    st.success(response.choices[0].message.content)
