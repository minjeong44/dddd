import streamlit as st
import random

st.title("✂️ 가위바위보 게임")

options = ["가위", "바위", "보"]

if "user_score" not in st.session_state:
    st.session_state.user_score = 0
if "comp_score" not in st.session_state:
    st.session_state.comp_score = 0

user_choice = st.selectbox("가위, 바위, 보 중 선택하세요", options)

if st.button("선택!"):
    comp_choice = random.choice(options)
    st.write(f"컴퓨터 선택: {comp_choice}")

    if user_choice == comp_choice:
        st.write("무승부!")
    elif (user_choice == "가위" and comp_choice == "보") or \
         (user_choice == "바위" and comp_choice == "가위") or \
         (user_choice == "보" and comp_choice == "바위"):
        st.write("🎉 당신이 이겼습니다!")
        st.session_state.user_score += 1
    else:
        st.write("😢 컴퓨터가 이겼습니다!")
        st.session_state.comp_score += 1

    st.write(f"현재 점수 - 당신: {st.session_state.user_score} | 컴퓨터: {st.session_state.comp_score}")

if st.button("점수 초기화"):
    st.session_state.user_score = 0
    st.session_state.comp_score = 0



