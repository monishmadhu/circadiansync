import streamlit as st

def main():
    st.title("CircadianSync")

    # Add content to the main area of the app
    st.write("This is the main content of the app.")

    # Add widgets to the sidebar
    st.sidebar.title("CircadianSync")
    st.sidebar.image("path/to/your/image.png", use_column_width=True)

    st.sidebar.write("CircadianSync is a Machine Learning model that intakes the gene expression levels of patients in order to analyze and predict whether they have pancreatic adenocarcinoma, circadian dysfunction, neither, or both.")
    st.sidebar.write("To use CircSync to predict a patient's diagnosis, upload a CSV/Excel file with their gene expression levels as numerical values in it. Make sure there are two columns: 1 for gene names labeled GeneID and 1 for the values labeled ExpressionLevels")

    # Add a file uploader widget to the sidebar
    uploaded_file = st.sidebar.file_uploader("Upload a file", type=["csv"])

    # Process the uploaded file (if any)
    if uploaded_file is not None:
        file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type}
        st.write(file_details)
  
if __name__ == "__main__":
    main()
