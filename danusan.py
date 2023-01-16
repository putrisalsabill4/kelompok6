import streamlit as st
st.sidebar.header("Kolom Pencarian")
text=st.sidebar.text_area("Cari produk di sini")
button1=st.sidebar.button("Masukkan")
if button1:
    st.write(text) 
    clean=clean_text(text)
    st.write(clean)
st.header("Kelompok 6")
st.title("DANBOX")
 
    
option = st.selectbox(
    'Pilihan Pengambilan',
    ('pick up', ' delivered'))
st.write('You selected:', option)

    
import streamlit as st
name = st.text_input('Nama Pelanggan')
if not name:
    st.warning('Please input a name.')
name = st.text_input('Kelas')
if not name:
    st.warning('Please input a class.')
import datetime
import streamlit as st
d = st.date_input(
    " Tanggal Pemesanan",
    datetime.date(2019, 7, 6))
import datetime
import streamlit as st
t = st.time_input('Waktu Pemesanan', datetime.time(8, 45))

import streamlit as st
st.subheader('Menu Makanan')
from PIL import Image
import streamlit as st

col1, col2, col3=st.columns(3)
with col1:
    st.subheader('risol mayo')
    st.image('don.jpg',width=150)
    number1 = st.number_input('Jumlah Risol',0)
with col2:
    st.subheader('risol mayo')
    st.image('sang.jpg',width=150)
    number2 = st.number_input('Jumlah asfa',0)
with col3:
    st.subheader('risol mayo')
    st.image('sss.jpg',width=150)
    number3 = st.number_input('Jumlah afaetf',0)
col4, col5, col6=st.columns(3)
with col4:
    st.subheader('risol mayo')
    st.image('sus.jpg',width=150)
    number4 = st.number_input('Jumlah Riarvwsol',0)
with col5:
    st.subheader('risol mayo')
    st.image('coba.jpg',width=150)
    number5 = st.number_input('Jumlah erc',0)
with col6:
    st.subheader('risol mayo')
    st.image('bom.jpg',width=150)
    number5 = st.number_input('Jumlah sdq',0)
Total=st.button ("Rincian")
lah=number1+number2+number3+number4+number5
while lah>0:
    import pandas as pd
    harga1=2000*number1
    harga2=3000*number2
    harga3=2000*number3
    harga4=2000*number4
    harga5=2000*number5
    data = [['Risol',number1,harga1],['Keu Sus',number2,harga2],['Pisang Roll',number3,harga3],['Martabak Telor',number4,harga4],['Pastel',number5,harga5]]
    df=pd.DataFrame(data,columns=['Makanan','jumlah','harga (Rp.)'])
    df
    break
else:
    lah<0.01
    st.warning('Tidak ada pesanan')

harga1=2000
harga2=3000
harga3=2000
harga4=2000
harga5=2000
hitung1=(harga1*number1)+(harga2*number2)+(harga3*number3)+(harga4*number4)+(harga5*number5)
if hitung1<20000:
        st.write("total harga makanan Rp.",hitung1)
if hitung1>20000:
    hitung1=hitung1-0.1*hitung1
    st.write("Diskon 10% total harga makanan Rp.",hitung1)

import streamlit as st
st.subheader('Perlengkapan Laboratorium')
from PIL import Image
import streamlit as st

col7, col8, col9=st.columns(3)
with col7:
    st.header("Sarung Tangan")
    image = Image.open('sarung.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberA = st.number_input('Jumlah sarung tangan',0)
    

with col8:
    st.header("Serbet")
    image = Image.open('serbet.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberB = st.number_input('Jumlah serbet',0)
    
with col9:
    st.header("Tabung Reaksi")
    image = Image.open('tr.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberC = st.number_input('Jumlah tabung reaksi',0)
    
col10, col11, col12=st.columns(3)
with col10:
    st.header("Gelas Piala")
    image = Image.open('piala.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberD = st.number_input('Jumlah Gelas Piala',0)    
    
with col11:
    st.header("Tabung Ulir")
    image = Image.open('lir.jpg')
    st.image(image, width=150)
    import streamlit as st
    numberE = st.number_input('Jumlah tabung ulir',0)
    
lab = st.button("rincian")
jml=numberA+numberB+numberC+numberD+numberE
while jml>0:
    import pandas as pd
    hargaA=2000*numberA
    hargaB=5000*numberB
    hargaC=10000*numberC
    hargaD=20000*numberD
    hargaE=20000*numberE
    data = [['Sarung Tangan',numberA,hargaA],['Serbet',numberB,hargaB],['Tabung Reaksi',numberC,hargaC],['Gelas Piala',numberD,hargaD],['Tabung Ulir',numberE,hargaE]]
    df=pd.DataFrame(data,columns=['Perlengkapan','jumlah','harga (Rp.)'])
    df
    break
    import streamlit as st
else:
    jml<0.1
    st.warning('Tidak ada pesanan')
    
   
    hargaA=2
hargaB=5000
hargaC=10000
hargaD=20000
hargaE=20000
hitung=(hargaA*numberA)+(hargaB*numberB)+(hargaC*numberC)+(hargaD*numberD)+(hargaE*numberE)
if hitung<30000:
        st.write("total harga perlengkapan Rp.",hitung)
if hitung>30000:
    hitung=hitung-0.1*hitung
    st.write("Diskon 10% total harga perlengkapan Rp.",hitung)
    
st.write('-----------------------------------------------------------------------------------------------------------------------------')

seluruh=hitung1+hitung
st.write('Total Harga keseluruhan Rp.',seluruh)
    
agree = st.checkbox('Saya setuju')

if agree:
    st.write('Terima kasih atas pesanannya!')

jumlah=int(input('banyak makanana'))


