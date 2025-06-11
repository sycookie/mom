import streamlit as st

st.title("재미있는 심리테스트")

st.write("당신은 밥을 먹을 때 무엇부터 먹나요?")

col1, col2, col3 = st.columns(3)
show_image = False

with col1:
    if st.button("밥"):
        show_image = True
with col2:
    if st.button("반찬"):
        show_image = True
with col3:
    if st.button("국"):
        show_image = True

if show_image:
    st.image("cookiemerong.jpg", use_container_width=True)
    
    # 엄마 메롱 텍스트 + 둥둥 떠다니는 이모지 CSS 애니메이션
    floating_emoji_html = """
    <style>
    .floating-emoji {
        position: relative;
        display: inline-block;
        font-size: 40px;
        animation: float 3s ease-in-out infinite;
        margin-left: 10px;
    }
    @keyframes float {
        0% { transform: translateY(0); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0); }
    }
    .caption-text {
        font-size: 48px;
        font-weight: bold;
        text-align: center;
        color: black;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin-top: 10px;
    }
    </style>
    <div class="caption-text">
        엄마 메롱
        <span class="floating-emoji">😛</span>
    </div>
    """
    
    st.markdown(floating_emoji_html, unsafe_allow_html=True)
