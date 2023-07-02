import streamlit as st
import pandas as pd
from PIL import Image
#from model import open_data, preprocess_data, split_data, load_model_and_predict

min_age = 6
max_age = 122
min_fd = 1
max_fd = 10000
min_delay = 0
max_delay = 3000
min_score = 1
max_score = 5


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
    st.write("## Ваши данные: ")
    st.write(df)


def write_prediction(prediction, prediction_probas):
    st.write("## Наше предсказание: ")
    st.write(prediction)

    st.write("## Вероятность предсказания: ")
    st.write(prediction_probas)


def process_side_bar_inputs():
    st.sidebar.header('Заполните данные здесь, пожалуйста')
    user_input_df = sidebar_input_features()

    # train_df = open_data()
    #train_X_df, _ = split_data(train_df)
    #full_X_df = pd.concat((user_input_df, train_X_df), axis=0)
    #preprocessed_X_df = preprocess_data(full_X_df, test=False)

    #user_X_df = preprocessed_X_df[:1]
    #write_user_data(user_X_df)

    #prediction, prediction_probas = load_model_and_predict(user_X_df)
    #write_prediction(prediction, prediction_probas)


def sidebar_input_features():
    st.error('Error message')
    st.warning('Warning message')
    st.info('Info message')
    st.success('Success message')

    gender = st.sidebar.selectbox("Пол", ("Мужской", "Женский", "Небинарный"))
    age = st.sidebar.slider("Возраст", min_value=min_age, max_value=max_age, step=1)
    customer_type = st.sidebar.radio('Лояльны ли к авиакомпании?', ['да', 'нет'])
    type_of_travel = st.sidebar.selectbox("Тип поездки", ("Бизнес-поездка", "Персональная/личная поездка"))
    airplane_class = st.sidebar.selectbox("Класс обслуживания в самолёте", ("Бизнес", "Эконом", "Эконом Плюс"))
    flight_distance = st.sidebar.number_input("Введите дальность перелета (в милях)", min_value=min_fd, max_value=max_fd)
    departure_delay = st.sidebar.number_input("Введите задержку отправления (в минутах)", min_value=min_delay, max_value=max_delay)
    arrival_delay = st.sidebar.number_input("Введите задержку прибытия (в минутах)", min_value=min_delay, max_value=max_delay)

    time_convenient = st.sidebar.slider("Оцените удобство времени прилета и вылета", min_value=1, max_value=5, key=1, step=1)
    online_booking = st.sidebar.slider("Оцените удобство онлайн-бронирования", min_value=1, max_value=5, key=2, step=1)
    checking_service = st.sidebar.slider("Оцените регистрацию на рейс", min_value=1, max_value=5, key=3, step=1)
    baggage_handling = st.sidebar.slider("Оцените обращение с багажом", min_value=1, max_value=5, key=4, step=1)
    gate_location = st.sidebar.slider("Оцените удобство расположения выхода на посадку в аэропорту", min_value=1, max_value=5, key=5, step=1)
    online_boarding = st.sidebar.slider("Оцените выбор места в самолете", min_value=1, max_value=5, key=6, step=1)
    seat_comfort = st.sidebar.slider("Оцените удобство сиденья", min_value=1, max_value=5, key=7, step=1)
    leg_service = st.sidebar.slider("Оцените место в ногах на борту", min_value=1, max_value=5, key=8, step=1)
    food_drink = st.sidebar.slider("Оцените еду и напитки на борту", min_value=1, max_value=5, key=9, step=1)
    inflight_service = st.sidebar.slider("Оцените обслуживание во время полета", min_value=1, max_value=5, key=14, step=1)
    wifi_service = st.sidebar.slider("Оцените интернет во время полета", min_value=1, max_value=5, key=10, step=1)
    entertainment = st.sidebar.slider("Оцените развлечения во время полета", min_value=1, max_value=5, key=11, step=1)
    onboard_service = st.sidebar.slider("Оцените обслуживание на борту", min_value=1, max_value=5, key=12, step=1)
    cleanliness = st.sidebar.slider("Оцените чистоту на борту", min_value=1, max_value=5, key=13, step=1)
    personal_data = st.sidebar.checkbox('Согласие на обработку персональных данных')

    if personal_data and st.sidebar.button('Готово'):
        st.balloons()

    data = {
        "Gender_Male": gender == 'Мужской',
        "Gender_Female": gender == 'Женский',
        "Gender_Non-binary": gender == 'Небинарный',
        "Age": (age - min_age) / (max_age - min_age),
        "Customer Type": customer_type == 'да',
        "Type of Travel": type_of_travel == "Персональная/личная поездка",
        "Class_Business": airplane_class == "Бизнес",
        "Class_Eco": airplane_class == "Эконом",
        "Class_Eco Plus": airplane_class == "Эконом Плюс",
        "Flight Distance": (flight_distance - min_fd) / (max_fd - min_fd),
        "Departure Delay in Minutes": (departure_delay - min_delay) / (max_delay - min_delay),
        "Arrival Delay in Minutes": (arrival_delay - min_delay) / (max_delay - min_delay),
        "Inflight wifi service": (wifi_service - min_score) / (max_score - min_score),
        "Departure/Arrival time convenient": (time_convenient - min_score) / (max_score - min_score),
        "Ease of Online booking": (online_booking - min_score) / (max_score - min_score),
        "Gate location": (gate_location - min_score) / (max_score - min_score),
        "Food and drink": (food_drink- min_score) / (max_score - min_score),
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
