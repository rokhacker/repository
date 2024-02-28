import streamlit as st
import pandas as pd

# Streamlit 앱의 제목 설정
st.title('파일 업로드 예제')

# 파일 업로드 위젯 추가
uploaded_file = st.file_uploader("파일을 업로드하세요", type=['csv'])

# 파일이 업로드 되면 내용을 읽음
if uploaded_file is not None:
    # 파일을 pandas dataframe으로 읽어들임
    df = pd.read_csv(uploaded_file)
    
    # 데이터 프레임의 내용을 화면에 출력
    st.write(df)
