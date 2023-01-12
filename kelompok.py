import streamlit as st

st.header("Kelompok 6")
st.title("DANBOX")


option = st.selectbox(
    'Pilihan Pengambilan',
    ('pick up', ' delivered'))

st.write('You selected:', option)


agree = st.checkbox('Saya setuju')

if agree:
    st.write('Terima kasih atas pesanannya!')
    
