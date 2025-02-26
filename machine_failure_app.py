import streamlit as st
import pickle
from PIL import Image



def home_page():
    def set_background(image_path):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{image_path});
                background-size: cover;
                background-position: center;
            }}
            [data-testid="stHeader"]{{
                background-color: rgba(0,0,0,0)
            }}
            </style>
            """,
            unsafe_allow_html=True
        )


    def load_image(image_file):
        import base64
        with open(image_file, "rb") as image:
            return base64.b64encode(image.read()).decode()

    image_path = load_image("pexels-pavel-danilyuk-8294630.jpg")
    set_background(image_path)


    st.title(':house: HOME')
    st.write("Welcome to the Machine Failure Prediction. Use the sidebar to navigate.")



def instructions():
    def set_background(image_path):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{image_path});
                background-size: cover;
                background-position: center;
            }}
            [data-testid="stHeader"]{{
                background-color: rgba(0,0,0,0)
            }}
            </style>
            """,
            unsafe_allow_html=True
        )


    def load_image(image_file):
        import base64
        with open(image_file, "rb") as image:
            return base64.b64encode(image.read()).decode()


    image_path = load_image("pexels-padrinan-1061135.jpg")
    set_background(image_path)

    st.title('INSTRUCTIONS')
    st.title("🚀 Machine Operation Instructions")
    st.header("Step-by-Step Instructions:")
    st.write("1. **Ensure the workspace is clear** to prevent accidents.")
    st.write("2. **Power on the machine** using the main switch.")
    st.write("3. **Set the desired parameters** according to the task.")
    st.write("4. **Load the material** into the machine carefully.")
    st.write("5. **Start the operation** by pressing the 'Start' button.")
    st.write("6. **Monitor the process** to ensure everything runs smoothly.")
    st.write("7. **Power off the machine** once the job is complete.")


def main():
    def set_background(image_path):
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url(data:image/png;base64,{image_path});
                background-size: cover;
                background-position: center;
            }}
            [data-testid="stHeader"]{{
                background-color: rgba(0,0,0,0)
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    def load_image(image_file):
        import base64
        with open(image_file, "rb") as image:
            return base64.b64encode(image.read()).decode()


    image_path = load_image("pexels-agk42-2599244.jpg")
    set_background(image_path)

    st.title('MACHINE FAILURE CHECKER')


    Type = st.selectbox('TYPE', ['LOW', 'MEDIUM', 'HIGH'])
    Air_temperature = st.number_input('AIR TEMPERATURE', min_value=0.0, max_value=3000.0, step=0.1)
    Process_temperature = st.number_input('PROCESS TEMPERATURE [K]', min_value=0.0, max_value=10000.0, step=0.1)
    Rotational_speed = st.number_input('ROTATIONAL SPEED [RPM]', min_value=00.0, max_value=5000.0, step=0.1)
    Torque = st.number_input('TORQUE [NM]', min_value=00.0, max_value=100.0, step=0.1)
    Tool_wear = st.number_input('TOOL WEAR [MIN]')
    Target = st.slider('FIX ON', 0, 1)

    Type_map = {'LOW': 2, 'MEDIUM': 1, 'HIGH': 0}
    features = [Type_map[Type], Air_temperature, Process_temperature, Rotational_speed, Torque, Tool_wear, Target]

    scaler = pickle.load(open('MP_scaler.sav', 'rb'))
    model = pickle.load(open('Machinepredictive.sav', 'rb'))

    failure = st.button('MACHINE FAILURE REASON')
    if failure:
        result = model.predict(scaler.transform([features]))
        if result == 0:
            st.write("HEAT DISSIPATION FAILURE")
        elif result == 1:
            st.write("NO FAILURE")
        elif result == 2:
            st.write("OVER STRAIN FAILURE")
        elif result == 3:
            st.write("POWER FAILURE")
        elif result == 4:
            st.write("RANDOM FAILURE")
        else:
            st.write("TOOL WEAR FAILURE")


def resources_page():
    st.title(':link: RESOURCES')
    st.markdown("### 📂 Dataset")
    st.write("You can download the dataset from the following link with my permission:")
    st.markdown(
        "[Dataset Link](https://www.kaggle.com/datasets/shivamb/machine-predictive-maintenance-classification?select=train.csv)")


# Sidebar Navigation
st.sidebar.title('Navigation')
menu = st.sidebar.radio("Go to", ['Home', 'Instructions', 'Prediction', 'Resources'])

if menu == 'Home':
    home_page()
elif menu == 'Instructions':
    instructions()
elif menu == 'Prediction':
    main()
elif menu == 'Resources':
    resources_page()




