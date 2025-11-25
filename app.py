import streamlit as st
from agents.controller_agent import ControllerAgent

# ---------------------------
# Streamlit Page Configuration
# ---------------------------
st.set_page_config(page_title="FitLife AI", page_icon="💪", layout="centered")

# ---------------------------
# App Title
# ---------------------------
st.title("💪 FitLife - AI Fitness & Diet Multi-Agent System")

st.write(
    """
    Welcome to **FitLife**, your personal AI-driven multi-agent fitness & diet planner!  
    This app uses **Workout Agent**, **Diet Agent**, and **Explanation Agent**  
    managed by a **Controller Agent** to generate personalized fitness & diet plans.
    """
)

# ---------------------------
# User Inputs
# ---------------------------
st.header("📋 Enter Your Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input("Age", min_value=10, max_value=100, step=1)
    height = st.number_input("Height (in cm)", min_value=120, max_value=220)
    fitness_goal = st.selectbox(
        "Fitness Goal",
        ["Weight Loss", "Muscle Gain", "General Fitness", "Fat Loss"]
    )

with col2:
    weight = st.number_input("Weight (in kg)", min_value=30, max_value=200)
    activity_level = st.selectbox(
        "Activity Level",
        ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
    )

submitted = st.button("Generate Plan")

# ---------------------------
# When user clicks button
# ---------------------------
if submitted:
    with st.spinner("⏳ Generating your personalized fitness & diet plan..."):
        try:
            agent = ControllerAgent()

            user_data = {
                "age": age,
                "height": height,
                "weight": weight,
                "fitness_goal": fitness_goal,
                "activity_level": activity_level
            }

            result = agent.generate_plan(user_data)

            st.success("Plan Generated Successfully!")

            # Display Results
            st.header("🏋️ Workout Plan")
            st.write(result.get("workout_plan", "No workout plan generated."))

            st.header("🥗 Diet Plan")
            st.write(result.get("diet_plan", "No diet plan generated."))

            st.header("ℹ️ Explanation")
            st.write(result.get("explanation", "No explanation available."))

        except Exception as e:
            st.error(f"Error: {e}")
