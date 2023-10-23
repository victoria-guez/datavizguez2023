# streamlit run C:\Users\33781\Desktop\datavizguez2023\main.py [ARGUMENTS]

import os
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px
from datetime import datetime

# dictionnaires :


CODES_REGION = {
    "Hauts-de-France": 32,
    "Île-de-France": 11,
    "Grand Est": 44,
    "Normandie": 28,
    "Bretagne": 53,
    "Pays de la Loire": 52,
    "Centre-Val de Loire": 24,
    "Bourgogne-Franche-Comté": 27,
    "Auvergne-Rhône-Alpes": 84,
    "Occitanie": 76,
    "Provence-Alpes-Côte d'Azur": 93,
    "Corse": 94,
    "Nouvelle-Aquitaine": 75
}

REGIONS = {
    1: 'Auvergne-Rhône-Alpes',
    2: 'Hauts-de-France',
    3: 'Auvergne-Rhône-Alpes',
    4: 'Provence-Alpes-Côte d\'Azur',
    5: 'Provence-Alpes-Côte d\'Azur',
    6: 'Provence-Alpes-Côte d\'Azur',
    7: 'Auvergne-Rhône-Alpes',
    8: 'Grand Est',
    9: 'Occitanie',
    10: 'Grand Est',
    11: 'Occitanie',
    12: 'Occitanie',
    13: 'Provence-Alpes-Côte d\'Azur',
    14: 'Normandie',
    15: 'Auvergne-Rhône-Alpes',
    16: 'Nouvelle-Aquitaine',
    17: 'Nouvelle-Aquitaine',
    18: 'Centre-Val de Loire',
    19: 'Nouvelle-Aquitaine',
    20: 'Corse',
    21: 'Bourgogne-Franche-Comté',
    22: 'Bretagne',
    23: 'Nouvelle-Aquitaine',
    24: 'Nouvelle-Aquitaine',
    25: 'Bourgogne-Franche-Comté',
    26: 'Auvergne-Rhône-Alpes',
    27: 'Normandie',
    28: 'Centre-Val de Loire',
    29: 'Bretagne',
    30: 'Occitanie',
    31: 'Occitanie',
    32: 'Occitanie',
    33: 'Nouvelle-Aquitaine',
    34: 'Occitanie',
    35: 'Bretagne',
    36: 'Centre-Val de Loire',
    37: 'Centre-Val de Loire',
    38: 'Auvergne-Rhône-Alpes',
    39: 'Bourgogne-Franche-Comté',
    40: 'Nouvelle-Aquitaine',
    41: 'Centre-Val de Loire',
    42: 'Auvergne-Rhône-Alpes',
    43: 'Auvergne-Rhône-Alpes',
    44: 'Pays de la Loire',
    45: 'Centre-Val de Loire',
    46: 'Occitanie',
    47: 'Nouvelle-Aquitaine',
    48: 'Occitanie',
    49: 'Pays de la Loire',
    50: 'Normandie',
    51: 'Grand Est',
    52: 'Grand Est',
    53: 'Pays de la Loire',
    54: 'Grand Est',
    55: 'Grand Est',
    56: 'Bretagne',
    57: 'Grand Est',
    58: 'Bourgogne-Franche-Comté',
    59: 'Hauts-de-France',
    60: 'Hauts-de-France',
    61: 'Normandie',
    62: 'Hauts-de-France',
    63: 'Auvergne-Rhône-Alpes',
    64: 'Nouvelle-Aquitaine',
    65: 'Occitanie',
    66: 'Occitanie',
    67: 'Grand Est',
    68: 'Grand Est',
    69: 'Auvergne-Rhône-Alpes',
    70: 'Bourgogne-Franche-Comté',
    71: 'Bourgogne-Franche-Comté',
    72: 'Pays de la Loire',
    73: 'Auvergne-Rhône-Alpes',
    74: 'Auvergne-Rhône-Alpes',
    75: 'Île-de-France',
    76: 'Normandie',
    77: 'Île-de-France',
    78: 'Île-de-France',
    79: 'Nouvelle-Aquitaine',
    80: 'Hauts-de-France',
    81: 'Occitanie',
    82: 'Occitanie',
    83: 'Provence-Alpes-Côte d\'Azur',
    84: 'Provence-Alpes-Côte d\'Azur',
    85: 'Pays de la Loire',
    86: 'Nouvelle-Aquitaine',
    87: 'Nouvelle-Aquitaine',
    88: 'Grand Est',
    89: 'Bourgogne-Franche-Comté',
    90: 'Bourgogne-Franche-Comté',
    91: 'Île-de-France',
    92: 'Île-de-France',
    93: 'Île-de-France',
    94: 'Île-de-France',
    95: 'Île-de-France',
    97: 'Hors de France',
    99: 'Outre-mer',

}

