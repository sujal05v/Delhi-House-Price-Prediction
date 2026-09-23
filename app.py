import streamlit as st
import pandas as pd
import joblib

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------

st.set_page_config(
    page_title="Delhi House Price Predictor",
    page_icon="🏠",
    layout="wide"
)

# --------------------------------------------------
# Custom CSS
# --------------------------------------------------

st.markdown("""
<style>

.main {
    padding-top: 1rem;
}

.title {
    text-align: center;
    font-size: 42px;
    font-weight: 700;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #777;
    margin-bottom: 35px;
}

.section-title {
    font-size: 24px;
    font-weight: 600;
    margin-top: 20px;
    margin-bottom: 15px;
}

.result-box {
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    margin-top: 25px;
}

.result-label {
    font-size: 18px;
    margin-bottom: 8px;
}

.result-price {
    font-size: 38px;
    font-weight: 700;
}

.small-result {
    font-size: 17px;
    margin-top: 8px;
}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# Load Model
# --------------------------------------------------

model = joblib.load("delhi_house_price_model_compressed.pkl")

# --------------------------------------------------
# Header
# --------------------------------------------------

st.markdown(
    '<div class="title">🏠 Delhi House Price Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Predict the estimated price of a residential property in Delhi using Machine Learning'
    '</div>',
    unsafe_allow_html=True
)

# --------------------------------------------------
# Form
# --------------------------------------------------

with st.form("prediction_form"):

    # ---------------- Location ----------------

    st.markdown(
        '<div class="section-title">📍 Location Details</div>',
        unsafe_allow_html=True
    )

    col1, col2 = st.columns(2)

    with col1:
        district = st.selectbox(
            "District",
            [
                "Central Delhi",
                "East Delhi",
                "North Delhi",
                "North East Delhi",
                "South Delhi",
                "South West Delhi",
                "West Delhi"
            ]
        )

    with col2:
        locality = st.selectbox(
            "Locality",
            [
                "Shahdara",
                "Hauz Khas",
                "Model Town",
                "Karol Bagh",
                "Punjabi Bagh",
                "Preet Vihar",
                "Vasant Kunj",
                "Vasant Vihar",
                "Shalimar Bagh",
                "Mahipalpur",
                "Chirag Delhi",
                "Saket",
                "Yamuna Vihar",
                "Rajinder Nagar",
                "Palam",
                "Paschim Vihar",
                "Rohini",
                "Paharganj",
                "Munirka",
                "Mayur Vihar",
                "Laxmi Nagar",
                "Greater Kailash",
                "Rajouri Garden",
                "Anand Vihar",
                "Vivek Vihar",
                "Janakpuri",
                "Dwarka",
                "Dilshad Garden",
                "Tilak Nagar",
                "Patel Nagar",
                "Defence Colony",
                "Pitampura",
                "Patparganj",
                "Seelampur",
                "Civil Lines",
                "Connaught Place",
                "Najafgarh"
            ]
        )

    # ---------------- Property ----------------

    st.markdown(
        '<div class="section-title">🏡 Property Details</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        property_type = st.selectbox(
            "Property Type",
            [
                "Apartment",
                "Builder Floor",
                "Independent House",
                "Villa",
                "Studio Apartment"
            ]
        )

    with col2:
        area_sqft = st.number_input(
            "Area (sqft)",
            min_value=1.0,
            value=1000.0
        )

    with col3:
        bedrooms = st.number_input(
            "Bedrooms",
            min_value=1,
            value=2
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        bathrooms = st.number_input(
            "Bathrooms",
            min_value=1,
            value=2
        )

    with col2:
        floor_no = st.number_input(
            "Floor Number",
            min_value=0,
            value=1
        )

    with col3:
        total_floors = st.number_input(
            "Total Floors",
            min_value=1,
            value=4
        )

    col1, col2, col3 = st.columns(3)

    with col1:
        furnishing = st.selectbox(
            "Furnishing",
            [
                "Furnished",
                "Semi-Furnished",
                "Unfurnished"
            ]
        )

    with col2:
        property_age = st.number_input(
            "Property Age (Years)",
            min_value=0,
            value=5
        )

    with col3:
        ownership_type = st.selectbox(
            "Ownership Type",
            [
                "Freehold",
                "Leasehold",
                "Co-operative Society"
            ]
        )

    # ---------------- Amenities ----------------

    st.markdown(
        '<div class="section-title">✨ Amenities & Infrastructure</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        facing = st.selectbox(
            "Facing",
            [
                "North",
                "South",
                "East",
                "West",
                "North-East",
                "North-West",
                "South-East",
                "South-West"
            ]
        )

    with col2:
        parking_spaces = st.number_input(
            "Parking Spaces",
            min_value=0,
            value=1
        )

    with col3:
        balconies = st.number_input(
            "Balconies",
            min_value=0,
            value=1
        )

    col1, col2 = st.columns(2)

    with col1:
        monthly_maintenance = st.number_input(
            "Monthly Maintenance (₹)",
            min_value=0.0,
            value=5000.0
        )

    with col2:
        road_width = st.number_input(
            "Road Width (ft)",
            min_value=0.0,
            value=30.0
        )

    # ---------------- Distances ----------------

    st.markdown(
        '<div class="section-title">📏 Nearby Facilities</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    with col1:
        metro_distance = st.number_input(
            "Metro Distance (km)",
            min_value=0.0,
            value=2.0
        )

    with col2:
        school_distance = st.number_input(
            "School Distance (km)",
            min_value=0.0,
            value=2.0
        )

    with col3:
        hospital_distance = st.number_input(
            "Hospital Distance (km)",
            min_value=0.0,
            value=2.0
        )

    # ---------------- Button ----------------

    st.markdown("<br>", unsafe_allow_html=True)

    submitted = st.form_submit_button(
        "🔮 Predict House Price",
        use_container_width=True
    )

# --------------------------------------------------
# Prediction
# --------------------------------------------------

if submitted:

    input_data = pd.DataFrame({
        "District": [district],
        "Locality": [locality],
        "Property_Type": [property_type],
        "Area_sqft": [area_sqft],
        "Bedrooms": [bedrooms],
        "Bathrooms": [bathrooms],
        "Floor_No": [floor_no],
        "Total_Floors": [total_floors],
        "Furnishing": [furnishing],
        "Property_Age_Years": [property_age],
        "Ownership_Type": [ownership_type],
        "Facing": [facing],
        "Parking_Spaces": [parking_spaces],
        "Balconies": [balconies],
        "Monthly_Maintenance_INR": [monthly_maintenance],
        "Metro_Distance_km": [metro_distance],
        "School_Distance_km": [school_distance],
        "Hospital_Distance_km": [hospital_distance],
        "Road_Width_ft": [road_width]
    })

    prediction = model.predict(input_data)[0]

    # Convert to crore/lakh
    crore = prediction / 10_000_000
    lakh = prediction / 100_000

    st.markdown(
        f"""
        <div class="result-box">
            <div class="result-label">Estimated Property Price</div>
            <div class="result-price">₹{prediction:,.0f}</div>
            <div class="small-result">
                Approximately ₹{crore:.2f} Crore
                &nbsp; | &nbsp;
                ₹{lakh:.2f} Lakh
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.success("Prediction generated successfully! 🎉")

# --------------------------------------------------
# Footer
# --------------------------------------------------

st.markdown("---")

st.caption(
    "Delhi House Price Prediction • Machine Learning Project • "
    "Random Forest Regression"
)
