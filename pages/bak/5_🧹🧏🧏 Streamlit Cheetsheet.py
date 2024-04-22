import streamlit as st
import pandas as pd, numpy as np

data = {
    'A': np.random.rand(10),
    'B': np.random.randint(1, 100, size=10),
    'C': np.random.choice(['X', 'Y', 'Z'], size=10)
}

my_dataframe = pd.DataFrame(data)

# Basics

# Title and header
st.title('My Streamlit App')
st.header('Welcome to my app!')

# Text and markdown
st.text('This is plain text.')
st.markdown('This is **markdown** text.')

# Data display
st.dataframe(my_dataframe)  # Display a DataFrame
st.table(my_dataframe)  # Display a static table

# Widgets

# Button
if st.button('Click me'):
    st.write('Button clicked!')

# Checkbox
if st.checkbox('Show/Hide'):
    st.write('Content is visible.')

# Radio buttons
option = st.radio('Select an option', ('Option 1', 'Option 2', 'Option 3'))
st.write(f'You selected: {option}')

# Selectbox
option = st.selectbox('Select an option', ('Option 1', 'Option 2', 'Option 3'))
st.write(f'You selected: {option}')

# Multiselect
options = st.multiselect('Select multiple options', ('Option 1', 'Option 2', 'Option 3'))
st.write(f'You selected: {options}')

# Slider
value = st.slider('Select a value', min_value=0, max_value=100, value=50, step=1)
st.write(f'You selected: {value}')

# Text input
text = st.text_input('Enter your name')
st.write(f'Hello, {text}!')

# Number input
number = st.number_input('Enter a number', min_value=0, max_value=100, value=50, step=1)
st.write(f'You entered: {number}')

# Date input
date = st.date_input('Select a date')
st.write(f'You selected: {date}')

# Time input
time = st.time_input('Select a time')
st.write(f'You selected: {time}')

# File uploader
uploaded_file = st.file_uploader('Choose a file')
if uploaded_file is not None:
    # Process the uploaded file
    pass

# Color picker
color = st.color_picker('Pick a color')
st.write(f'You selected: {color}')

# Layout

# Sidebar
st.sidebar.title('Sidebar Title')
st.sidebar.button('Sidebar Button')

# Columns
col1, col2, col3 = st.columns(3)
with col1:
    st.header('Column 1')
    st.write('Content for column 1')
with col2:
    st.header('Column 2')
    st.write('Content for column 2')
with col3:
    st.header('Column 3')
    st.write('Content for column 3')

# Expander
with st.expander('Click to expand'):
    st.write('This content is hidden by default.')

# Container
with st.container():
    st.write('This content is inside a container.')

# Empty
st.empty()  # Create an empty placeholder

# Progress and Status

# Progress bar
progress_bar = st.progress(0)
for i in range(100):
    # Simulate progress
    progress_bar.progress(i + 1)

# Spinner
with st.spinner('Loading...'):
    # Simulate a long-running operation
    pass

# Success message
st.success('Operation successful!')

# Info message
st.info('This is an informational message.')

# Warning message
st.warning('This is a warning message.')

# Error message
st.error('This is an error message.')

# Exception
try:
    # Some code that may raise an exception
    pass
except Exception as e:
    st.exception(e)

# Plotting

# Line chart
st.line_chart(data)

# Area chart
st.area_chart(data)

# Bar chart
st.bar_chart(data)


st.code("""
# Do's and Don'ts

# Do: Use meaningful variable and function names
# Don't: Use single-letter or cryptic variable and function names

# Do: Break down your code into smaller, reusable functions
# Don't: Write long, monolithic functions

# Do: Use caching when dealing with expensive computations or loading data
# Don't: Recompute expensive operations unnecessarily

# Do: Handle exceptions and display informative error messages
# Don't: Let exceptions go unhandled, leading to a broken app

# Do: Use layout components to organize your app's UI
# Don't: Clutter your app with unorganized widgets

# Do: Provide clear instructions and guidance to users
# Don't: Assume users will know how to use your app without any guidance

# Do: Test your app thoroughly before deploying
# Don't: Deploy an untested app with potential bugs or errors

# Do: Keep your app's design simple and intuitive
# Don't: Overcomplicate the UI with unnecessary elements or confusing layouts

# Do: Optimize your app's performance by minimizing the use of expensive operations
# Don't: Ignore performance considerations, leading to a slow and unresponsive app

# Do: Regularly update and maintain your app
# Don't: Neglect your app after deployment, leading to outdated or broken functionality

""")