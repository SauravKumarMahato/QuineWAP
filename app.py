import streamlit as st
from gpt_requester import generate_code_with_gpt
import time
# import pyperclip

# Set the layout to a wide format
st.set_page_config(layout="wide")

# List of programming languages and frameworks
languages_frameworks = [
    "C++", "JavaScript", "Java", "Python", "C#", "Ruby", "Swift", "TypeScript",
    "HTML", "CSS", "PHP", "Go", "Rust", "Kotlin", "Objective-C", "Scala", "R",
    "Shell", "PowerShell", "Dart", "Perl", "Lua", "Haskell", "Groovy", "Matlab",
    "SQL", "Assembly", "Visual Basic", "Groovy", "Rust", "Django", "React", "Angular", "Vue.js",
    "Node.js", ".NET", "Spring", "Flask", "Express.js", "Rails", "Laravel", "Symfony"
]

# Left section
left_col = st.sidebar
left_col.title("Code Generator:")

# Box for code explanation
code_explanation = left_col.text_area("Explain the code you want to generate:", height=300, max_chars=1000)

# Selection for languages or frameworks
selected_language = left_col.selectbox("Select Language/Framework", languages_frameworks)

# Button to generate code with dynamic styling
generate_button_clicked = left_col.button(label="Generate Code", key="generate_button", help="Click to generate code")

# Variables for controlling the display speed
delay_between_words = 0.2

# Right section
right_col = st
right_col.title("Generated Code")
# st.markdown("<hr>", unsafe_allow_html=True)

# Generate code using GPT API when the button is pressed
if(code_explanation):
    generated_code = generate_code_with_gpt(code_explanation, selected_language)
else:
    generated_code = "Welcome to Code Generate Platfrom powered by ChatGPT"


         
if generate_button_clicked and code_explanation:

    if generated_code:
        # Split the generated code into lnes
        generated_lines = generated_code.split("\n")

        # Display each line with characters revealed one by one
        for line in generated_lines:
            st.text(line)
            time.sleep(delay_between_words)

# copy_button = right_col.button("Copy Code")

# Copy Code button and Markdown box
# if generated_code:
    # st.markdown(f"```{selected_language}\n{generated_code}\n```")