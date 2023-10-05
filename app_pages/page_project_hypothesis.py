import streamlit as st
import matplotlib.pyplot as plt


def page_project_hypothesis_body():
    st.header("📝 Project-Based Hypothesis and Its Validation 📝")

    st.success(
        f"Powdery mildew is a fungal disease caused by various species "
        f"of ascomycete fungi, predominantly from the order Erysiphales.\n\n"
        f"It affects a wide range of plants, with cherry "
        f"leaves being no exception. This disease is among the easiest "
        f"to identify due to its distinct symptoms.\n\n"
        f"Afflicted plants, including cherries, exhibit white, "
        f"powdery spots or marks on their leaves and stems, "
        f"with the lower leaves often being the most affected.\n"
        f"However, this powdery substance can cover any above-ground "
        f"part of the plant. As the disease advances, these spots expand "
        f"and become denser due to the formation of numerous asexual spores, "
        f"potentially enveloping the whole leaf and making the plant appear "
        f"as though it's been dusted with white powder.\n\n"
        f"Given these pronounced features, we believe they serve as "
        f"adequate markers to differentiate between a healthy and an "
        f"infected leaf.\n\n"
        f"However, their shapes didn't present any distinct patterns for "
        f"identification.\n\n"
        f"Consequently, our machine learning model aims to distinguish "
        f"between a healthy cherry leaf and one affected by powdery mildew "
        f"with a projected accuracy of at least 97%."
    )