DEPARTEMENTS = {

    1: 'Ain',
    2: 'Aisne',
    3: 'Allier',
    4: 'Alpes-de-Haute-Provence',
    5: 'Hautes-Alpes',
    6: 'Alpes-Maritimes',
    7: 'Ardèche',
    8: 'Ardennes',
    9: 'Ariège',
    10: 'Aube',
    11: 'Aude',
    12: 'Aveyron',
    13: 'Bouches-du-Rhône',
    14: 'Calvados',
    15: 'Cantal',
    16: 'Charente',
    17: 'Charente-Maritime',
    18: 'Cher',
    19: 'Corrèze',
    21: 'Côte-d\'Or',
    22: 'Côtes-d\'Armor',
    23: 'Creuse',
    24: 'Dordogne',
    25: 'Doubs',
    26: 'Drôme',
    27: 'Eure',
    28: 'Eure-et-Loir',
    29: 'Finistère',
    30: 'Gard',
    31: 'Haute-Garonne',
    32: 'Gers',
    33: 'Gironde',
    34: 'Hérault',
    35: 'Ille-et-Vilaine',
    36: 'Indre',
    37: 'Indre-et-Loire',
    38: 'Isère',
    39: 'Jura',
    40: 'Landes',
    41: 'Loir-et-Cher',
    42: 'Loire',
    43: 'Haute-Loire',
    44: 'Loire-Atlantique',
    45: 'Loiret',
    46: 'Lot',
    47: 'Lot-et-Garonne',
    48: 'Lozère',
    49: 'Maine-et-Loire',
    50: 'Manche',
    51: 'Marne',
    52: 'Haute-Marne',
    53: 'Mayenne',
    54: 'Meurthe-et-Moselle',
    55: 'Meuse',
    56: 'Morbihan',
    57: 'Moselle',
    58: 'Nièvre',
    59: 'Nord',
    60: 'Oise',
    61: 'Orne',
    62: 'Pas-de-Calais',
    63: 'Puy-de-Dôme',
    64: 'Pyrénées-Atlantiques',
    65: 'Hautes-Pyrénées',
    66: 'Pyrénées-Orientales',
    67: 'Bas-Rhin',
    68: 'Haut-Rhin',
    69: 'Rhône',
    70: 'Haute-Saône',
    71: 'Saône-et-Loire',
    72: 'Sarthe',
    73: 'Savoie',
    74: 'Haute-Savoie',
    75: 'Paris',
    76: 'Seine-Maritime',
    77: 'Seine-et-Marne',
    78: 'Yvelines',
    79: 'Deux-Sèvres',
    80: 'Somme',
    81: 'Tarn',
    82: 'Tarn-et-Garonne',
    83: 'Var',
    84: 'Vaucluse',
    85: 'Vendée',
    86: 'Vienne',
    87: 'Haute-Vienne',
    88: 'Vosges',
    89: 'Yonne',
    90: 'Territoire de Belfort',
    91: 'Essonne',
    92: 'Hauts-de-Seine',
    93: 'Seine-Saint-Denis',
    94: 'Val-de-Marne',
    95: 'Val-d\'Oise',
    97: 'Outre-Mer',

    20: 'Corse',
}

