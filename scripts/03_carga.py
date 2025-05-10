import pandas as pd
import sqlite3

def main():
    df = pd.read_csv('data/dados_transformados.csv')

    conn = sqlite3.connect('data/insidentes.db')
    df.to_sql('insidentes', conn, if_exists='replace', index=False)
    conn.close()

    print("✅ Dados carregados no banco 'data/insidentes.db' na tabela 'insidentes'")

if __name__ == "__main__":
    main()
