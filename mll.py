import streamlit as st
import numpy as np
import random


def run_mll():
    st.title("📚 성적 분석 및 맞춤형 공부법 추천")
    st.subheader("🔍 공부 방법을 개선하고 목표 점수를 달성하세요!")

    # ✅ 공부법 추천 함수
    

    def recommend_study_method(score):
        study_resources = {
            "10-30": [
                ("EBSi 인강", "https://www.ebsi.co.kr/"),
                ("케이무크(K-MOOC)", "https://www.kmooc.kr/"),
                ("메가스터디", "https://www.megastudy.net/"),
                ("쎈수학", "https://www.ssemath.com/"),
                ("엠베스트", "https://www.mbest.co.kr/")
            ],
            "30-50": [
                ("EBSi 인강", "https://www.ebsi.co.kr/"),
                ("이투스", "https://www.etoos.com/"),
                ("대성마이맥", "https://www.mimacstudy.com/"),
                ("수박씨닷컴", "https://www.soobakc.com/"),
                ("매스플랫(수학 전문)", "https://www.mathflat.com/")
            ],
            "50-70": [
                ("스카이에듀", "https://www.skyedu.com/"),
                ("비상에듀", "https://visang.com/"),
                ("ETOOS 인강", "https://www.etoos.com/"),
                ("스터디노트(과목별 개념 정리)", "https://www.studynote.kr/"),
                ("엠베스트(중등 전문)", "https://www.mbest.co.kr/")
            ],
            "70-90": [
                ("강남인강", "https://www.ebsi.co.kr/main/gangnam.ebs"),
                ("메가스터디 러셀", "https://www.russel.ac/"),
                ("대성마이맥", "https://www.mimacstudy.com/"),
                ("비상에듀", "https://visang.com/"),
                ("스터디노트", "https://www.studynote.kr/")
            ],
            "90-100": [
                ("EBSi 프리미엄", "https://www.ebsi.co.kr/"),
                ("이투스 프리미엄", "https://www.etoos.com/"),
                ("스카이에듀 프리미엄", "https://www.skyedu.com/"),
                ("메가스터디 러셀 최상위권", "https://www.russel.ac/"),
                ("대성마이맥 프리미엄", "https://www.mimacstudy.com/")
            ]
        }

        if 10 <= score < 30:
            level = "10-30"
            message = "📖 기초 개념부터 다시 학습, 개념 강의 & 문제 풀이 병행"
        elif 30 <= score < 50:
            level = "30-50"
            message = "📘 자주 틀리는 유형 정리, 쉬운 문제부터 반복 연습"
        elif 50 <= score < 70:
            level = "50-70"
            message = "📝 개념 복습 + 문제 풀이량 증가, 오답 분석 철저히"
        elif 70 <= score < 90:
            level = "70-90"
            message = "🔍 다양한 난이도의 문제 풀이, 시간 관리 연습"
        elif 90 <= score <= 100:
            level = "90-100"
            message = "🎉 실전 모의고사 반복, 취약한 부분 미세 조정"
        else:
            return "⚠️ 유효한 점수를 입력해주세요 (10~100)."

        # 추천 강의 3개를 랜덤으로 선택
        selected_links = random.sample(study_resources[level], 3)
        
        return f"{message}\n추천 강의:\n- {selected_links[0]}\n- {selected_links[1]}\n- {selected_links[2]}"





    # ✅ 목표 점수 달성을 위한 공부 시간 조절
    def calculate_time_adjustments(current_studytime, current_freetime, current_score, target_score=90):
        if current_score >= target_score:
            return current_studytime, current_freetime, "🎉 본인에게 맞는 공부법을 잘 활용하고 계십니다! 지속적으로 유지하세요!"

        # 목표 점수 차이 계산
        score_difference = target_score - current_score

        # 점수 증가를 위해 필요한 공부 시간 증가량 계산 (대략적인 가정)
        extra_study_hours = (score_difference / 10) * 2  # 점수 10점당 2시간 추가 공부 필요
        reduced_free_hours = extra_study_hours * 0.7  # 자유 시간은 공부 시간 증가량의 70%만큼 줄임

        # 새로운 공부 시간 및 자유 시간 계산
        new_studytime = current_studytime + extra_study_hours
        new_freetime = max(0, current_freetime - reduced_free_hours)  # 자유 시간은 0 이하로 내려가지 않도록 처리

        return round(new_studytime, 1), round(new_freetime, 1), f"🎯 장학금성적({target_score}점)에 도달하려면 공부 시간을 {round(extra_study_hours, 1)}시간 늘리고 자유 시간을 {round(reduced_free_hours, 1)}시간 줄이는 것이 좋습니다!"

    # ✅ 사용자 입력 받기
    current_studytime = st.number_input("⏳ 현재 하루 평균 공부 시간 (시간)", min_value=0, max_value=24, step=1, value=3)
    current_freetime = st.number_input("🎮 현재 하루 평균 자유 시간 (시간)", min_value=0, max_value=24, step=1, value=5)
    current_score = st.number_input("📊 현재 G3 성적 (점수)", min_value=10, max_value=100, step=1, value=50)
    
    # ✅ 목표 점수 설정 (기본값: 90점)
    target_score = 90

    # ✅ 공부 방법 추천
    study_method = recommend_study_method(current_score)

    # ✅ 공부 시간 조절 계산
    new_studytime, new_freetime, time_adjustment_message = calculate_time_adjustments(current_studytime, current_freetime, current_score, target_score)

    # ✅ 결과 출력
    st.info(f"🔎 현재 성적: {current_score}점")
    st.markdown(f'''
<div style="background-color:#dff0d8; padding:10px; border-radius:5px;">
    <h2 style="color:#155724; margin:0;">📌 공부 방법 추천:</h2>
            
    {study_method}
</div>
''', unsafe_allow_html=True)
    st.warning(time_adjustment_message)
    st.success(f"📅 조정 후 공부 시간: {new_studytime}시간, 자유 시간: {new_freetime}시간")

# ✅ Streamlit 실행

