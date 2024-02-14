import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='AppleGothic')

df = pd.read_csv('pages/rnd_population.csv')

st.title("지역 별 연구개발인력 현황")

selected_regions = st.multiselect('지역 선택', options=df['region'])

data = {}
for region in selected_regions:
    data[region] = []
    for year in range(2015, 2021):
        data[region].append(int(df[df['region'] == region][str(year)].str.replace(',', '').values[0]))

plt.figure(figsize=(10, 6))  
for region, values in data.items():
    plt.plot(range(2015, 2021), values, label=region)

plt.xlabel('연도')  
plt.ylabel('인구 수')
plt.title('지역 별 연구개발인력 현황')  
plt.legend()  
st.pyplot(plt)  
