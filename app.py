import streamlit as st
import pandas as pd
import pickle

min_age = 6
max_age = 122
min_fd = 1
max_fd = 10000
min_delay = 0
max_delay = 3000
min_score = 1
max_score = 5


def load_model_and_predict(df):
    with open('model.pickle', 'rb') as f:
        model = pickle.load(f)

    prediction = model.predict(df)
    prediction_prob = model.predict_proba(df)[0]

    encode_prediction_prob = {
        0: "Вы будете удовлетворены с вероятностью",
        1: "Вы не будете удовлетворены с вероятностью"
    }
    encode_prediction = {
        0: "Ура! Кажется, Вы довольны нашим сервиом.",
        1: "Сожалеем, кажется, наш сервис Вас не устроил"
    }

    prediction_data = {}
    for key, value in encode_prediction_prob.items():
        prediction_data.update({value: prediction_prob[key]})

    prediction_df = pd.DataFrame(prediction_data, index=[0])
    prediction = encode_prediction[prediction]

    return prediction, prediction_df


def process_main_page():
    show_main_page()
    process_side_bar_inputs()


def show_main_page():
    st.set_page_config(
        layout="wide",
        initial_sidebar_state="auto",
        page_title="Airline Client Satisfaction",
        page_icon="✈️",
    )

    st.title('Понравились ли Вам услуги нашей авиакомпании?✈️')
    st.subheader('Укажите данные о себе и своём рейсе, а также оцените качество оказанных услуг.')
    st.subheader('А мы попробуем отгадать, остались ли Вы довольны предоставленным сервисом или нет :)')

    st.subheader('')
    st.markdown("![airplane_gif](https://tenor.com/ru/view/plane-window-sky-travelling-clouds-flying-gif-13818405.gif)")
    st.subheader('')


def write_user_data(df):
    st.write("## Показываем немного внутрянки. Это Ваши масштабированные данные: ")
    st.write(df)


def write_prediction(prediction, prediction_probas):
    st.write("## Наше предсказание: ")
    st.write(prediction)

    st.write("## Вероятность предсказания: ")
    st.write(prediction_probas)


def process_side_bar_inputs():
    st.sidebar.header('Заполните данные здесь, пожалуйста')
    user_input_df = sidebar_input_features()

    write_user_data(user_input_df)

    prediction, prediction_probs = load_model_and_predict(user_input_df)
    write_prediction(prediction, prediction_probs)


def sidebar_input_features():
    gender = st.sidebar.selectbox("Пол", ("Мужской", "Женский", "Небинарный"))
    age = st.sidebar.slider("Возраст", min_value=min_age, max_value=max_age, value=35, step=1)
    customer_type = st.sidebar.radio('Лояльны ли Вы к авиакомпании?', ['да', 'нет'])
    type_of_travel = st.sidebar.selectbox("Тип поездки", ("Персональная поездка", "Бизнес-поездка"))
    airplane_class = st.sidebar.selectbox("Класс обслуживания в самолёте", ("Эконом", "Эконом Плюс", "Бизнес"))
    flight_distance = st.sidebar.number_input("Введите дальность перелета (в милях)", min_value=min_fd, max_value=max_fd, value=2000)
    departure_delay = st.sidebar.number_input("Введите задержку отправления (в минутах)", min_value=min_delay, max_value=max_delay)
    arrival_delay = st.sidebar.number_input("Введите задержку прибытия (в минутах)", min_value=min_delay, max_value=max_delay)

    time_convenient = st.sidebar.slider("Оцените удобство времени прилета и вылета", min_value=1, max_value=5, key=1, value=3, step=1)
    online_booking = st.sidebar.slider("Оцените удобство онлайн-бронирования", min_value=1, max_value=5, key=2, value=3, step=1)
    checking_service = st.sidebar.slider("Оцените регистрацию на рейс", min_value=1, max_value=5, key=3, value=3, step=1)
    baggage_handling = st.sidebar.slider("Оцените обращение с багажом", min_value=1, max_value=5, key=4, value=3, step=1)
    gate_location = st.sidebar.slider("Оцените удобство расположения выхода на посадку в аэропорту", min_value=1, max_value=5, key=5, value=3, step=1)
    online_boarding = st.sidebar.slider("Оцените выбор места в самолете", min_value=1, max_value=5, key=6, value=3, step=1)
    seat_comfort = st.sidebar.slider("Оцените удобство сиденья", min_value=1, max_value=5, key=7, value=3, step=1)
    leg_service = st.sidebar.slider("Оцените место в ногах на борту", min_value=1, max_value=5, key=8, value=3, step=1)
    food_drink = st.sidebar.slider("Оцените еду и напитки на борту", min_value=1, max_value=5, key=9, value=3, step=1)
    inflight_service = st.sidebar.slider("Оцените обслуживание во время полета", min_value=1, max_value=5, key=14, value=3, step=1)
    wifi_service = st.sidebar.slider("Оцените интернет во время полета", min_value=1, max_value=5, key=10, value=3, step=1)
    entertainment = st.sidebar.slider("Оцените развлечения во время полета", min_value=1, max_value=5, key=11, value=3, step=1)
    onboard_service = st.sidebar.slider("Оцените обслуживание на борту", min_value=1, max_value=5, key=12, value=3, step=1)
    cleanliness = st.sidebar.slider("Оцените чистоту на борту", min_value=1, max_value=5, key=13, value=3, step=1)
    personal_data = st.sidebar.checkbox('Согласие на обработку персональных данных')

    if personal_data:
        if st.sidebar.button('Готово'):
            st.balloons()

    data = {
        "Gender_Female": int(gender == 'Женский'),
        "Gender_Male": int(gender == 'Мужской'),
        "Gender_Non-binary": int(gender == 'Небинарный'),
        "Class_Business": int(airplane_class == "Бизнес"),
        "Class_Eco": int(airplane_class == "Эконом"),
        "Class_Eco Plus": int(airplane_class == "Эконом Плюс"),
        "Age": (age - min_age) / (max_age - min_age),
        "Customer Type": int(customer_type == 'да'),
        "Type of Travel": int(type_of_travel == "Персональная поездка"),
        "Flight Distance": (flight_distance - min_fd) / (max_fd - min_fd),
        "Departure Delay in Minutes": (departure_delay - min_delay) / (max_delay - min_delay),
        "Arrival Delay in Minutes": (arrival_delay - min_delay) / (max_delay - min_delay),
        "Inflight wifi service": (wifi_service - min_score) / (max_score - min_score),
        "Departure/Arrival time convenient": (time_convenient - min_score) / (max_score - min_score),
        "Ease of Online booking": (online_booking - min_score) / (max_score - min_score),
        "Gate location": (gate_location - min_score) / (max_score - min_score),
        "Food and drink": (food_drink - min_score) / (max_score - min_score),
        "Online boarding": (online_boarding - min_score) / (max_score - min_score),
        "Seat comfort": (seat_comfort - min_score) / (max_score - min_score),
        "Inflight entertainment": (entertainment - min_score) / (max_score - min_score),
        "On-board service": (onboard_service - min_score) / (max_score - min_score),
        "Leg room service": (leg_service - min_score) / (max_score - min_score),
        "Baggage handling": (baggage_handling - min_score) / (max_score - min_score),
        "Checkin service": (checking_service - min_score) / (max_score - min_score),
        "Inflight service": (inflight_service - min_score) / (max_score - min_score),
        "Cleanliness": (cleanliness - min_score) / (max_score - min_score)
    }

    df = pd.DataFrame(data, index=[0])
    return df


if __name__ == "__main__":
    process_main_page()
