import streamlit as st

st.title("버튼을 눌러 고양이 사진을 확인하세요! 🐱")

# 버튼 만들기
col1, col2, col3, col4 = st.columns(4)
show_image = False

with col1:
    if st.button("A"):
        show_image = True
with col2:
    if st.button("B"):
        show_image = True
with col3:
    if st.button("C"):
        show_image = True
with col4:
    if st.button("D"):
        show_image = True

# 버튼 중 하나라도 눌리면 사진 보여주기
if show_image:
    st.image("cookiemerong.jpg", use_container_width=True)
    st.markdown("<h1 style='text-align: center; color: black;'>엄마 메롱 😛</h1>", unsafe_allow_html=True)
