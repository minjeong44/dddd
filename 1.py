import streamlit as st
import random
import time

st.title("기억력 테스트")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(100, 999)

if st.button("시작하기"):
    st.write(f"숫자를 외우세요!: **{st.session_state.secret}**")
    time.sleep(3)
    st.experimental_rerun()

guess = st.text_input("기억나는 숫자를 입력하세요:")
if guess:
    if guess == str(st.session_state.secret):
        st.success("정답")
else:
        st.error(f"틀림 정답은 {st.session_state.secret}이다")
