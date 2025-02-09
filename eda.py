import streamlit as st
import numpy as np
import joblib
import pandas as pd
import datetime
from sklearn.preprocessing import StandardScaler

def run_eda():
    # ✅ 모델 및 스케일러 로드
    scaler_X = joblib.load("scaler_X.pkl")  # G3 예측용 스케일러
    best_model = joblib.load("best_model.pkl")  # 최적 G3 예측 모델
    scholarship_model = joblib.load("scholarship_model.pkl")  # 장학금 예측 모델
    scholarship_scaler = joblib.load("scholarship_scaler.pkl")  # 장학금 예측용 스케일러

    # ✅ **G3 점수 예측 함수**
    def predict_g3(G1, G2, studytime_per_week, freetime_per_week, start_date):
        G_avg = G1 + G2
        G_ratio = G1 / (G2 + 1)

        # ✅ 6개월 후 날짜 계산
        end_date = start_date + datetime.timedelta(weeks=26)

        # ✅ 실제 날짜 차이 계산 (단위: 주)
        weeks_diff = (end_date - start_date).days // 7  

        # ✅ 6개월 동안 누적된 학습/자유 시간 계산
        studytime_total = studytime_per_week * weeks_diff
        freetime_total = freetime_per_week * weeks_diff
        total_hours = studytime_total + freetime_total

        # ✅ 공부 시간당 성적 0.6배 증가 적용
        studytime_boost = studytime_total * 0.6  

        # ✅ 자유 시간 패널티 적용 (완화)
        freetime_penalty = np.sqrt(freetime_total) * 1.5  

        # ✅ 학습 시간 비율 계산 (꾸준히 증가)
        studytime_ratio = (studytime_total / (total_hours + 1)) ** 1.3  

        # ✅ 입력 데이터 DataFrame 생성
        new_data = pd.DataFrame([[studytime_total, freetime_total, G_avg, G_ratio, total_hours, 
                                  studytime_boost, freetime_penalty, studytime_ratio]], 
                                columns=scaler_X.feature_names_in_)

        # ✅ StandardScaler 적용
        new_data_scaled = scaler_X.transform(new_data)

        # ✅ 예측 실행 (🔥 6개월 후 G3 직접 예측)
        predicted_g3 = best_model.predict(new_data_scaled).item()

        return np.round(predicted_g3, 2), end_date

    # ✅ **장학금 가능 여부 예측 함수**
    def check_scholarship_eligibility(predicted_g3):
        # ✅ 입력 데이터를 DataFrame으로 변환
        student_data = pd.DataFrame([[predicted_g3]], columns=['G3'])

        # ✅ 데이터 정규화
        student_scaled = scholarship_scaler.transform(student_data)

        # ✅ 장학금 가능 여부 예측
        scholarship_prediction = scholarship_model.predict(student_scaled)[0]
        scholarship_probability = scholarship_model.predict_proba(student_scaled)[0][1]

        if predicted_g3 >= 90:  # ✅ 장학금 기준 (G3 ≥ 90 필요)
            return f"🎓 장학금을 받을 수 있습니다!", 0, 0

        # ✅ 부족한 점수 계산
        required_G3 = 90
        improvement_needed = max(0, required_G3 - predicted_g3)
        improvement_percentage = (improvement_needed / predicted_g3) * 100 if improvement_needed > 0 else 0

        return (f"❌ 장학금을 받을 수 없습니다.",
                improvement_needed, improvement_percentage)

    # ✅ **Streamlit UI에서 입력된 값을 사용하여 예측**
    def predict_grade():
        st.subheader("📌 6개월 후 나의 성적과 장학금 가능성을 예측해볼까요?")

        # 📌 유저 입력 받기
        start_date = st.date_input("📅 현재 날짜를 선택하세요", datetime.date.today())
        studytime = st.number_input("⏳ 일주일 평균 공부 시간 (시간)", min_value=0, max_value=24, step=1, value=10)
        freetime = st.number_input("🎮 일주일 평균 자유 시간 (시간)", min_value=0, max_value=24, step=1, value=14)
        G1 = st.number_input("📊 중간고사 성적 (G1)", min_value=0, max_value=100, step=1, value=50)
        G2 = st.number_input("📊 기말고사 성적 (G2)", min_value=0, max_value=100, step=1, value=50)

        # ✅ 모델 예측 실행
        predicted_g3, end_date = predict_g3(G1, G2, studytime, freetime, start_date)

        # ✅ 장학금 가능 여부 확인
        scholarship_result, needed_points, needed_percentage = check_scholarship_eligibility(predicted_g3)

        # ✅ 결과 출력
        st.success(f"📅 6개월 후 날짜: **{end_date.strftime('%Y-%m-%d')}**")
        st.success(f"📢 6개월 후 예상 성적 (G3): 🎯 **{predicted_g3:.2f}점**")

        # ✅ 장학금 가능 여부 출력
        if needed_points == 0:
            st.success(scholarship_result)
        else:
            st.warning(scholarship_result)
            st.info(f"🔺 점수를 최소 {needed_points:.2f}점 올려야 장학금을 받을 수 있습니다.")

    # ✅ 실행 시 바로 `predict_grade()` 호출하여 메뉴 없이 자동 실행
    predict_grade()

# ✅ Streamlit 애플리케이션 실행 (🚀 메뉴 없이 바로 실행)
if __name__ == "__main__":
    run_eda()
