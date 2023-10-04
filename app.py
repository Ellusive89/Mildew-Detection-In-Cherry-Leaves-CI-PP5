import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.page_cherry_leaves_visualizer import page_cherry_leaves_visualizer_body

app = MultiPage(app_name="Mildew Detection In Cherry Leaves")

app.add_page("Cherry Leaves Visualizer", page_cherry_leaves_visualizer_body)
