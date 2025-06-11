import streamlit as st

st.title("🔮 초간단 심리테스트 🔮")

st.markdown(
    """
    <style>
    .question {
        font-size: 24px;
        font-weight: 600;
        color: #4B0082;
        margin-bottom: 20px;
    }
    .description {
        font-size: 16px;
        color: #6A5ACD;
        margin-bottom: 40px;
    }
    /* 사진 밑 둥둥 떠다니는 이모지 */
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
        color: #4B0082;
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 10px;
        margin-top: 10px;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        user-select: none;
    }

    /* 화면 아래에서 위로 올라오는 메롱 이모지 풍선 */
    .floating-emoji-bg {
        position: fixed;
        font-size: 30px;
        user-select: none;
        pointer-events: none;
        z-index: 9999;
        opacity: 0.7;
        animation-name: floatUp;
        animation-timing-function: ease-out;
        animation-iteration-count: infinite;
        animation-direction: alternate;
    }
    @keyframes floatUp {
        0% {
            transform: translateY(100vh);
            opacity: 0;
        }
        100% {
            transform: translateY(calc(100vh - 50px));
            opacity: 0.7;
        }
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="question">당신은 밥을 먹을 때 무엇부터 먹나요?</div>', unsafe_allow_html=True)
st.markdown('<div class="description">아래 버튼 중 하나를 선택해 주세요.</div>', unsafe_allow_html=True)

if 'selected' not in st.session_state:
    st.session_state.selected = None

col1, col2, col3 = st.columns(3)

def toggle_selection(choice):
    if st.session_state.selected == choice:
        st.session_state.selected = None
    else:
        st.session_state.selected = choice

with col1:
    if st.button("밥"):
        toggle_selection("밥")
with col2:
    if st.button("반찬"):
        toggle_selection("반찬")
with col3:
    if st.button("국"):
        toggle_selection("국")

if st.session_state.selected:
    st.image("cookiemerong.jpg", use_container_width=True)

    floating_emoji_html = """
    <div class="caption-text">
        엄마 메롱
        <span class="floating-emoji">😛</span>
    </div>
    """

    st.markdown(floating_emoji_html, unsafe_allow_html=True)

    interpretations = {
        "밥": "밥부터 먹는 당신은 바보입니다.",
        "반찬": "반찬부터 먹는 당신은 바보이에요.",
        "국": "국부터 먹는 당신은 바보랍니다.",
    }
    st.markdown(f"""
    <div style="margin-top:30px; font-size:20px; color:#483D8B; font-style: italic; text-align:center;">
    {interpretations.get(st.session_state.selected, "")}
    </div>
    """, unsafe_allow_html=True)

    # 버튼 눌렸을 때만 화면 전체에 떠다니는 메롱 이모지 풍선 보여주기
    floating_emojis = f"""
    <div style="left:5vw; animation-duration:4s; top:100vh;" class="floating-emoji-bg">😛</div>
    <div style="left:20vw; animation-duration:5s; animation-delay: 1s; top:100vh;" class="floating-emoji-bg">😛</div>
    <div style="left:35vw; animation-duration:6s; animation-delay: 2s; top:100vh;" class="floating-emoji-bg">😛</div>
    <div style="left:50vw; animation-duration:4.5s; animation-delay: 1.5s; top:100vh;" class="floating-emoji-bg">😛</div>
    <div style="left:65vw; animation-duration:5.5s; animation-delay: 0.5s; top:100vh;" class="floating-emoji-bg">😛</div>
    <div style="left:80vw; animation-duration:6s; animation-delay: 1.2s; top:100vh;" class="floating-emoji-bg">😛</div>
    """
    st.markdown(floating_emojis, unsafe_allow_html=True)
