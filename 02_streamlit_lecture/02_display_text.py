import streamlit as st

# ============================================
# 과제: 뉴스 기사 만들기 (최종 답안만)
# ============================================

st.title("🏫 대학생 최민한, AI와 운동을 결합한 다이어트 프로젝트 화제")
st.caption("작성자: 최민한 | 2026-01-16")

st.image(
    "https://images.pexels.com/photos/841130/pexels-photo-841130.jpeg",
    caption="AI와 함께 운동 데이터를 분석하는 대학생",
    use_container_width=True,
)

st.markdown("""
서울의 한 대학교에서 **운동과 다이어트**, 그리고 **인공지능(AI)** 을 결합한  
새로운 프로젝트가 학생들 사이에서 큰 관심을 받고 있습니다.

이 프로젝트는 대학생 **최민한** 씨가 주도하고 있으며,  
학생들의 운동 기록과 식단 데이터를 Streamlit 앱으로 시각화하여  
다이어트 진행 상황을 한눈에 볼 수 있도록 하는 것이 특징입니다.

전문가들은 *"데이터 기반 생활 관리가 MZ세대의 새로운 건강 트렌드가 될 것"* 이라고 전망하고 있습니다.
""")

st.info("""
💡 관련 정보  
- 프로젝트 이름: *AI 피트니스 다이어리*  
- 사용 기술: Python, Streamlit, Pandas  
- 주요 기능: 운동 기록 시각화, 하루 섭취 칼로리 체크, 주간 변화 추이 그래프
""")

st.code("""
# 간단한 운동 기록 예시 데이터 (딕셔너리 형태)
workout_data = {
    "date": ["2026-01-10", "2026-01-11", "2026-01-12"],
    "exercise": ["웨이트 트레이닝", "런닝", "수영"],
    "duration_min": [60, 45, 50],
    "kcal_burned": [450, 380, 420],
}

# 추후에 pandas DataFrame으로 만들어서 시각화 가능
# import pandas as pd
# df = pd.DataFrame(workout_data)
# st.dataframe(df)
""", language="python")
