import streamlit as st
import random
import time

st.title("🧠 기억력 챌린지: 숫자 시퀀스")

# 난이도 조절용 슬라이더
num_digits = st.slider("숫자 개수 선택 (난이도)", 3, 7, 4)

# 시작 버튼 누르면 새로운 숫자 시퀀스를 생성
if st.button("시작하기"):
    st.session_state.sequence = [random.randint(10, 99) for _ in range(num_digits)]
    st.session_state.show_sequence = True
    st.rerun()

# 숫자 시퀀스 보여주기 (3초간)
if st.session_state.get("show_sequence", False):
    st.write("숫자들을 외우세요! (3초 후 사라집니다)")
    st.write("👉", "  ".join(str(n) for n in st.session_state.sequence))
    time.sleep(3)
    st.session_state.show_sequence = False
    st.rerun()

# 사용자 입력받기
guess = st.text_input(f"{num_digits}개의 숫자를 순서대로 입력하세요 (예: 12 45 78 91):")

# 정답 체크
if guess and "sequence" in st.session_state:
    try:
        guess_list = list(map(int, guess.strip().split()))
        correct = st.session_state.sequence
        if guess_list == correct:
            st.success("🎉 정답! 완벽하게 기억했어요.")
        else:
            st.error(f"❌ 틀렸어요! 정답은 {' '.join(map(str, correct))}")
    except:
        st.warning("⚠️ 공백으로 숫자를 구분해서 입력해주세요.")


