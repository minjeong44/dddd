import streamlit as st
import pandas as pd
import numpy as np

st.title("실시간 클릭 누적 그래프")

if "clicks" not in st.session_state:
    st.session_state.clicks = []

if st.button("한 번 눌러볼까?"):
    st.session_state.clicks.append(len(st.session_state.clicks) +1),

df = pd.DataFrame({
    "횟수": range(1, len(st.session_state.clicks) +1),
    "값": st.session_state.clicks
})

st.line_chart(df.set_index("횟수"))
