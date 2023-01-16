import streamlit as st
import sqlite3
from deta import Deta

DETA_KEY="c0vyzncy_FtHYP14kaerkDsVKqs5eGtBBNaRVwtH7"

deta=Deta(DETA_KEY)

db=deta.Base("pelanggan_db")

st.header("Kelompok 6")
st.title("DANBOX")
option = st.selectbox(
    'Pilihan Pengambilan',
    ('pick up', ' delivered'))
st.write('You selected:', option)

#fungsi pesanan
def nama(nama):
    return db.put({"Nama":nama})

import streamlit as st
nama = st.text_input('Nama Pelanggan')
if not nama:
    st.warning('Mohon masukkan nama.')
    
    
def kelas(kelas):
    return db.put({"Kelas":kelas})  

kelas = st.text_input('Kelas')
if not kelas:
    st.warning('Mohon masukkan Kelas.')

    
def d(tanggal):
    return db.put({"Tanggal":tanggal})

import datetime
import streamlit as st
d = st.date_input(
    " Tanggal Pemesanan",
    datetime.date(2019, 7, 6))


def t(waktu):   
    return db.put({"Waktu":waktu})
import datetime
import streamlit as st
t = st.time_input('Waktu Pemesanan', datetime.time(8, 45))
import streamlit as st
st.subheader('Menu Makanan')

from PIL import Image
import streamlit as st
tab1, tab2, tab3, tab4, tab5= st.tabs(["Risol Mayo", "Kue Sus", "Pisang Roll","Martabak Telor","Pastel"])


with tab1:
    st.header("Risol Mayo")
    image = Image.open('oip.jpg')
    st.image(image, width=200)
    import streamlit as st
    number1 = st.number_input('Jumlah Risol')
    

with tab2:
    st.header("Kue Sus")
    image = Image.open('sss.jpg')
    st.image(image, width=200)
    import streamlit as st
    number2 = st.number_input('Jumlah Kue Sus')
    
with tab3:
    st.header("Pisang Roll")
    image = Image.open('sang.jpg')
    st.image(image, width=200)
    import streamlit as st
    number3 = st.number_input('Jumlah Pisang Roll')
    
with tab4:
    st.header("Martabak Telor")
    image = Image.open('mar.jpg')
    st.image(image, width=200)
    import streamlit as st
    number4 = st.number_input('Jumlah Martabak Telor')    
    
with tab5:
    st.header("Pastel")
    image = Image.open('pas.jpg')
    st.image(image, width=200)
    import streamlit as st
    number5 = st.number_input('Jumlah Pastel')
    
Total=st.button("Rincian")
if Total:
    import pandas as pd
    harga1=2000*number1
    harga2=3000*number2
    harga3=2000*number3
    harga4=2000*number4
    harga5=2000*number5
    data = [['Risol',number1,harga1],['Keu Sus',number2,harga2],['Pisang Roll',number3,harga3],['Martabak Telor',number4,harga4],['Pastel',number5,harga5]]
    df=pd.DataFrame(data,columns=['Makanan','jumlah','harga (Rp.)'])
    df


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
tab1, tab2, tab3, tab4, tab5= st.tabs(["Sarung Tangan", " Serbet", "Tabung Reaksi","Gelas Piala","Tabung Ulir"])

with tab1:
    st.header("Sarung Tangan")
    image = Image.open('sarung.jpg')
    st.image(image, width=200)
    import streamlit as st
    numberA = st.number_input('Jumlah sarung tangan')
    

with tab2:
    st.header("Serbet")
    image = Image.open('serbet.jpg')
    st.image(image, width=200)
    import streamlit as st
    numberB = st.number_input('Jumlah serbet')
    
with tab3:
    st.header("Tabung Reaksi")
    image = Image.open('tr.jpg')
    st.image(image, width=200)
    import streamlit as st
    numberC = st.number_input('Jumlah tabung reaksi')
    
with tab4:
    st.header("Gelas Piala")
    image = Image.open('piala.jpg')
    st.image(image, width=200)
    import streamlit as st
    numberD = st.number_input('Jumlah Gelas Piala')    
    
with tab5:
    st.header("Tabung Ulir")
    image = Image.open('lir.jpg')
    st.image(image, width=200)
    import streamlit as st
    numberE = st.number_input('Jumlah tabung ulir')
    
lab = st.button("rincian")
if lab:
    import pandas as pd
    hargaA=2000*numberA
    hargaB=5000*numberB
    hargaC=10000*numberC
    hargaD=20000*numberD
    hargaE=20000*numberE
    data = [['Sarung Tangan',numberA,hargaA],['Serbet',numberB,hargaB],['Tabung Reaksi',numberC,hargaC],['Gelas Piala',numberD,hargaD],['Tabung Ulir',numberE,hargaE]]
    df=pd.DataFrame(data,columns=['Perlengkapan','jumlah','harga (Rp.)'])
    df


hargaA=2000
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

seluruh=hitung1+hitung
st.write('Total Harga keseluruhan Rp.',seluruh)
    
agree = st.checkbox('Saya setuju')

if agree:
    st.write('Terima kasih atas pesanannya!')
