import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd

from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import (
    load_model_and_predict,
    resize_input_image,
    plot_predictions_probabilities
)


def page_powdery_mildew_detector_body():

    st.header("🔎 Powdery Mildew Detector 🔍")
    st.info(
        f" The client wishes to determine whether a cherry leaf "
        f"is healthy or afflicted with powdery mildew.")

    st.write('---')

    st.info(
        f"Download a collection of leaf images that includes both healthy leaves "
        f"and those with powdery mildew for real-time prediction. "
        f"You can obtain these images from **kaggle** "
        f" 👉 (https://www.kaggle.com/codeinstitute/cherry-leaves) 👈")

    st.write('---')

    images_buffer = st.file_uploader('Upload a sharp image of a cherry leaf for real-time predictions. Multiple selections are allowed.',
                                     accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:

            img_pil = (Image.open(image))
            st.info(f"Cherry Leaves Sample: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(
                img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(
                resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name": image.name, 'Result': pred_class},
                                         ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(
                df_report), unsafe_allow_html=True)
