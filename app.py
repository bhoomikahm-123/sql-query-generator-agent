import streamlit as st
import openai

# Set your OpenRouter API key from secrets
api_key = st.secrets["openrouter_api_key"]

# Set up the OpenAI client for OpenRouter
client = openai.OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

st.title("🧠 SQL Chatbot")
st.write("Ask a question in natural language, and I'll convert it into an SQL query!")

user_input = st.text_input("Ask your SQL question:")

if user_input:
    with st.spinner("Generating SQL query..."):
        try:
            response = client.chat.completions.create(
                model="mistralai/mistral-7b-instruct:free",
                messages=[
                    {"role": "system", "content": "You are an expert SQL assistant. Convert user input into SQL queries only."},
                    {"role": "user", "content": user_input}
                ]
            )
            sql_query = response.choices[0].message.content.strip()
            st.success("Here's your SQL query:")
            st.code(sql_query, language="sql")
        except Exception as e:
            st.error(f"❌ Error: {str(e)}")
