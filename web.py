import streamlit as st
import os
import numpy as np
import pandas as pd  
from keras.models import load_model  
from PIL import Image, ImageOps
import plotly.express as px  
import time

def run_web():
    st.title("📌 앱 개발 과정")
    st.divider()

    # ✅ 인공지능 성적 분석 모델 설명
    st.subheader('📌 인공지능을 활용한 성적 분석 모델')
    st.markdown('''이 프로그램은 Linear Regression과 **XGBoost Regressor(XGBRegressor)**를 학습시켜 6개월 후(G3) 성적을 예측하는 모델을 만드는 과정이다.

두 모델의 성능(R² Score)을 비교한 결과, Linear Regression이 83%의 정확도를 보여 최적 모델로 선택되었다.

📌 **문제점 및 해결 방법**
                
단순한 학습 모델에서는 성적(G1, G2)의 영향력이 너무 커서 자유 시간과 공부 시간의 중요도가 상대적으로 낮아지는 문제가 발생하였다.  
                
이를 해결하기 위해 자유 시간이 많을수록 성적 하락 패널티를 증가시켰으며, 로그 변환(log1p)을 적용하여 공부 시간이 증가할수록 성적이 점진적으로 향상되도록 보정하였다.  
이러한 과정을 통해 모델이 전체적인 학습 비율을 고르게 반영하도록 조정하였다.
''')  

    st.write('')
    st.divider()
    st.write('')

    # ✅ 배포 과정 설명
    st.subheader('📌 배포 과정')
    st.markdown('''이 프로그램은 **Streamlit을 사용하여 웹 애플리케이션 형태로 구현**하였다.  

초기에는 로컬 환경에서 개발을 진행하였으며, 이후 외부 환경에서도 실행될 수 있도록 설정하였다.  
이를 위해 **`requirements.txt` 파일을 생성하여 필요한 패키지를 명시**하였으며,  
이를 기반으로 **배포 환경에서도 동일한 설정으로 애플리케이션을 실행할 수 있도록 구성**하였다.  

이 과정을 통해 웹 애플리케이션 형태로 배포하여 사용자들이 직접 성적 예측을 할 수 있도록 구현하였다.
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
        st.markdown('''📌 **이 앱의 숨겨진 비밀: 0.6배의 마법**
        
이 앱에는 겉으로 드러나지 않는 중요한 비밀이 하나 숨겨져 있다.  
바로 **공부 시간당 성적이 0.6배씩 증가하도록 설계**된 것이다.

**🔹 왜 0.6배인가?**  
우리는 현실에서 공부한 만큼 성적이 극적으로 오르는 경우를 기대하지만,  
단기간에 성과가 보이지 않으면 쉽게 지쳐버리곤 한다.  

그러나 **0.6배 증가라는 작은 변화가 쌓이면 예상보다 훨씬 큰 차이를 만든다.**  
이는 **학습 곡선(Learning Curve)**과 **인지 부조화(Cognitive Dissonance)** 이론을 기반으로 설정되었다.  
즉, 적절한 성취감을 제공하면서도 실제 성적 향상을 유도할 수 있는 최적의 균형점이 바로 0.6배이다.

📌 **인공지능도 예측할 수 없는 미래를 위한 설계**  
공부는 단순한 숫자 게임이 아니다.  
학생 스스로가 집중하고 노력하는 순간, 모델이 예측할 수 없는 가능성이 열린다.

이 앱은 그 가능성을 **0.6배라는 숫자 안에 담았다.**  
이는 학습량과 성과 간의 간극을 조절하여, 사용자가 꾸준히 성장할 수 있도록 설계된 비밀 코드인 것이다.

결국, **0.6배의 마법**은 단순한 수치 조정이 아니라,  
학생들이 포기하지 않고 계속 도전할 수 있도록 유도하는 **숨겨진 장치**이다.  
그리고 그 작은 변화가 쌓이면, 미래는 인공지능조차 예측할 수 없는 무한한 가능성으로 열린다. 🚀
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

