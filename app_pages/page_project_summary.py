import streamlit as st
import matplotlib.pyplot as plt


def page_project_summary_body():

    st.header("🗒️ Brief Project Summary 🗒️")

    st.info(
        f"**General Information**\n\n"
        f"Cherry powdery mildew is a superficial fungus affecting both the "
        f"leaves and fruit of cherry trees. It presents as white fungal "
        f"patches, often circular. "
        f"Not only does it harm the cherries it directly infests, but it can "
        f"also contaminate whole packages at harvest. "
        f"In these cases, infected cherries begin to rot, spreading the decay "
        f"to neighboring fruit in the container.\n\n"
        f"The mildew survives the winter as ascospores on leaf tissue "
        f"or in tree limb crotches. During wet conditions, these spores "
        f"are released, settling on new leaf tissue. Its powdery appearance "
        f"can be misleading during packing, as the visible white layer seems "
        f"to wash off during processing. "
        f"However, while the outer layer may appear clean, the underlying "
        f"fungus remains. Once packaged, these spores can revive and spread "
        f"within the fruit boxes.\n\n"
        f"**Project Dataset**\n\n"
        f"The dataset for this project was sourced from"
        f"[Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)\n"
        f"The dataset at hand includes 2104 healthy leaves and an equal number "
        f"of powdery mildew affected leaves."
    )

    st.success(
        f"**The project has two business requirements:**\n\n"
        f"* The client is interested in conducting a study to visually "
        f"differentiate a cherry leaf that is healthy from one that contains "
        f"powdery mildew.\n\n"
        f"* The client is interested in predicting if a cherry leaf is healthy "
        f"or contains powdery mildew."
    )

    st.info(
        f"For further details about the project, kindly refer to the "
        f"[README file](https://github.com/Ellusive89/Mildew-Detection-In-Cherry-Leaves-CI-PP5/blob/main/README.md)"
    )


