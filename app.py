import streamlit as st 
import google.generativeai as genai 
import os 
from dotenv import load_dotenv 

load_dotenv()

genai.configure(api_key = os.getenv('GOOGLE_API_KEY'))

## designing the page 
st.title('Image to text application ')
user_input = st.text_input('Input Prompt:')
uploaded_file = st.file_uploader('Upload the image...',type=['jpg','jpeg','png'])

#display the image on the page 
from PIL import Image 
img = ''
if uploaded_file is not None:
    img = Image.open(uploaded_file) 
    st.image(img,caption = 'Uploaded image',use_column_width=True) 

## Function for evaluating the image annotating it 
def gemini_response(user_input,img):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if user_input!='':
        response = model.generate_content([user_input,img])
    else:
        response = model.generate_content(img)
    return response.text

#create submit button and map the genai function
submit = st.button('submit')

if submit:
    response = gemini_response(user_input=user_input,img=img)
    st.subheader('The response is:')
    st.write(response)


        
#st.sidebar.title('Model Diagnostics')
#st.sidebar.markdown('click to know more')
#univ_analysis = st.sidebar.button('univeriate analysis')