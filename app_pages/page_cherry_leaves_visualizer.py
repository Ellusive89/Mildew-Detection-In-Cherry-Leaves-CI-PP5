import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread
import itertools
import random
from annotated_text import annotated_text


def page_leaves_visualizer_body():

    st.title("🍒 Cherry Leaves Visualizer 🍒")

    annotated_text(
        "This page visually contrasts ("healthy") Cherry Leaves "
        "with those infected by ("powdery mildew")."
    )
    version = 'v1'
    if st.checkbox("Comparison of average vs. variability imagery."):

        avg_var_healty = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        avg_var_powdery_mildew = plt.imread(
            f"outputs/{version}/avg_var_powdery_mildew.png")
        st.info(
            f" A distinct visual difference in color consistency is evident: "
            f" Infected leaves, in both average and variability images, "
            f" exhibit more white blotches on their surface. "
            f" In contrast, healthy leaves display a more uniform green shade. "
            f" However, these images don't offer any intuitive patterns to easily distinguish between the two."
        )
        st.image(avg_var_healty, caption='Healty leaves - Avegare and Variability')
        st.image(avg_var_powdery_mildew,
                 caption='Powdery Mildew infected leaves - Average and Variability')
        st.write("---")

    if st.checkbox("Comparisons of average healthy leaves versus infected ones."):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.success(
            f"We observe a comparable pattern where the healthy leaves present a clearer, greener  "
            f"appearance, while the infected leaves exhibit more white coloring on their surface. "
            f"However, contrasting the two types of leaves remains challenging. "
        )

        st.image(diff_between_avgs, caption='Discrepancy among typical images.')

    if st.checkbox("Image Montage"):
        annotated_text(
            "To generate and update the montage, press the ("Generate Montage") button")
        st.info(
            f"The montage assists in visually distinguishing between a healthy leaf and a diseased one. "
            f"The latter displays white, powdery marks or areas on the upper surface of the leaves. "
        )
        my_data_dir = 'inputs/cherry_leaves_dataset/cherry-leaves'
        labels = os.listdir(my_data_dir + '/validation')
        label_to_display = st.selectbox(
            label="Select label:", options=labels, index=0)
        if st.button("Generate Montage"):
            image_montage(dir_path=my_data_dir + '/validation',
                          label_to_display=label_to_display,
                          nrows=8, ncols=3, figsize=(10, 25))
        st.write("---")


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15, 10)):
    sns.set_style("dark")
    labels = os.listdir(dir_path)

    images_list = os.listdir(dir_path+'/' + label_to_display)
    if nrows * ncols < len(images_list):
        img_idx = random.sample(images_list, nrows * ncols)
    else:
        print(
            f"Reduce the number of rows or columns to generate your montage. \n"
            f"Your subset contains {len(images_list)} images."
            f"However, you specified a montage layout for {nrows * ncols} images.")
        return

    list_rows = range(0, nrows)
    list_cols = range(0, ncols)
    plot_idx = list(itertools.product(list_rows, list_cols))

    fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=figsize)
    for x in range(0, nrows*ncols):
        img = imread(f"{dir_path}/{label_to_display}/{img_idx[x]}")
        img_shape = img.shape
        axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
        axes[plot_idx[x][0], plot_idx[x][1]].set_title(
            f"Width {img_shape[1]}px x Height {img_shape[0]}px")
        axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
        axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()

    st.pyplot(fig=fig)
