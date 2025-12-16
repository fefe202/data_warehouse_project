import pandas as pd
import re

# Carica il dataset
file_path = "car_prices.csv"  # Sostituisci con il percorso corretto del file CSV
df = pd.read_csv(file_path)

# Assicurati che le colonne 'make' e 'seller' siano trattate come stringhe e gestisci i valori mancanti
df['make'] = df['make'].fillna("").astype(str)
df['seller'] = df['seller'].fillna("").astype(str)

# Estrai tutte le marche uniche dal dataset, rimuovendo spazi extra e valori vuoti
makes_set = set(make for make in df['make'].str.lower() if make.strip())  # Aggiunge solo marche non vuote

# Stampa il set delle marche
print("Makes Set:")
print(makes_set)  # Mostra tutte le marche uniche nel dataset

# Funzione per classificare il tipo di venditore
def classify_seller(row):
    seller = str(row['seller']).lower()  # Converte il nome del venditore in minuscolo

    # Aggiungi il controllo per i venditori di remarketing
    remarketing_keywords = ["remarketing", "wholesale", "resale", "auction"]
    if any(keyword in seller for keyword in remarketing_keywords):
        return "Remarketing"

    # Se il venditore è una società di leasing/noleggio
    rental_keywords = ["hertz", "avis", "enterprise", "rental", "lease", "leasing","exchange", "fleet"]
    if any(keyword in seller for keyword in rental_keywords):
        return "Rental / Leasing"

    # Controlla se almeno una marca è nel nome del venditore
    for make in makes_set:
        if make in seller:
            return "Official Dealer"
    
    # Se il venditore è una banca o un servizio finanziario
    financial_keywords = ["financial", "bank", "wells fargo", "dealer services", "investment", "finance", "credit"]
    if any(keyword in seller for keyword in financial_keywords):
        return "Bank / Financial"

    # Altrimenti, consideriamolo un rivenditore indipendente
    return "Independent Dealer"

# Applica la funzione a ogni riga
df['seller_type'] = df.apply(classify_seller, axis=1)

# Salva il nuovo dataset con la colonna aggiuntiva
df.to_csv("car_prices_updated.csv", index=False)

# Calcola e stampa la distribuzione percentuale dei tipi di venditori
seller_counts = df['seller_type'].value_counts(normalize=True) * 100

print("Seller Type Distribution (%):")
print(seller_counts.to_string())

print("Classification completed! The file has been saved as 'car_prices_updated.csv'.")
