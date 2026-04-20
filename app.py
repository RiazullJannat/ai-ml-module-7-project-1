import streamlit as st

st.header("Note summary and quiz generator.", anchor=False)
st.markdown("upload up to 3 images to generate note summary and quizzes")
st.divider()


with st.sidebar:
    st.header("Controls", anchor=False)
    #images
    images = st.file_uploader("Upload the photos of your note", accept_multiple_files=True, type=["png", "jpg", "jpeg"])
    if images:
        if len(images)>2:
            st.warning("Please upload only 2 images.")
        else:
            col = st.columns(len(images))
            st.subheader("Uploaded Images")
            for i,img in enumerate(images):
                with col[i]:
                    st.image(img)
    #difficulty
    selectedOptions = st.selectbox("Select the difficulty of the quiz", options=["Easy", "Medium", "Hard"], index=None)
    if selectedOptions:
        st.write("You have selected", selectedOptions, "level quiz")
    else:
        st.error("Please select the difficulty level.")
    st.button("click the button to initiate  AI", type="primary")