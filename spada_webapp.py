import streamlit as st
import pickle

lin_model=pickle.load(open('lin_model.pkl','rb'))
log_model=pickle.load(open('log_model.pkl','rb'))

def classify(num):
    if num<2.0:
        print(num)
        return 'TIDAK SEHAT'
    elif num<2.2:
        print(num)
        return 'SEDANG'
    else:
        print(num)
        return 'BAIK'
def main():
    st.title("Tugas Besar SPADA DIKTI")
    html_temp = """
    <h4> Kelompok 45 | Tel-U 3</h4>
    <h5> 1. Alfinata Yusuf Sitaba <h5>
    <h5> 2. Jehua Kusuma Dewa <h5>
    <h5> 3. Fauzi Arya Surya Abadi <h5><br/>
    <div style="background-color:blue ;padding:10px">
    <h2 style="color:white;text-align:center;">Air Level Classification</h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    activities=['Linear Regression','Logistic Regression']
    option=st.sidebar.selectbox('Which model would you like to use?',activities)
    st.subheader(option)

    pm10 = st.slider('Partikulat (PM10)',0.0, 100.0)
    so2 = st.slider('Belerang dioksida (Sulfur dioxide)',0.0, 100.0)
    co = st.slider('Karbon monoksida (CO)',0.0, 100.0)
    o3 = st.slider('Ozon (O3)',0.0, 100.0)
    no2 = st.slider('Nitrogen dioksida (NO2)',0.0, 100.0)
    inputs=[[pm10,so2,co,o3,no2]]
    
    if st.button('Classify'):
        if option=='Linear Regression':
            st.success(classify(lin_model.predict(inputs)))
        elif option=='Logistic Regression':
            st.success(classify(log_model.predict(inputs)))

if __name__=='__main__':
    main()
