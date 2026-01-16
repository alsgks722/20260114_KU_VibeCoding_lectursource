import streamlit as st

st.set_page_config(page_title="BMI 계산기", page_icon="⚖️", layout="centered")

# 전체 스타일 커스터마이징 (버튼 + 입력창)
st.markdown("""
    <style>
    /* 빨간색 버튼 */
    div.stButton > button:first-child {
        background-color: #ff4d4d;
        color: white;
    }
    div.stButton > button:first-child:hover {
        background-color: #e60000;
        color: white;
    }
""", unsafe_allow_html=True)

st.title("BMI 계산기")

st.write("키(cm)와 몸무게(kg)를 입력한 후 **BMI 계산하기** 버튼을 눌러 주세요.")

# 숫자 입력 (세로 배치)
height = st.number_input(
    "키 (cm)",
    min_value=100.0,
    max_value=250.0,
    value=170.0,
    step=0.1
)

weight = st.number_input(
    "몸무게 (kg)",
    min_value=20.0,
    max_value=200.0,
    value=65.0,
    step=0.1
)

# 계산 버튼
if st.button("BMI 계산하기"):
    if height <= 0:
        st.error("키는 0보다 커야 합니다.")
    else:
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        if bmi < 18.5:
            status = "저체중"
        elif 18.5 <= bmi <= 22.9:
            status = "정상"
        elif 23 <= bmi <= 24.9:
            status = "과체중"
        else:
            status = "비만"

        st.subheader("결과")
        st.write(f"**BMI:** {bmi:.2f}")
        st.write(f"**판정:** {status}")
else:
    st.info("키와 몸무게를 입력한 뒤 **BMI 계산하기** 버튼을 눌러 BMI를 확인하세요.")


# ============================================
# 실습 과제
# ============================================
st.divider()
st.header("📝 실습 과제")

st.markdown("""
### 과제 1: 회원가입 폼 만들기

다음 정보를 입력받는 회원가입 폼을 만들어보세요:
- 이름 (텍스트 입력)
- 이메일 (텍스트 입력, type="default")
- 비밀번호 (텍스트 입력, type="password")
- 생년월일 (날짜 선택)
- 성별 (라디오 버튼)
- 관심사 (다중 선택)
- 마케팅 수신 동의 (체크박스)
- 가입하기 버튼

버튼을 누르면 입력한 정보를 요약해서 보여주세요!

### 과제 2: BMI 계산기

- 키 입력 (숫자 또는 슬라이더, 단위: cm)
- 몸무게 입력 (숫자 또는 슬라이더, 단위: kg)
- 계산하기 버튼
- (BMI = 체중(kg) / (신장(m) * 신장(m)))
- BMI 결과 및 판정 표시
  - 저체중 (< 18.5)
  - 정상 (18.5 ~ 22.9)
  - 과체중 (23 ~ 24.9)
  - 비만 (≥ 25)
""")

# 예시 답안
with st.expander("💡 과제 1 예시 답안"):
    st.subheader("회원가입")
    
    with st.form("signup_form"):
        form_name = st.text_input("이름*")
        form_email = st.text_input("이메일*")
        form_password = st.text_input("비밀번호*", type="password")
        form_birth = st.date_input("생년월일*")
        form_gender = st.radio("성별*", ["남성", "여성", "기타"], horizontal=True)
        form_interests = st.multiselect(
            "관심사",
            ["스포츠", "음악", "영화", "독서", "게임", "요리"]
        )
        form_marketing = st.checkbox("마케팅 수신 동의")
        
        submitted = st.form_submit_button("가입하기", type="primary")
        
        if submitted:
            if form_name and form_email and form_password:
                st.success("✅ 회원가입이 완료되었습니다!")
                st.write("### 가입 정보")
                st.write(f"- 이름: {form_name}")
                st.write(f"- 이메일: {form_email}")
                st.write(f"- 생년월일: {form_birth}")
                st.write(f"- 성별: {form_gender}")
                st.write(f"- 관심사: {', '.join(form_interests) if form_interests else '없음'}")
                st.write(f"- 마케팅 수신: {'동의' if form_marketing else '미동의'}")
            else:
                st.error("❌ 필수 항목을 모두 입력해주세요!")

with st.expander("💡 과제 2 예시 답안"):
    st.subheader("BMI 계산기")
    
    bmi_height = st.number_input("키 (cm):", min_value=100.0, max_value=250.0, value=170.0, step=0.1)
    bmi_weight = st.number_input("몸무게 (kg):", min_value=30.0, max_value=200.0, value=65.0, step=0.1)
    
    if st.button("BMI 계산하기", type="primary"):
        # BMI = 체중(kg) / (신장(m) * 신장(m))
        height_m = bmi_height / 100
        bmi = bmi_weight / (height_m ** 2)
        
        st.metric("BMI", f"{bmi:.1f}")
        
        if bmi < 18.5:
            st.info("📊 판정: 저체중")
        elif bmi < 23:
            st.success("📊 판정: 정상")
        elif bmi < 25:
            st.warning("📊 판정: 과체중")
        else:
            st.error("📊 판정: 비만")
