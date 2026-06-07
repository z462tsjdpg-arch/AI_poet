from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
import streamlit as st

chat_model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

st.title("인공지능 시인")

subject = st.text_input("시의 주제를 입력해 주세요")

if st.button("시 작성"):
    with st.spinner("시 작성 중..."):
        result = chat_model.invoke(subject + "에 대한 시를 써줘")
        st.write(result.content)