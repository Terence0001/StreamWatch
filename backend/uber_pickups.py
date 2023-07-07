import numpy as np, streamlit as st, pandas as pd

# Titre de l'application
st.title('Ramassages Uber à New York')

# Définition des constantes
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# Fonction pour charger les données (mise en cache)


@st.cache_data
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Chargement des données
data_load_state = st.text('Chargement des données')
data = load_data(10001)
data_load_state.text("Données Chargées !")

# Affichage des données brutes (optionnel)
if st.checkbox('Montrer les données brutes'):
    st.write(data)

# Affichage du nombre de trajets par heure (histogramme)
hist_values = np.histogram(
    data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
st.subheader('Nombre de ramassages par heure')
st.bar_chart(hist_values)

# Filtre des données en fonction de l'heure choisie
hour_to_filter = st.slider('hour', 0, 23, 17)
filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# Affichage de la carte des trajets pour une heure spécifique
st.subheader(f'Carte des ramassages {hour_to_filter}:00')
st.map(filtered_data)
