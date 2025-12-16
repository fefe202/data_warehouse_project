import pandas as pd

# Dizionario di mappatura stato -> tipo di terreno
mapping = {
    'Alabama': 'rural',
    'Alaska': 'mountainous',
    'Arizona': 'desertic/sandy',
    'Arkansas': 'rural',
    'California': 'mountainous',
    'Colorado': 'mountainous',
    'Connecticut': 'rural',
    'Delaware': 'swampy/wet',
    'Florida': 'swampy/wet',
    'Georgia': 'rural',
    'Hawaii': 'mountainous',
    'Idaho': 'mountainous',
    'Illinois': 'rural',
    'Indiana': 'rural',
    'Iowa': 'rural',
    'Kansas': 'rural',
    'Kentucky': 'rural',
    'Louisiana': 'swampy/wet',
    'Maine': 'rural',
    'Maryland': 'rural',
    'Massachusetts': 'urban',
    'Michigan': 'rural',
    'Minnesota': 'rural',
    'Mississippi': 'rural',
    'Missouri': 'rural',
    'Montana': 'mountainous',
    'Nebraska': 'rural',
    'Nevada': 'desertic/sandy',
    'New Hampshire': 'mountainous',
    'New Jersey': 'urban',
    'New Mexico': 'desertic/sandy',
    'New York': 'rural',
    'North Carolina': 'swampy/wet',
    'North Dakota': 'rural',
    'Ohio': 'rural',
    'Oklahoma': 'rural',
    'Oregon': 'mountainous',
    'Pennsylvania': 'mountainous',
    'Rhode Island': 'urban',
    'South Carolina': 'swampy/wet',
    'South Dakota': 'rural',
    'Tennessee': 'mountainous',
    'Texas': 'rural',
    'Utah': 'mountainous',
    'Vermont': 'mountainous',
    'Virginia': 'rural',
    'Washington': 'mountainous',
    'West Virginia': 'mountainous',
    'Wisconsin': 'rural',
    'Wyoming': 'mountainous',
    'Puerto Rico': 'mountainous'
}

# Legge il CSV di input
df = pd.read_csv('car_prices_grouped_body.csv')

# Aggiunge la colonna type_land basandosi sulla colonna state
df['type_land'] = df['state'].map(mapping)

# Salva il risultato su un nuovo CSV
df.to_csv('car_prices_with_land.csv', index=False)
print("Conversione completata! Il file è stato salvato come 'car_prices_with_land.csv'.")