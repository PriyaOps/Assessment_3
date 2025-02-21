import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu
import base64
from PIL import Image
import requests
from io import BytesIO

# Set up page configurations (optional)
# st.set_page_config(page_title="Multiple Disease Prediction", layout="wide")

# Load ML models
kidney_model = pickle.load(open('kidney_model.sav', 'rb'))
liver_model = pickle.load(open('liver_model.sav', 'rb'))
parkinsons_model = pickle.load(open('parkinsons_model.sav', 'rb'))

# Function to get base64 image from URL
def get_base64_image_from_url(image_url):
    response = requests.get(image_url)
    if response.status_code == 200:
        encoded = base64.b64encode(response.content).decode()
        return encoded
    else:
        raise Exception(f"Failed to download image. Status code: {response.status_code}")

# Function to resize images to a consistent size
def resize_image(image, size=(400, 400)):
    img = Image.open(BytesIO(image))  # Open image from the bytes (URL)
    img = img.resize(size)  # Resize to uniform dimensions
    return img

# Sidebar menu for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Home', 'Kidney Prediction', 'Liver Prediction', 'Parkinsons Prediction'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Background styling
st.markdown(
    """
    <style>
        .stApp {
            background: linear-gradient(to bottom, #f0f8ff, #ffffff);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Header Section for the Home Page
if selected == "Home":
    # Get the base64 encoded string from the image URL
    image_url ='https://tse1.mm.bing.net/th?id=OIP.obEy3w7reQp2zSgeKFB67gAAAA&pid=Api&P=0&h=180'
    base64_image = get_base64_image_from_url(image_url)
    
    # Inject custom CSS with the base64-encoded image
    st.markdown(
        f"""
        <style>
        .custom-title {{
            font-size: 50px;
            color: white;
            text-align: center;
            text-shadow: 2px 2px 4px black;
            padding: 40px;
            border-radius: 10px;
            background-image: url('data:image/png;base64,{base64_image}');
            background-size: cover;
            background-position: center;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

    # Display title
    st.markdown("<h1 class='custom-title'>🩺 MULTIPLE DISEASE PREDICTION SYSTEM</h1>", unsafe_allow_html=True)

    # Create a layout with three columns
    col1, col2, col3 = st.columns(3)

    with col1:
        st.image(resize_image(requests.get('https://th.bing.com/th?id=OIP.550oDkNeWxOg2I8ubFffLAHaGG&w=275&h=226&c=8&rs=1&qlt=90&o=6&dpr=1.3&pid=3.1&rm=2').content), width=200)
        st.markdown("<p style='text-align: center; font-size:16px;'>Kidney Disease Prediction</p>", unsafe_allow_html=True)

    with col2:
        st.image(resize_image(requests.get('https://tse1.mm.bing.net/th?id=OIP.iwLfJ48eBSowJZNjTBpzIAHaF7&pid=Api&P=0&h=180').content), width=200)
        st.markdown("<p style='text-align: center; font-size:16px;'>Liver Disease Prediction</p>", unsafe_allow_html=True)

    with col3:
        st.image(resize_image(requests.get('https://th.bing.com/th/id/OIP.rOUmpoRDd85St85C5esf3QHaFP?rs=1&pid=ImgDetMain').content), width=200)
        st.markdown("<p style='text-align: center; font-size:16px;'>Parkinson's Prediction</p>", unsafe_allow_html=True)

if selected == "Kidney Prediction":
  
# Create side-by-side tabs
   tab1= st.tabs([ "🩸 Kidney Disease Diagnosis"])[0]

 


   with tab1:
        
        st.title("Kidney Disease Prediction")

       
        col1, col2, col3, col4, col5 = st.columns(5)

        with col1:
            age = st.text_input('Age')

        with col2:
            bp = st.text_input('Blood Pressure')

        with col3:
            al = st.text_input('Albumin')

        with col4:
            su = st.text_input('Sugar')

        with col5:
            rbc = st.text_input('Red Blood Cells')

        with col1:
            pc = st.text_input('Pus Cell')

        with col2:
            pcc = st.text_input('Pus Cell Clumps')

        with col3:
            ba = st.text_input('Bacteria')

        with col4:
                bgr = st.text_input('Blood Glucose ')

        with col5:
            bu = st.text_input('Blood Urea')

        with col1:
                sc = st.text_input('Serum Creatinine')
                
        with col2:
            pot = st.text_input('Potassium')  

        with col3:
            wc = st.text_input('WBC Count')

        with col4:
            htn = st.text_input('Hypertension')

        with col5:
            dm = st.text_input('Diabetes Mellitus')

        with col1:
            cad = st.text_input('CAD')

        with col2:
            pe = st.text_input('Pedal Edema')

        with col3:
            ane = st.text_input('Anemia')

        kidney_diagnosis = ''

        if st.button("Kidney Test Result"):
            user_input = [age, bp, al, su, rbc, pc, pcc, ba, bgr, bu, sc, pot,
                            wc, htn, dm, cad, pe, ane]
            
            user_input = [float(x) for x in user_input]

            Kidney_Prediction = kidney_model.predict([user_input])

            if Kidney_Prediction[0] == 1:
                    kidney_diagnosis = "The person has kidney disease. It is advised to seek medical consultation for further evaluation and treatment."
            else:
                    kidney_diagnosis = "The person does not have kidney disease. However, maintaining a healthy lifestyle is recommended."

        st.success(kidney_diagnosis)
   

if selected == "Liver Prediction":


    # Create side-by-side tabs
    tab1= st.tabs([ "🩸 Liver Disease Diagnosis"])[0]

    with tab1:
 
            st.title('Liver Disease Prediction')

            col1,col2,col3 = st.columns(3)

            with col1:
                age = st.text_input('age')

            with col2:
                Total_Bilirubin = st.text_input('Total_Bilirubin')

            with col3:
                Direct_Bilirubin = st.text_input('Direct_Bilirubin')

            with col1:
                Alkaline_Phosphotase = st.text_input('Alkaline_Phosphotase')

            with col2:
                Alamine_Aminotransferase = st.text_input('Alamine_Aminotransferase')

            with col3:
                Aspartate_Aminotransferase = st.text_input('Aspartate_Aminotransferase')

            with col1:
                Total_Protiens = st.text_input('Total_Protiens')

            with col2:
                Albumin = st.text_input('Albumin')

            with col3:
                Albumin_and_Globulin_Ratio = st.text_input('Albumin_and_Globulin_Ratio')

            with col1:
                Gender_Male = st.text_input('Gender_Male')

            liver_diagnosis = ''

            if st.button("Liver Test Result"):

                user_input = [age, Total_Bilirubin, Direct_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                                Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio,Gender_Male]
                
                user_input = [float(x) for x in user_input]

                liver_Prediction = liver_model.predict([user_input])

                if liver_Prediction[0] == 1:

                    liver_diagnosis = "The person has liver disease"
                else:
                    liver_diagnosis = "The person does not have liver disease"

            st.success(liver_diagnosis)
  # Parkinson's Prediction Page
if selected == "Parkinsons Prediction":

    # Create side-by-side tabs
    tab1 = st.tabs(["🩸 Parkinsons   Disease Diagnosis"])[0]  # Unpack the first tab

    with tab1:
        
            # page title
            st.title("Parkinsons Prediction")
            col1, col2, col3, col4, col5 = st.columns(5)

            with col1:
                fo = st.text_input('MDVP:Fo(Hz)')

            with col2:
                fhi = st.text_input('MDVP:Fhi(Hz)')

            with col3:
                flo = st.text_input('MDVP:Flo(Hz)')

            with col4:
                Jitter_percent = st.text_input('MDVP:Jitter(%)')

            with col5:
                Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')

            with col1:
                RAP = st.text_input('MDVP:RAP')

            with col2:
                PPQ = st.text_input('MDVP:PPQ')

            with col3:
                DDP = st.text_input('Jitter:DDP')

            with col4:
                Shimmer = st.text_input('MDVP:Shimmer')

            with col5:
                Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')

            with col1:
                APQ3 = st.text_input('Shimmer:APQ3')

            with col2:
                APQ5 = st.text_input('Shimmer:APQ5')

            with col3:
                APQ = st.text_input('MDVP:APQ')

            with col4:
                DDA = st.text_input('Shimmer:DDA')

            with col5:
                NHR = st.text_input('NHR')

            with col1:
                HNR = st.text_input('HNR')

            with col2:
                RPDE = st.text_input('RPDE')

            with col3:
                DFA = st.text_input('DFA')

            with col4:
                spread1 = st.text_input('spread1')

            with col5:
                spread2 = st.text_input('spread2')

            with col1:
                D2 = st.text_input('D2')

            with col2:
                PPE = st.text_input('PPE')

                

            # code for Prediction
            parkinsons_diagnosis = ''

            # creating a button for Prediction    
            if st.button("Parkinson's Test Result"):

                user_input = [fo, fhi, flo, Jitter_percent, Jitter_Abs,
                            RAP, PPQ, DDP,Shimmer, Shimmer_dB, APQ3, APQ5,
                            APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]

                user_input = [float(x) for x in user_input]

                parkinsons_prediction = parkinsons_model.predict([user_input])

                if parkinsons_prediction[0] == 1:
                    parkinsons_diagnosis = "The person has Parkinson's disease"
                else:
                    parkinsons_diagnosis = "The person does not have Parkinson's disease"

            st.success(parkinsons_diagnosis)
