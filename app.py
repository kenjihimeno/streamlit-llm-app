from dotenv import load_dotenv

load_dotenv()

from openai import OpenAI
import os
import streamlit as st

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

st.title("Chapter6：【提出課題】LLM機能を搭載したWebアプリを開発しよう")

st.write("##### 動作モード1: サッカーの専門家")
st.write("サッカーのスコア予想を行います。予想してほしい試合情報を入力してください。")
st.write("##### 動作モード2: クラシック音楽の専門家")
st.write("クラシック音楽に関する質問に答えます。")

selected_item = st.radio(
    "動作モードを選択してください。",
    ["サッカー、スコア予想", "クラシック音楽の専門家"]
)

st.divider()

if selected_item == "サッカー、スコア予想":
    input_message = st.text_input(label="予想してほしい試合情報を入力してください。")

else:
    input_message = st.text_input(label="クラシック音楽に関する質問を入力してください。")

    
if st.button("実行"):
    st.divider()
    
    if input_message:
        if selected_item == "サッカー、スコア予想":
            role_prompt = "あなたはサッカーの専門家です。試合情報をもとにスコアを予想してください。"
            st.write(f"試合情報「{input_message}」に基づくスコア予想を実行中...")
            
        else:
            role_prompt = "あなたはクラシック音楽の専門家です。正確かつ深い知識で質問に答えてください。"
            st.write(f"クラシック音楽の質問「{input_message}」に対する回答を生成中...")
            
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": role_prompt},
                {"role": "user", "content": input_message}
            ]
        )

        st.write("▼ 回答")
        st.success(response.choices[0].message.content)

    else:
        st.error("テキストを入力してから「実行」ボタンを押してください。")
