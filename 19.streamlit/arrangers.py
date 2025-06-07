import streamlit as st
import pandas as pd
'''
# Set page config
st.set_page_config(page_title="Arrangers - Event Services", layout="wide")

# Dummy data
vendors_data = [
    {"Name": "Sharma Caterers", "Category": "Caterer", "Location": "Bhopal", "Contact": "9876543210", "Price": "₹5000+"},
    {"Name": "Raj Decorators", "Category": "Decorator", "Location": "Bhopal", "Contact": "9876543211", "Price": "₹3000+"},
    {"Name": "Royal Banquet Hall", "Category": "Venue", "Location": "Bhopal", "Contact": "9876543212", "Price": "₹10000+"},
    {"Name": "ClickStudio Photography", "Category": "Photographer", "Location": "Bhopal", "Contact": "9876543213", "Price": "₹7000+"},
    {"Name": "Sweet Delights Halwai", "Category": "Halwai", "Location": "Bhopal", "Contact": "9876543214", "Price": "₹2000+"},
    {"Name": "Creative Cards", "Category": "Wedding Card Maker", "Location": "Bhopal", "Contact": "9876543215", "Price": "₹1500+"},
    {"Name": "EventCam Pros", "Category": "Cameraman", "Location": "Bhopal", "Contact": "9876543216", "Price": "₹4000+"}
]
vendors_df = pd.DataFrame(vendors_data)

# Sidebar Navigation
st.sidebar.title("Arrangers")
page = st.sidebar.radio("Navigate", ["Home", "Browse Vendors", "Book an Event", "Vendor Registration", "About"])

# Home Page
if page == "Home":
    st.title("Welcome to Arrangers 🎉")
    st.subheader("Your one-stop platform for real-time event planning and vendor bookings.")
    st.image("https://images.unsplash.com/photo-1524169358666-79f22534bc6e", use_column_width=True)
    st.info("Use the sidebar to explore vendors, book services, or register.")

# Browse Vendors Page
elif page == "Browse Vendors":
    st.title("Browse Event Vendors")
    category = st.selectbox("Choose a Service Category", vendors_df["Category"].unique())
    filtered_df = vendors_df[vendors_df["Category"] == category]
    st.dataframe(filtered_df.reset_index(drop=True), use_container_width=True)

# Booking Page
elif page == "Book an Event":
    st.title("Book Your Event")
    with st.form("booking_form"):
        name = st.text_input("Your Name")
        contact = st.text_input("Contact Number")
        event_type = st.selectbox("Event Type", ["Birthday", "Engagement", "Wedding", "Corporate", "Other"])
        location = st.text_input("Event Location")
        date = st.date_input("Event Date")
        vendor_type = st.selectbox("Service Required", vendors_df["Category"].unique())
        submitted = st.form_submit_button("Submit Booking Request")
        if submitted:
            st.success(f"Thank you {name}, your request for a {event_type} has been submitted!")

# Vendor Registration Page
elif page == "Vendor Registration":
    st.title("Vendor Registration")
    with st.form("vendor_form"):
        vendor_name = st.text_input("Vendor Name")
        category = st.selectbox("Category", vendors_df["Category"].unique())
        location = st.text_input("Operating Location")
        contact = st.text_input("Contact Number")
        price = st.text_input("Starting Price")
        submitted = st.form_submit_button("Register Vendor")
        if submitted:
            st.success(f"Vendor '{vendor_name}' registered successfully!")

# About Page
elif page == "About":
    st.title("About Arrangers")
    st.markdown("""
        **Arrangers** is an event planning platform built to simplify local event management.
        
        - 🏠 Real-time venue and vendor search  
        - 📆 Last-minute restaurant bookings  
        - 🎉 Focus on small to mid-size gatherings  
        - 🤝 Local vendor discovery made easy
        
        _Founder: [Your Name]_  
        _Made with ❤️ using Streamlit_
    """)
'''

## 2nd
# Move the uploaded logo file to a standard filename for referencing in the Streamlit app
import shutil

source_path = "/mnt/data/Arrangers-removebg-preview.png"
dest_path = "/mnt/data/arrangers_logo.png"

# Rename the uploaded file to a fixed name
shutil.copyfile(source_path, dest_path)

dest_path
