import streamlit as st
import random
import time

st.title("🧠 기억력 챌린지: 숫자 시퀀스")

# 숫자 개수 선택
num_digits = st.slider("숫자 개수 선택 (난이도)", 3, 7, 4)

# 시퀀스 저장
if "sequence" not in st.session_state:
    st.session_state.sequence = [random.randint(10, 99) for _ in range(num_digits)]

# 시작 버튼
if st.button("시작하기"):
    st.write("숫자들을 외우세요! (3초 후 사라집니다)")
    st.write("👉 ", "  ".join(str(n) for n in st.session_state.sequence))
    time.sleep(3)
    st.rerun()

# 사용자 입력
guess = st.text_input(f"{num_digits}개의 숫자를 순서대로 입력하세요 (예: 12 45 78 91):")

if guess:
    # 입력값을 리스트로 변환
    try:
        guess_list = list(map(int, guess.strip().split()))
        if guess_list == st.session_state.sequence:
            st.success("🎉 정답! 완벽하게 기억했어요.")
        else:
            st.error(f"❌ 틀렸어요! 정답은 {' '.join(map(str, st.session_state.sequence))}")
    except:
        st.warning("⚠️ 공백으로 숫자를 구분해서 입력해주세요.")

