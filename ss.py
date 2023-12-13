import streamlit as st
from PIL import Image



def main():
    st.title("Computer Vision Project")
    activities = ["Drowsiness Detection System"]
    summary_choice = st.selectbox("Select Activity", ["Computer Vision Operation On Image", "Drowsiness Detection Using Webcam"])
    if summary_choice == "Computer Vision Operation On Image":
        st.header("Computer Vision Operation On Image")
        st.subheader("Upload an Image")
        # Upload an image file
        image = st.file_uploader("Choose an image...", type=["jpg", "png", "jpeg"])
        if image is not None:
            pil_image = Image.open(image)
            st.subheader("Original Image :")
            st.image(image, caption="Uploaded Image", use_column_width=True)
        st.sidebar.header("Select Operations : ")
        brightness = st.sidebar.slider("Brightness",0.0, 2.0, 1.0)
        selected_color = st.sidebar.radio("Select Color : ", ["None","BGR", "Gray"])
        selected_filter = st.sidebar.radio("Select Filter Type : ", ["None","Blur Filters", "Sharpening Filters","Gradient Filters"])
        selected_morphological = st.sidebar.radio("Select Morphological Operation : ", ["None","Erosion", "Dilation", "Opening", "Closing", "Gradient" , "Black Hat" , "Top Hat"])
        selected_thershold = st.sidebar.radio("Select Thershold Type : ", ["None","Binary Thersholding", "Inverse Binary Thersholding", "Turncate Thersholding" , "Zero Thersholding" , "Inverted Zero Thersholding"])
        edge_detection = st.sidebar.checkbox("Canny Edge Detection")
        drowy = st.sidebar.checkbox("Find Drowsy or Not")
        face_detection = st.sidebar.checkbox("Face Detection")
        eye_detection = st.sidebar.checkbox("Eye and Mouth Detection")
        find_contour = st.sidebar.checkbox("Find Contour")


    if image is not None:
        # Display original image
        st.image(image, caption="Original Image", use_column_width=True)

    if image is not None:
        st.subheader("Updated Image :")
        st.image(pil_image, caption="Updated Image", use_column_width=True)

if __name__ == "__main__":
    main()
