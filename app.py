import streamlit as st
import numpy as np
import joblib
import pandas as pd
from sklearn.preprocessing import MinMaxScaler





# ✅ MinMaxScaler 로드 (훈련 데이터 기준)
scaler_X = joblib.load("scaler_X.pkl")
scaler_y = joblib.load("scaler_y.pkl")  

# ✅ Feature 순서 (훈련 시 사용한 feature 순서)
feature_order = ['studytime', 'freetime', 'failures', 'G1', 'G2']

# ✅ 성적 예측 UI 생성
def predict_grade():
    st.subheader("📌 나의 성적을 예측해볼까요?")

    # 📌 유저 입력 받기
    studytime = st.slider("⏳ 하루 공부 시간 (시간)", min_value=1, max_value=10, step=1, value=2)
    freetime = st.slider("🎮 자유시간 (1~5)", min_value=1, max_value=5, step=1, value=3)
    failures = st.slider("❌ 실패한 과목 수", min_value=0, max_value=5, step=1, value=0)
    G1 = st.number_input("📊 과거 성적 1 (G1)", min_value=0, max_value=100, step=1, value=50)
    G2 = st.number_input("📊 과거 성적 2 (G2)", min_value=0, max_value=100, step=1, value=50)

    # ✅ 예측 실행 버튼
    if st.button("📢 결과 보기"):
        regressor=joblib.load('regressor.pkl')
        # ✅ 올바른 형식으로 입력 데이터 생성 (🔥 (1,5) 형태 유지)
        new_data = pd.DataFrame([[studytime, freetime, failures, G1, G2]], columns=feature_order)

        # ✅ MinMaxScaler 적용
        new_data_scaled = scaler_X.transform(new_data)

        # ✅ 모델 예측 실행
        predicted_grade_scaled = regressor.predict(new_data_scaled)

        # ✅ 🔹 정규화 해제 (원래 점수 범위로 변환)
        predicted_grade = scaler_y.inverse_transform(predicted_grade_scaled.reshape(-1, 1))

        # ✅ 0~100 사이 값으로 제한
        predicted_grade = np.clip(predicted_grade, 1, 100)

        # ✅ 결과 출력
        st.success(f"📢 예측된 성적 (G3): {predicted_grade[0][0]:.3f}점")

# ✅ Streamlit 실행
def main():
    st.title("당신의 성적을 예측해드립니다!")
    st.sidebar.title("메뉴")
    if st.sidebar.radio("무엇이 궁금하나요?", ["나의 성적은?"]) == "나의 성적은?":
        predict_grade()

if __name__ == "__main__":
    main()
