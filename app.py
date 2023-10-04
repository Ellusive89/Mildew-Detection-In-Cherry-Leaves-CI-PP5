import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_cherry_leaves_visualizer import page_cherry_leaves_visualizer_body
from app_pages.page_powdery_mildew_detector import page_powdery_mildew_detector_body

app = MultiPage(app_name="Mildew Detection In Cherry Leaves")

app.add_page("Cherry Leaves Visualizer", page_cherry_leaves_visualizer_body)
app.add_page("Powdery Mildew Detector", page_powdery_mildew_detector_body)

app.run()
