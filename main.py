# from dotenv import load_dotenv
# load_dotenv()

from langchain.llms import OpenAI
from langchain.chat_models import ChatOpenAI
import streamlit as st


chat_model = ChatOpenAI()

st.title("AI 시인 :sunglasses:")
content = st.text_input("주제를 제시해주세요")

if st.button("시 작성 시작하기"):
    with st.spinner("시 쓰는 중 📝"):
        result = chat_model.predict(content + "에 대한 시를 써줘")
        st.write(result)
