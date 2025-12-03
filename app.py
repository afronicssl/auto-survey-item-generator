import streamlit as st
from utils import auto_generate_items

st.title("Automatic Item Generator")

constructs = st.text_area(
    "Enter constructs (one per line):",
    """Marketing Strategy
Customer Satisfaction"""
)

num_items = st.number_input("Items per construct:", min_value=1, max_value=20, value=3)

if st.button("Generate Items"):
    constructs_list = constructs.strip().split("\n")
    result = auto_generate_items(constructs_list, num_items)
    st.write("### Generated Items:")
    for line in result:
        st.write(line)

