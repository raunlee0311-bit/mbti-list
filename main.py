import streamlit as st

st.set_page_config(
    page_title="MBTI 성격 유형",
    page_icon="🧠",
    layout="wide"
)

st.title("🧠 MBTI 성격 유형 소개 사이트")

st.write("""
MBTI는 사람의 성향을 16가지 유형으로 나누어 이해하는 성격 유형 검사입니다.

왼쪽 사이드바에서 원하는 MBTI 유형을 선택하면
각 유형의 특징, 장점, 어울리는 직업을 확인할 수 있습니다.
""")

st.divider()

st.header("📌 MBTI 4가지 기준")

col1, col2 = st.columns(2)

with col1:
    st.info("""
**E / I**

E : 외향형  
I : 내향형

**S / N**

S : 현실적 정보  
N : 직관적 정보
""")

with col2:
    st.success("""
**T / F**

T : 사고 중심  
F : 감정 중심

**J / P**

J : 계획형  
P : 즉흥형
""")

st.warning("MBTI는 성격을 이해하는 참고 자료이며, 사람을 완전히 판단하는 기준은 아닙니다.")