# initialisation de la dataframe (sans dynamisme)
# la database a déjà été travaillée d'où le manque de dynamisme et nous allons travailler la df ci dessous

current_directory = os.path.dirname(__file__)
csv_path = os.path.join(current_directory, "deces.csv")
df = pd.read_csv(csv_path, sep=';',
                 encoding='utf-8')

# ajout/modification de colonnes dans la dataframe

# passage en date time des variable DATE_M et DATE_N
# (elles sont sous forme de nombres de jours écoulés deuis le 30 décembre 1899)

# DATE_N
df['DATE_N'] = pd.to_numeric(df['DATE_N'], errors='coerce')
base_date = datetime(1899, 12, 30)
df['DATE_N'] = base_date + pd.to_timedelta(df['DATE_N'], unit='D')

# DATE_M
df['DATE_M'] = pd.to_numeric(df['DATE_M'], errors='coerce')
base_date = datetime(1899, 12, 30)
df['DATE_M'] = base_date + pd.to_timedelta(df['DATE_M'], unit='D')

# récupération des code de département
df['DEPARTEMENT_M'] = df['POSTALE_M'].apply(lambda x: (x // 1000))
df['DEPARTEMENT_N'] = df['POSTALE_N'].apply(lambda x: (x // 1000))
df['DEPARTEMENT_N'] = df['DEPARTEMENT_N'].fillna(20)
df['DEPARTEMENT_M'] = df['DEPARTEMENT_M'].fillna(20)

# ajout des noms des régions et des departements de naissance (N) et de mort (M) dans la dataframe
df['REGION_M'] = df['DEPARTEMENT_M'].map(REGIONS)
df['REGION_N'] = df['DEPARTEMENT_N'].map(REGIONS)
df['NOM_DEP_M'] = df['DEPARTEMENT_M'].map(DEPARTEMENTS)
df['NOM_DEP_N'] = df['DEPARTEMENT_N'].map(DEPARTEMENTS)

# création des codes regions pour la map
df['CODE_REGION_M'] = df['REGION_M'].map(CODES_REGION)
df['CODE_REGION_N'] = df['REGION_N'].map(CODES_REGION)

# separation nom et prenom
df[['NOM', 'PRENOM']] = df['NOM_COMPLET'].str.split('*', expand=True, n=1)

# on supprime les tirets des noms composés qui risqueraient d'etre considéré comme deux prénom s'il est en premier préno
df['PRENOM'] = df['PRENOM'].str.replace('-', '')

# recuperation du premier prenom
df['PREMIER_PRENOM'] = df['PRENOM'].str.split().str[0]

# count du nombre de prénoms
df['NB_PRENOM'] = df['PRENOM'].str.count(' ') + 1

# récupération de l'année de naissance
df['ANNEE'] = df['DATE_N'].dt.year

# calcul de l'age
df['AGE'] = (df['DATE_M'] - df['DATE_N']).dt.days // 365

# definition des tranches d'âge
tranches_age = [-1, 20, 35, 50, 65, 75, 85, 90, 95, np.inf]
labels = ['0-20', '21-35', '36-50', '51-65', '66-75', '76-85', '86-90', '91-95', '95 et plus']
df['TRANCHE_AGE'] = pd.cut(df['AGE'], bins=tranches_age, labels=labels)

# introduction de la variable MEME_REGION
df['MEME_REGION'] = (df['REGION_M'] == df['REGION_N'])

# réarrangement des colonnes
df = df[['INDICE', 'PRENOM', 'NOM', 'SEXE', 'AGE', 'DATE_M', 'DEPARTEMENT_M', 'REGION_M',
         'DATE_N', 'DEPARTEMENT_N', 'REGION_N', 'POSTALE_N', 'POSTALE_M', 'NB_PRENOM', 'PREMIER_PRENOM', 'ANNEE',
         'NOM_COMPLET', 'NOM_DEP_M', 'NOM_DEP_N', 'VILLE_N', 'PAYS_N', 'TRANCHE_AGE',
         'MEME_REGION', 'CODE_REGION_N', 'CODE_REGION_M']]

# affiche test
# st.write(df['AGE'].dtypes)
# st.write(df['DEPARTEMENT_M'].dtypes)
# st.write(df['DATE_N'].dtypes)


# ________________________________GRAPH1______________________________________
# diagramme en barre de la répartition de l'âge des personnes décédées ainsi que pour chaque tranche d'âge de leur sexe

NB_SEXE_AGE = pd.crosstab(df['TRANCHE_AGE'], df['SEXE'])

graph1, axes1 = plt.subplots()

# initialisation du graphique
HOMMES = axes1.bar(labels, NB_SEXE_AGE[1], width=0.3, label='Hommes', color='blue')
FEMMES = axes1.bar(labels, NB_SEXE_AGE[2], width=0.3, label='Femmes', color='pink', bottom=NB_SEXE_AGE[1])

axes1.set_xlabel('Tranche d\'âge')
axes1.set_ylabel('Nombre de personnes')
axes1.legend()

# ____________________________________________GRAPH2____________________________________________
# count
NB_N = df.groupby('REGION_N')['INDICE'].count().reset_index()
NB_M = df.groupby('REGION_M')['INDICE'].count().reset_index()

# initialisation et placement des barres
graph2 = px.bar(NB_N, x='REGION_N', y='INDICE')
graph2.add_bar(x=NB_M['REGION_M'], y=NB_M['INDICE'], name='Décès')

graph2.update_traces(x='REGION_N', selector=dict(name='Naissances'))
graph2.update_layout(barmode='group')
graph2.update_xaxes(title_text='Régions de France')
graph2.update_yaxes(title_text='Nombre de décès et de morts')

# ____________________________________________GRAPH3____________________________________________

graph3 = px.scatter(df, x='DATE_N', y='NB_PRENOM',
                    labels={'DATE_N': 'Date de Naissance', 'NB_PRENOM': 'Nombre de Prénoms'})

# ____________________________________________GRAPH4____________________________________________

# création des varaibles nécessaires


PROP_REGION = df['MEME_REGION'].mean()

# initialisation du graphique
data = pd.DataFrame({'PROP': [PROP_REGION, 1 - PROP_REGION]},
                    index=['Né et décédé dans la même région', 'né et décédé dans deux régions différentes'])
graph4 = px.pie(data, names=data.index, values='PROP')

PROP_REGION = df.groupby('TRANCHE_AGE')['MEME_REGION'].mean()

# 1
TRANCHE1 = PROP_REGION["0-20"]
graph41 = px.pie(values=[TRANCHE1, 1 - TRANCHE1], title="0-20 ans")

# 2
TRANCHE2 = PROP_REGION["21-35"]
graph42 = px.pie(values=[TRANCHE2, 1 - TRANCHE2], title="21-35 ans")

# 3
TRANCHE3 = PROP_REGION["36-50"]
graph43 = px.pie(values=[TRANCHE3, 1 - TRANCHE3], title="36-50 ans")

# 4
TRANCHE4 = PROP_REGION["51-65"]
graph44 = px.pie(values=[TRANCHE4, 1 - TRANCHE4], title="51-65 ans")

# 5
TRANCHE5 = PROP_REGION["66-75"]
graph45 = px.pie(values=[TRANCHE5, 1 - TRANCHE5], title="66-75 ans")

# 6
TRANCHE6 = PROP_REGION["76-85"]
graph46 = px.pie(values=[TRANCHE6, 1 - TRANCHE6], title="76-85 ans")

# 7
TRANCHE7 = PROP_REGION["86-90"]
graph47 = px.pie(values=[TRANCHE7, 1 - TRANCHE7], title="86-90 ans")

# 8
TRANCHE8 = PROP_REGION["91-95"]
graph48 = px.pie(values=[TRANCHE8, 1 - TRANCHE8], title="91-95 ans")

# 9
TRANCHE9 = PROP_REGION["95 et plus"]
graph49 = px.pie(values=[TRANCHE9, 1 - TRANCHE9], title="96 ans et plus")

# ____________________________________________GRAPH5____________________________________________

# récupération de la liste des prénoms féminin les plus donné par tranche d'age

grouped = df[df['SEXE'] == 2].groupby(['TRANCHE_AGE', 'PREMIER_PRENOM'])['PREMIER_PRENOM'].count().reset_index(
    name='COUNT')
PF_AGE = grouped.groupby('TRANCHE_AGE').apply(lambda x: x.nlargest(1, 'COUNT')).reset_index(drop=True)
TOP_PRENOM_F = PF_AGE['PREMIER_PRENOM'].tolist()
TOP_PRENOM_F = list(set(TOP_PRENOM_F))

# récupération de la liste des prénoms masculin les plus donnés

grouped = df[df['SEXE'] == 1].groupby(['TRANCHE_AGE', 'PREMIER_PRENOM'])['PREMIER_PRENOM'].count().reset_index(
    name='COUNT')
PM_PAR_AGE = grouped.groupby('TRANCHE_AGE').apply(lambda x: x.nlargest(1, 'COUNT')).reset_index(drop=True)
TOP_PRENOM_M = PM_PAR_AGE['PREMIER_PRENOM'].tolist()
TOP_PRENOM_M = list(set(TOP_PRENOM_M))

TOP_PRENOM = TOP_PRENOM_M + TOP_PRENOM_F

# initialisation du graph 5

FILTRE = df[df['PREMIER_PRENOM'].isin(TOP_PRENOM)]
grouped = FILTRE.groupby(['ANNEE', 'PREMIER_PRENOM'])['PREMIER_PRENOM'].count().reset_index(name='COUNT')
graph51 = px.line(grouped, x='ANNEE', y='COUNT', color='PREMIER_PRENOM',
                  labels={'COUNT': 'Occurrence'})

graph52 = px.line(grouped, x='ANNEE', y='COUNT', color='PREMIER_PRENOM',
                  title='Évolution des Prénoms les Plus Récurrents à Travers les Années',
                  labels={'COUNT': 'Occurrence'})
graph52 = graph52.update_xaxes(range=[1970, 2024])
graph52 = graph52.update_yaxes(range=[0, 25])

# _____________________________________________GRAPH6__________________________________________

france_map = 'https://france-geojson.gregoiredavid.fr/repo/regions.geojson'

DF_REGION = df.groupby('CODE_REGION_M')['INDICE'].count().reset_index()

graph6 = px.choropleth(
    DF_REGION,
    geojson=france_map,
    locations='CODE_REGION_M',
    featureidkey="properties.code",
    color='INDICE',
    color_continuous_scale=px.colors.sequential.Plasma,
)

graph6.update_geos(
    center={"lat": 46.603354, "lon": 1.888334},
    scope="europe",
)

# ________________________________________________GRAPH7___________________________________________________

PAYS = df.dropna(subset=['PAYS_N'])

top_countries = PAYS[~PAYS['PAYS_N'].isin(['MARTINIQUE', 'GUADELOUPE', 'LA REUNION'])]['PAYS_N'].value_counts().nlargest(12).index
PAYS['PAYS_N'] = PAYS['PAYS_N'].apply(lambda x: x if x in top_countries else 'Autre')

graph7 = px.pie(PAYS, names='PAYS_N')

# ________________________________________________AFFICHAGE STREAMLIT_________________________________________

# Mise en place d'un menu
st.sidebar.title("Menu")
st.sidebar.write("#dataviz2023")
st.sidebar.markdown("""
[Présentation : ](#presentation)\n
[Graph n°1 : répartition selon l'age et le sexe ](#graph1)\n
[Graph n°2 : répartition des naissances et décès selon la région ](#graph2)\n
[Carte de france : répartition des décès ](#graph3)\n
[Graph n°4 : les Français reste il dans la même région ? ](#graph4)\n
[Graph n°5 : évolution des prénoms à travers les âges ](#graph5)\n
[Graph n°6 : évolution du nombre de prénoms ](#graph6)\n
[Graph n°7 : où sont nés ceux qui viennent en France ? ](#graph7)\n
""")

st.sidebar.write("Par Victoria Guez")

# initialisation de streamlit et test en display
st.markdown('<a id="presentation"></a>', unsafe_allow_html=True)
st.title("Etude de l'évolution des habitudes et des moeurs des Français")
st.header("Ou plutôt, où fait-il bon de naître et de mourir en France ?")


st.write("Cette étude est basée sur 147 000 décès en France en 2023. \n "
             "nous avons pour chacun les informations suivantes :\n "
             "- date de naissance \n"
             "- date de mort\n"
             "- code postale du lieu de naissance \n"
             "- code postale du lieu de décès\n"
             "- Nom et Prénoms\n"
             "- sexe\n"
             "- ville de naissance\n"
             "- pays si différent de la France\n ")
st.write("C'est grâce à ces éléments que vous pouvez découvrir aujourd'hui notre études :"
         " Comment ont évolué les vies des Français depuis 100 ans  ?")

# display des différents graph :
st.markdown('<a id="graph1"></a>', unsafe_allow_html=True)
st.header("Ce graphique présente la répartition des décès par tranche d'âge en fonction du sexe")
st.pyplot(graph1)

st.markdown('<a id="graph2"></a>', unsafe_allow_html=True)
st.header("Ce graphique représente la répartition des décès et des naissances en fonction des régions ")
st.plotly_chart(graph2)

st.markdown('<a id="graph6"></a>', unsafe_allow_html=True)

st.header("Cette carte de France montre la répartition des décès en fonction des régions")
st.write("le focus étant mis sur Paris il suffit d'appuyer sur zoom pour n'avoir que la france dans le cadre ")
st.plotly_chart(graph6)



st.markdown('<a id="graph4"></a>', unsafe_allow_html=True)
st.header("Ces graphiques repésentent la part de personnes étant nés et décédés dans la même région ")
st.write("le premier graphique repésente la part générale puis les 9 petits la part pour chacune des tranches d'âge")
st.plotly_chart(graph4)
col1, col2, col3 = st.columns(3)
with col1:
    st.plotly_chart(graph41, use_container_width=True)
    pass

with col2:
    st.plotly_chart(graph42, use_container_width=True)
    pass

with col3:
    st.plotly_chart(graph43, use_container_width=True)
    pass

with col1:
    st.plotly_chart(graph44, use_container_width=True)
    pass

with col2:
    st.plotly_chart(graph45, use_container_width=True)
    pass

with col3:
    st.plotly_chart(graph46, use_container_width=True)
    pass
with col1:
    st.plotly_chart(graph47, use_container_width=True)
    pass

with col2:
    st.plotly_chart(graph48, use_container_width=True)
    pass

with col3:
    st.plotly_chart(graph49, use_container_width=True)
    pass

st.markdown('<a id="graph5"></a>', unsafe_allow_html=True)

st.header("Ces graphiques repésentent les prénoms les plus donnés selon les années")
st.write("nous avons d'abord selectionné le prénom le plus récurrent pour chaque tranche d'âge puis sa répartition entre 1900 et 2023"
             "\n nous avons également fais un zoom entre 1970 et 2023 pour plus de clarté dans les résultats")
st.plotly_chart(graph51)
st.plotly_chart(graph52)

st.markdown('<a id="graph3"></a>', unsafe_allow_html=True)
st.header("Ce graphique représente  le nombre de prénom selon l'âge ")
st.plotly_chart(graph3)

st.markdown('<a id="graph7"></a>', unsafe_allow_html=True)
st.header("Ce diagramme en cercle montre les pays d'origine des personnes décédées en France mais né hors de France")
st.plotly_chart(graph7)

