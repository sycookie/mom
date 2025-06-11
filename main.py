import streamlit as st

st.title("🔮 재미있는 심리테스트 🔮")

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
    .button-row > div {
        padding: 0 10px;
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

    /* 화면 전체에 떠다니는 메롱 이모지 풍선 */
    .floating-emoji-bg {
        position: fixed;
        font-size: 30px;
        user-select: none;
        animation-name: floatUpDown;
        animation-timing-function: ease-in-out;
        animation-iteration-count: infinite;
        animation-direction: alternate;
        pointer-events: none; /* 클릭 방지 */
        z-index: 9999;
        opacity: 0.6;
    }
    @keyframes floatUpDown {
        0% {
            transform: translateY(0px);
        }
        100% {
            transform: translateY(-50px);
        }
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown('<div class="question">당신은 밥을 먹을 때 무엇부터 먹나요?</div>', unsafe_allow_html=True)
st.markdown('<div class="description">아래 버튼 중 하나를 선택해 주세요. 선택 후 다시 누르면 결과가 사라집니다.</div>', unsafe_allow_html=True)

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
        "밥": "밥부터 먹는 당신은 기본에 충실하고 안정감을 중요시하는 타입입니다.",
        "반찬": "반찬부터 먹는 당신은 변화를 즐기고 다양한 자극을 좋아하는 창의적인 성격이에요.",
        "국": "국부터 먹는 당신은 여유롭고 감성을 중시하는 따뜻한 마음의 소유자랍니다.",
    }
    st.markdown(f"""
    <div style="margin-top:30px; font-size:20px; color:#483D8B; font-style: italic; text-align:center;">
    {interpretations.get(st.session_state.selected, "")}
    </div>
    """, unsafe_allow_html=True)


# 화면 전체에 떠다니는 메롱 이모지 풍선 여러 개 추가
# 위치(x축)와 애니메이션 딜레이를 달리하여 자연스럽게

floating_emojis = """
<div style="position:fixed; top:90vh; left:5vw;" class="floating-emoji-bg" style="animation-duration:4s;">😛</div>
<div style="position:fixed; top:80vh; left:20vw; animation-duration:5s; animation-delay: 1s;" class="floating-emoji-bg">😛</div>
<div style="position:fixed; top:85vh; left:35vw; animation-duration:6s; animation-delay: 2s;" class="floating-emoji-bg">😛</div>
<div style="position:fixed; top:88vh; left:50vw; animation-duration:4.5s; animation-delay: 1.5s;" class="floating-emoji-bg">😛</div>
<div style="position:fixed; top:83vh; left:65vw; animation-duration:5.5s; animation-delay: 0.5s;" class="floating-emoji-bg">😛</div>
<div style="position:fixed; top:90vh; left:80vw; animation-duration:6s; animation-delay: 1.2s;" class="floating-emoji-bg">😛</div>
"""

st.markdown(floating_emojis, unsafe_allow_html=True)
