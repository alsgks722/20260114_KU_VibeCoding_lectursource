"""
1단계: Streamlit 소개 및 첫 번째 앱
학습 목표: Streamlit의 기본 구조 이해하기
"""

import streamlit as st

# 브라우저창 탭 아이콘과 페이지 타이틀 설정
st.set_page_config(
    page_title="스트림릿과의 만남",
    page_icon="🎨",
    layout="wide"  # "centered" 또는 "wide"
)

# 1. 제목을 자신의 이름으로 변경
st.title("🎉 최민한")

# 간단한 텍스트 출력
st.write("안녕하세요! Streamlit에 오신 것을 환영합니다.")

# 구분선
st.divider()

# 2. 자기소개 내용을 본인의 정보로 수정
st.header("자기소개")
st.write("이름: 최민한")
st.write("직업: 대학생")
st.write("관심사: 운동, 다이어트")

# 구분선
st.divider()

# 기존 버튼
st.subheader("버튼을 눌러보세요!")
if st.button("인사하기"):
    st.balloons()
    st.success("반갑습니다! 🎊")

# 3. 새로운 버튼 추가 + 다른 메시지 출력
st.subheader("새로운 버튼")
if st.button("오늘의 다짐 보기"):
    st.info("오늘도 운동과 식단 관리로 한 걸음 더 나아가요! 💪")

# 4. st.warning() 또는 st.error() 사용 예시
st.warning("주의: 운동할 때 무리하지 말고, 본인 컨디션에 맞춰서 하세요!")

# 정보 박스
st.info("💡 팁: 코드를 수정하고 저장하면 자동으로 새로고침됩니다!")

# ============================================
# 실습 과제 (원래대로)
# ============================================
st.divider()
st.header("📝 실습 과제")
st.markdown("""
1. 제목을 자신의 이름으로 변경해보세요
2. 자기소개 내용을 본인의 정보로 바꿔보세요
3. 새로운 버튼을 추가하고, 클릭 시 다른 메시지가 나오도록 해보세요
4. `st.warning()` 또는 `st.error()` 함수를 사용해보세요
""")
