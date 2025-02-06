import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import platform
from matplotlib import font_manager, rc

# ✅ 운영체제(OS)별 한글 폰트 설정
def set_korean_font():
    plt.rcParams["axes.unicode_minus"] = False  # ✅ 마이너스(-) 깨짐 방지

    if platform.system() == "Windows":
        rc("font", family="Malgun Gothic")  # ✅ 윈도우 환경 (맑은 고딕)
    elif platform.system() == "Linux":
        rc("font", family="NanumGothic")  # ✅ 리눅스 환경 (나눔 고딕)
    else:
        rc("font", family="DejaVu Sans")  # ✅ 기본 폰트 (맥OS 등)

set_korean_font()  # ✅ 폰트 설정 적용

def run_ml():
    """Streamlit을 사용하여 공부 시간과 자유 시간이 성적에 미치는 영향 분석"""

    def predict_score(study_time, free_time):
        """공부시간과 자유시간을 입력받아 예상 성적을 계산하는 함수"""
        if study_time + free_time == 0:
            return 10  # 최소 점수 설정
        
        study_ratio = study_time / (study_time + free_time + 1)  # +1로 0분모 방지
        predicted_score = 10 + 90 * study_ratio  # 공부시간 비례 증가 (단순 모델)
        return min(predicted_score, 100)  # 최대 100점 제한

    def show_comparison_plot(study_time, free_time, actual_score):
        """사용자 입력 성적과 예상 성적을 비교하는 플롯 차트"""
        # ✅ x축: 공부시간, y축: 성적
        study_hours = np.linspace(1, 10, 10)
        predicted_scores = [predict_score(s, free_time) for s in study_hours]

        fig, ax = plt.subplots(figsize=(8, 5))
        ax.plot(study_hours, predicted_scores, label="예상 성적", marker="o", linestyle="--", color="blue")
        ax.scatter(study_time, actual_score, color="red", label="사용자 입력 성적", s=100, edgecolors="black")

        ax.set_xlabel(" 공부 시간 (시간)")
        ax.set_ylabel(" 예상 성적")
        ax.set_title(" 공부시간 vs. 성적 (예측값 vs. 입력값 비교)")
        ax.legend()
        ax.grid(True)

        st.pyplot(fig)

    # ✅ Streamlit UI 설정 (바로 실행되도록 설정)
    st.title("📚 공부시간 & 자유시간 vs. 성적 분석")

    study_time = st.number_input("📚 하루 공부 시간 (시간)", min_value=1.0, max_value=10.0, value=5.0)
    free_time = st.number_input("🎮 하루 자유 시간 (시간)", min_value=1.0, max_value=10.0, value=3.0)
    actual_score = st.number_input("🎯 실제 성적 (사용자 입력값)", min_value=0.0, max_value=100.0, value=50.0)

    # ✅ 버튼 없이 자동 실행
    st.write("### 📊 공부시간 vs. 성적 비교 차트")
    show_comparison_plot(study_time, free_time, actual_score)

# ✅ Streamlit에서 실행
if __name__ == "__main__":
    run_ml()
