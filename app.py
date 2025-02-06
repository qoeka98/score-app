import streamlit as st
import numpy as np
import joblib
import pandas as pd
import datetime
from sklearn.preprocessing import StandardScaler

from eda import run_eda
from home import run_home
from ml import run_ml  
from mll import run_mll
from web import run_web

# ✅ Streamlit 실행
def main():
    # ✅ 사이드바 스타일 적용
    st.sidebar.markdown(
        """
        <style>
            .sidebar-title {
                font-size: 26px;
                font-weight: bold;
                text-align: center;
                color: #333;
                background-color: #D4EDDA; /* 💚 파스텔 연두색 */
                padding: 12px;
                border-radius: 10px;
                margin-bottom: 10px;
            }
            .sidebar-container {
                background-color: #F9F9F9;
                padding: 15px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
                margin-bottom: 15px;
            }
            .sidebar-footer {
                font-size: 14px;
                text-align: center;
                color: #555;
                margin-top: 20px;
                padding: 10px;
                background-color: #F1F1F1;
                border-radius: 10px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # ✅ 사이드바 제목 및 이미지 추가
    st.sidebar.markdown('<p class="sidebar-title">📌 탐색 메뉴</p>', unsafe_allow_html=True)
    st.sidebar.image('image/사이드바용.png', use_container_width=True)

    # ✅ 사이드바 메뉴 (빨간 상자 부분 제거, 기존 배치로 변경)
    menu = st.sidebar.radio(
        "📂 메뉴 선택",
        [
            "🏠 홈",
            "🔍 6개월뒤 성적으로 장학금을 받을 수 있을까?",
            "⚖️ 공부 시간 vs 자유 시간 영향 분석",
            "📚 성적 분석 및 맞춤형 공부법 추천",
            "🚀 앱개발과정"
        ]
    )

    # ✅ 사이드바 푸터 추가
    st.sidebar.markdown('<p class="sidebar-footer">© 개발자 이메일 : vhzkflfltm6@gmail.com</p>', unsafe_allow_html=True)

    # ✅ 선택된 메뉴 실행
    if menu == "🏠 홈":
        run_home()
    elif menu == "🔍 6개월뒤 성적으로 장학금을 받을 수 있을까?":
        run_eda()
    elif menu == "⚖️ 공부 시간 vs 자유 시간 영향 분석":
        run_ml()
    elif menu == "📚 성적 분석 및 맞춤형 공부법 추천":
        run_mll()
    elif menu == "🚀 앱개발과정":
        run_web()

# ✅ Streamlit 애플리케이션 실행
if __name__ == "__main__":
    main()
