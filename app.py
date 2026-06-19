import streamlit as st
import pandas as pd
import joblib

# Load Model
model = joblib.load("model/passenger_satisfaction_model.pkl")

# Page Config
st.set_page_config(
    page_title="Airline Passenger Satisfaction Prediction",
    page_icon="✈️",
)

st.title("✈️ Airline Passenger Satisfaction Prediction")
st.markdown(
    "Enter passenger and flight details to predict customer satisfaction."
)

# ==========================
# Passenger Information
# ==========================

st.subheader("Passenger Information")

gender = st.selectbox("Gender",["Female", "Male"])

customer_type = st.selectbox("Customer Type", ["Loyal Customer", "Disloyal Customer"])

age = st.number_input("Age", min_value=7, max_value=100, value=30)

travel_type = st.selectbox("Type of Travel",["Business Travel", "Personal Travel"])

travel_class = st.selectbox("Class",["Business", "Eco", "Eco Plus"])

flight_distance = st.number_input("Flight Distance", min_value=0, value=1000)

# ==========================
# Service Ratings
# ==========================

st.subheader("Service Ratings (0-5)")

wifi = st.slider("Inflight Wifi Service", 0, 5, 3)
online_booking = st.slider("Ease of Online Booking", 0, 5, 3)
gate_location = st.slider("Gate Location", 0, 5, 3)
food_drink = st.slider("Food and Drink", 0, 5, 3)

online_boarding = st.slider("Online Boarding", 0, 5, 3)
seat_comfort = st.slider("Seat Comfort", 0, 5, 3)
entertainment = st.slider("Inflight Entertainment", 0, 5, 3)
onboard_service = st.slider("On-board Service", 0, 5, 3)

legroom = st.slider("Leg Room Service", 0, 5, 3)
baggage = st.slider("Baggage Handling", 0, 5, 3)
checkin = st.slider("Check-in Service", 0, 5, 3)
inflight_service = st.slider("Inflight Service", 0, 5, 3)

cleanliness = st.slider("Cleanliness", 0, 5, 3)

# ==========================
# Flight Details
# ==========================

st.subheader("Flight Details")

departure_arrival = st.slider("Departure/Arrival Time Convenient", 0, 5, 3)

departure_delay = st.number_input("Departure Delay (Minutes)", min_value=0, value=0)

arrival_delay = st.number_input("Arrival Delay (Minutes)", min_value=0, value=0)

# ==========================
# Encoding
# ==========================

gender_map = {
    "Female": 0,
    "Male": 1
}

customer_map = {
    "Loyal Customer": 0,
    "Disloyal Customer": 1
}

travel_map = {
    "Business Travel": 0,
    "Personal Travel": 1
}

class_map = {
    "Business": 0,
    "Eco": 1,
    "Eco Plus": 2
}

# ==========================
# Feature Engineering
# ==========================

total_delay = departure_delay + arrival_delay

delayed_flight = 1 if total_delay > 15 else 0

average_service_rating = (
    wifi +
    online_booking +
    food_drink +
    online_boarding +
    seat_comfort +
    entertainment +
    onboard_service +
    legroom +
    baggage +
    checkin +
    inflight_service +
    cleanliness
) / 12

long_haul = 1 if flight_distance > 3000 else 0

# ==========================
# Predict
# ==========================

if st.button("Predict Satisfaction"):

    input_df = pd.DataFrame([{
        'Gender': gender_map[gender],
        'Customer Type': customer_map[customer_type],
        'Age': age,
        'Type of Travel': travel_map[travel_type],
        'Class': class_map[travel_class],
        'Flight Distance': flight_distance,
        'Inflight wifi service': wifi,
        'Departure/Arrival time convenient': departure_arrival,
        'Ease of Online booking': online_booking,
        'Gate location': gate_location,
        'Food and drink': food_drink,
        'Online boarding': online_boarding,
        'Seat comfort': seat_comfort,
        'Inflight entertainment': entertainment,
        'On-board service': onboard_service,
        'Leg room service': legroom,
        'Baggage handling': baggage,
        'Checkin service': checkin,
        'Inflight service': inflight_service,
        'Cleanliness': cleanliness,
        'Departure Delay in Minutes': departure_delay,
        'Arrival Delay in Minutes': arrival_delay,
        'Total_Delay': total_delay,
        'Delayed_Flight': delayed_flight,
        'Average_Service_Rating': average_service_rating,
        'Long_Haul': long_haul
    }])

    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.markdown("---")

    if prediction == 1:
        st.success(
            f"😊 Satisfied Passenger\n\nConfidence: {probability[1]*100:.2f}%"
        )
    else:
        st.error(
            f"☹️ Dissatisfied Passenger\n\nConfidence: {probability[0]*100:.2f}%"
        )
