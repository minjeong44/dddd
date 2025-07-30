import streamlit as st
import random
import time

st.title("🧠 기억력 테스트")

# 처음 실행될 때 비밀 숫자 설정
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(100, 999)

# 시작 버튼을 누르면 숫자 보여주고 3초 후 리렌더링
if st.button("시작하기"):
    st.write(f"숫자를 외우세요!: **{st.session_state.secret}**")
    time.sleep(3)
    st.rerun()

# 숫자 입력 받고 정답 확인
guess = st.text_input("기억나는 숫자를 입력하세요:")
if guess:
    if guess == str(st.session_state.secret):
        st.success("정답! 🎉 잘 기억했어요.")
    else:
        st.error(f"❌ 틀림! 정답은 {st.session_state.secret}입니다.")
