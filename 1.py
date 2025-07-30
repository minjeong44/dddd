import streamlit as st

st.title("🎨 그라데이션 배경 만들기")

color1 = st.color_picker('시작 색상', '#ff0000')
color2 = st.color_picker('끝 색상', '#0000ff')

st.markdown(
    f"""
    <div style="width: 100%; height: 200px;
         background: linear-gradient(to right, {color1}, {color2});
         border-radius: 10px; border: 1px solid #ccc;">
    </div>
    """,
    unsafe_allow_html=True
)
