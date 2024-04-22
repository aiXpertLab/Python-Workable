import streamlit as st, json
from datetime import datetime

def db_JSON():
    st.markdown('### json字符串 转 Python数据类型`json.loads` ')
    json_string = '''
    {
        "name": "crise",
        "age": 18,
        "parents": {
            "monther": "妈妈",
            "father": "爸爸"
        }
    }'''

    st.write(f"json_string数据类型： {type(json_string)}")
    data = json.loads(json_string)
    st.write(f"data数据类型：,{type(data)}")
    st.write(data)
    st.divider()
    st.subheader('Python数据类型 转 json字符串`json.dumps` ')
    data = {
        "name": "crise",
        "age": 18,
        "parents": {
            "monther": "妈妈",
            "father": "爸爸"
        }
    }
    st.write(f"data数据类型：,{type(data)}")
    json_string = json.dumps(data)
    st.write(f"json_string数据类型： {type(json_string)}")
    st.write(json_string)

    st.divider()
    st.markdown('### json文件 转 Python数据类型 `json.load`')
    # with open('data.json','r',encoding='utf-8') as f:
    #     data = json.load(f)
    #     st.write("data数据类型：", type(data))
    #     st.write(data)

    # st.write("*"*100)
    # # json.dump Python数据类型 转 json文件
    # data = {
    #     "name": "crise",
    #     "age": 18,
    #     "parents": {
    #         "monther": "妈妈",
    #         "father": "爸爸"
    #     }
    # }
    # with open('data_out.json','w',encoding='utf-8') as f:
    #     json.dump(data,f,ensure_ascii=False,indent=2)

def db_general():
    st.write('date')
    formatted_date = datetime.strptime("12/2/2022", '%m/%d/%Y').strftime('%Y-%m-%d')
    st.subheader(formatted_date)
    
def db_jsoncsv():
    st.info("In most cases, there's no reason to pick the csv library over pandas.")
    st.code("""
        # CSV    
        import csv
        import pandas as pd

        # Sample data
        data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 28]}
        df = pd.DataFrame(data)

        # Using csv library (manual control)
        with open('data.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(df.columns)  # Write header manually
        for index, row in df.iterrows():
            writer.writerow(row.tolist())  # Convert each row to list manually

        # Using pandas.DataFrame.to_csv (automatic formatting)
        df.to_csv('data_pandas.csv', index=False)  # Save without index
        

        #JSON        
        import json

        contexts = []  # Replace with your actual data

        # Function to save contexts as JSON
        def save_contexts_as_json(contexts, filename="contexts.json"):
            with open(filename, 'w') as f:
                json.dump(contexts, f, indent=4)  # Add indentation for readability

        # Save contexts
        save_contexts_as_json(contexts)
        

        contexts_df = pd.DataFrame(contexts)  # Assuming contexts is a list of dictionaries

        # Save contexts as JSON
        contexts_df.to_json("contexts.json", orient="records")  # Save each row as a JSON object


        #Retrieve/Load
        csv_file = "data.csv"
        df = pd.read_csv(csv_file)
        
        df = pd.read_json(json_file)
            """)

    import csv
    import pandas as pd

    # Sample data
    data = {'name': ['Alice', 'Bob', 'Charlie'], 'age': [25, 30, 28]}
    df = pd.DataFrame(data)

    # Using csv library (manual control)
    with open('./data/data_csv.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(df.columns)  # Write header manually
        for index, row in df.iterrows():
            writer.writerow(row.tolist())  # Convert each row to list manually

    # Using pandas.DataFrame.to_csv (automatic formatting)
    df.to_csv('./data/data_pandas.csv', index=False)  # Save without index
    
    
    contexts = ['Alice', 'Bob', 'Charlie']  # Replace with your actual data

    # Function to save contexts as JSON
    def save_contexts_as_json(contexts, filename="./data/contexts_json.json"):
        with open(filename, 'w') as f:
            json.dump(contexts, f, indent=4)  # Add indentation for readability

    # Save contexts
    save_contexts_as_json(contexts)
    

    contexts_df = pd.DataFrame(contexts)  # Assuming contexts is a list of dictionaries
    # Save contexts as JSON
    contexts_df.to_json("./data/contexts_pd.json", orient="records")  # Save each row as a JSON object

