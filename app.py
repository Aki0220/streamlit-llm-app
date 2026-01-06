import streamlit as st
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage

load_dotenv()

st.title("LLM専門家アプリ")
st.write("専門家を選び、質問を入力してください。")

expert = st.radio(
    "専門家を選択",
    ["プログラミングの専門家", "ビジネスの専門家"]
)

user_input = st.text_input("質問を入力")

def ask_llm(text, expert_type):
    system_prompt = (
        "あなたは優秀なプログラミングの専門家です。"
        if expert_type == "プログラミングの専門家"
        else "あなたは経験豊富なビジネスコンサルタントです。"
    )

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

    messages = [
        SystemMessage(content=system_prompt),
        HumanMessage(content=text)
    ]

    return llm(messages).content

if st.button("送信"):
    if user_input:
        answer = ask_llm(user_input, expert)
        st.write("### 回答")
        st.write(answer)