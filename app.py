import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_project_summary import page_project_summary_body
from app_pages.page_cherry_leaves_visualizer import page_cherry_leaves_visualizer_body
from app_pages.page_powdery_mildew_detector import page_powdery_mildew_detector_body
from app_pages.page_project_hypothesis import page_project_hypothesis_body
from app_pages.page_ml_performance import page_ml_performance_metrics

app = MultiPage(app_name="Mildew Detection In Cherry Leaves")

app.add_page("Brief Project Summary", page_project_summary_body)
app.add_page("Cherry Leaves Visualizer", page_cherry_leaves_visualizer_body)
app.add_page("Powdery Mildew Detector", page_powdery_mildew_detector_body)
app.add_page("Project-Based Hypothesis and Its Validation",
             page_project_hypothesis_body)
app.add_page("Machine Learning Performance", page_ml_performance_metrics)

app.run()
