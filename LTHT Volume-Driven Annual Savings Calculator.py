import streamlit as st

st.set_page_config(page_title="Leeds Teaching Hospitals NHS Trust Volume-Driven Annual Savings Calculator", layout="wide")

st.image("Ambitions Public Sector Logo.png", width=240)
st.markdown(
    "<h1 style='font-size: 40px;'>Leeds Teaching Hospitals NHS Trust Volume-Driven Annual Savings Calculator</h1>",
    unsafe_allow_html=True
)

fixed_number_1 = 6284.47
fixed_number_2 = 5958.10

st.markdown(
    '<p style="font-size:25px; margin: 0; line-height:1.1;">Enter the Quantity of Grade 2 Workers:</p>',
    unsafe_allow_html=True
)
gradetwo_qty = st.number_input("", min_value=0, step=1, format="%d", key="gradetwo_input")

st.markdown(
    '<p style="font-size:25px; margin: 0; line-height: 1.1;">Enter the Quantity of Grade 3 Workers:</p>',
    unsafe_allow_html=True
)
gradethree_qty = st.number_input("", min_value=0, step=1, format="%d", key="gradethree_input")

if st.button("Calculate Savings"):
    result_1 = fixed_number_1 * gradetwo_qty
    result_2 = fixed_number_2 * gradethree_qty
    total_result = result_1 + result_2

    formatted_result_1 = f"£{result_1:,.2f}"
    formatted_result_2 = f"£{result_2:,.2f}"
    formatted_total_result = f"£{total_result:,.2f}"

    st.markdown(
        f"""
        <p style='color:red; font-size:40px; font-weight:bold; text-align:center; margin: 0; line-height: 1.1;'>
        Annual Savings for Grade 2 Workers: {formatted_result_1}
        </p>
        <p style='color:red; font-size:40px; font-weight:bold; text-align:center; margin: 0; line-height: 1.1;'>
        Annual Savings for Grade 3 Workers: {formatted_result_2}
        </p>
        <p style='color:red; font-size:40px; font-weight:bold; text-align:center; margin: 0; line-height: 1.1;'>
        Total Annual Savings Achieved: {formatted_total_result}
        </p>
        """,
        unsafe_allow_html=True
    )