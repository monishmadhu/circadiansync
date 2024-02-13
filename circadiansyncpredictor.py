import streamlit as st

def main():
    st.title("CircadianSync")

    # Add content to the main area of the app
    st.write("This is the main content of the app.")

    # Use st.markdown to define the width of the sidebar
    st.markdown(
        """
        <style>
        .sidebar .sidebar-content {
            width: 500px;
            background-color: #8832b3;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Add widgets to the sidebar
    st.sidebar.title("CircadianSync")
    # st.sidebar.image("https://raw.githubusercontent.com/your_username/your_repository/main/path/to/your/image.png", use_column_width=True)

    st.sidebar.write("To use CircSync to predict a patient's diagnosis, upload a CSV/Excel file with their gene expression levels as numerical values in it. Make sure there are two columns: 1 for gene names labeled GeneID and 1 for the values labeled ExpressionLevels")

    # Add a file uploader widget to the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv"])

    # Add a big image to the main portion of the app
    # st.image("https://raw.githubusercontent.com/your_username/your_repository/main/path/to/your/big_image.png", use_column_width=True)

    # Add a title and text underneath the image
    st.header("CircadianSync")
    st.write("CircadianSync is a Machine Learning model that intakes the gene expression levels of patients in order to analyze and predict whether they have pancreatic adenocarcinoma, circadian dysfunction, neither, or both.")


    # Process the uploaded file (if any)
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)
  
if __name__ == "__main__":
    main()
