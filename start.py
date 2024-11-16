import streamlit as st
import math

st.title('두 수의 합 계산기')

a = st.number_input('첫번째 숫자를 입력하세요:', value=0.0)
b = st.number_input('두번째 숫자를 입력하세요:', value=0.0)

if st.button('계산하기'):
    result = a + b
    st.write(f'두 수의 합: {result}')
    
    if b != 0:
        division = round(a / b, 3)
        st.write(f'a/b의 결과: {division}')
    else:
        st.write('0으로 나눌 수 없습니다.')
    
    if a >= 0:
        sqrt_a = round(math.sqrt(a), 3)
        st.write(f'첫번째 숫자의 제곱근: {sqrt_a}')
    else:
        st.write('첫번째 숫자가 음수이므로 제곱근을 구할 수 없습니다.')
