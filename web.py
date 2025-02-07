import streamlit as st
import os
import numpy as np
import pandas as pd  
from keras.models import load_model  
from PIL import Image, ImageOps
import plotly.express as px  
import time

def run_web():
    st.title("🎯 인공지능을 활용한 성적 분석 및 예측 시스템")


    st.divider()

    # ✅ 인공지능 성적 분석 모델 설명
    st.subheader('📌 인공지능을 활용한 성적 분석 모델')
    st.markdown('''이 프로젝트는 Linear Regression과 **XGBoost Regressor(XGBRegressor)**를 학습시켜 6개월 후(G3) 성적을 예측하는 모델을 구축하는 과정입니다.

🔹 모델 성능 비교두 모델의 성능(R² Score)을 평가한 결과, Linear Regression이 83%의 정확도를 기록하여 최적 모델로 선정되었습니다.
''')  

    st.write('')
    st.divider()
    st.write('')

    st.subheader('🏗 개발 과정')
    st.markdown('''🔹 1. 문제점 및 해결 방법

단순한 학습 모델에서는 이전 성적(G1, G2)의 영향력이 너무 커서, 자유 시간과 공부 시간의 중요도가 낮아지는 문제가 발생하였습니다.

✅ 해결 방법

자유 시간이 많을수록 성적 하락 패널티 증가

로그 변환(log1p) 적용 → 공부 시간이 증가할수록 성적이 점진적으로 향상되도록 보정

학습 비율을 고르게 반영하여 모델 조정

📌 이를 통해 보다 현실적인 성적 예측이 가능하도록 모델을 최적화하였습니다.
''')  




    st.write('')
    st.divider()
    st.write('')

    # ✅ 배포 과정 설명
    st.subheader('📌 배포 과정')
    st.markdown('''🔹 2. Streamlit을 활용한 웹 애플리케이션 구현

이 프로그램은 Streamlit을 사용하여 웹 애플리케이션 형태로 배포되었습니다.

📌 배포 과정
                1️⃣ 초기에는 로컬 환경에서 개발 진행
                2️⃣ 외부에서도 실행 가능하도록 requirements.txt 파일 생성하여 패키지 의존성 명시
                3️⃣ 배포 환경에서 동일한 설정으로 애플리케이션 실행 가능하도록 구성
                4️⃣ 사용자가 직접 성적 예측을 할 수 있도록 웹 애플리케이션 형태로 배포 완료 ✅
''')
    
    st.write('')
    st.divider()
    st.write('')

    st.subheader('📌 이 앱의 비밀')
    # ✅ 버튼을 활용한 비밀 보기 (토글 기능)
    if "show_secret" not in st.session_state:
        st.session_state["show_secret"] = False  # ✅ 기본값: 아니오 (비밀 숨김)
        

    if st.button("📢 비밀 확인하기"):
        st.session_state["show_secret"] = not st.session_state["show_secret"]  # ✅ 버튼 클릭 시 True/False 변경

   
  

    # ✅ "예" 상태일 때 비밀 표시
    if st.session_state["show_secret"]:
        st.subheader('📌 이 앱의 숨겨진 비밀')
        st.markdown('''🧙 이 앱의 숨겨진 비밀: 0.6배의 마법
 이 앱에는 단순한 성적 예측을 넘어선 중요한 비밀이 숨겨져 있습니다.

🔹 3. 왜 0.6배인가?

현실에서 공부한 만큼 즉각적인 성과가 나타나지 않으면 쉽게 지쳐버리는 경우가 많습니다. 하지만 0.6배 증가라는 작은 변화가 지속적으로 누적되면 예상보다 훨씬 큰 차이를 만들어 냅니다.

💡 기반 이론✔ 학습 곡선(Learning Curve): 학습의 진척이 점진적으로 이루어지는 패턴✔ 인지 부조화(Cognitive Dissonance): 적절한 성취감을 제공하여 지속적인 동기 부여

📌 결과적절한 성취감을 유지하면서도 실제 성적 향상을 유도하는 최적의 균형점이 바로 0.6배 증가입니다.
''')
        st.write('')
        st.divider()
        st.write('')

        st.subheader('🔮 인공지능도 예측할 수 없는 미래를 위한 설계')

        st.markdown('''

공부는 단순한 숫자 게임이 아닙니다.💡 집중하고 노력하는 순간, 모델이 예측할 수 없는 가능성이 열립니다.

이 앱은 그 가능성을 0.6배라는 숫자 안에 담았습니다.이는 학습량과 성과 간의 간극을 조절하여, 사용자가 꾸준히 성장할 수 있도록 설계된 비밀 코드입니다.

🚀 결론


                    ✅ 0.6배의 마법은 단순한 수치 조정이 아니라,
        ✅ 학생들이 포기하지 않고 계속 도전할 수 있도록 유도하는 숨겨진 장치입니다.
        ✅ 그리고 그 작은 변화가 쌓이면, 미래는 인공지능조차 예측할 수 없는 무한한 가능성으로 열릴 것입니다. 🌟
''')


        
    
        


    st.write('')
    st.divider()
    st.write('')

    # ✅ 정보 출처 표시
    st.markdown('''📌 **정보 출처**  
https://www.kaggle.com/
''')

    st.write('')
    st.divider()
    st.write('')

    # ✅ 개발자 깃허브 링크
    st.subheader('📌 개발자 깃허브')
    st.markdown('[🔗 GitHub Repository](https://github.com/qoeka98/score-app)')

