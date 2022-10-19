import streamlit as st
import time
from img_classification import teachable_machine_classification
import image
from PIL import Image      
app_mode = st.sidebar.selectbox('Select Page',['Home','Image Prediction'])
if app_mode=='Home':
    st.title('Pixar Animation Charachters App')
    st.video('VideoAPPP.mp4') 
    st.subheader('App realised by : Soulaima Ben Youssef') 
   
   
elif app_mode =='Image Prediction':
    st.subheader(' Welcome to pixar charachters  app 💜 ')
    uploaded_file = st.file_uploader(" Dear User 🎇💜,   Please Import the image you want to classify", type="jpg")
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption='Uploaded Image.', use_column_width=True)
        st.write("")
        with st.spinner('Wait For it ....'):
            time.sleep(3)
        #st.write("Classifying....")
        label = teachable_machine_classification(image, 'keras_model.h5')
        if label == 0:
            st.subheader("The charachter is carl fredrick")
            st.balloons()

        elif label ==1 :
            st.subheader("The charachter is Din from Wish dragon")
            st.balloons()

        elif label ==2 :
            st.subheader("The charachter is Elastigirl from The Incredibles")    
            st.balloons()

        elif label ==3 :
            st.subheader("The charachter is JoeGardne from Soul")   
            st.balloons()

        elif label ==4 :
            st.subheader("The charachter is Joy from Inside Out")
            st.balloons()

        elif label ==5 :
            st.subheader("The charachter is LucaPaguro from Luca")   
            st.balloons()

        elif label ==6 :
            st.subheader("The charachter is Merida from Wish Brave")
            st.balloons()

        elif label ==7 :
            st.subheader("The charachter is Miguel from Wish Coco")    
            st.balloons()

        elif label ==8 :
            st.subheader("The charachter is Moana from Wish Moana")
            st.balloons()

        else :
            st.subheader("I didn't regocnize this charachter ,I will need more data for it 💫😁💜")  
             

    
    
    



