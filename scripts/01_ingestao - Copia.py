import os
import json
import shutil
import pandas as pd
from pathlib import Path

# 1. Configuração manual das credenciais (SOLUÇÃO DEFINITIVA)
KAGGLE_USERNAME = "galvaojdk"  # Substitua pelo seu usuário Kaggle
KAGGLE_KEY = "545542da37e3a308c9f74f127aa6437e"  # Use sua chave atualizada

# 2. Configuração de caminhos
SCRIPT_DIR = Path(__file__).parent
DATA_DIR = SCRIPT_DIR / "data"
DATA_DIR.mkdir(exist_ok=True)

def setup_kaggle():
    """Configura o ambiente Kaggle via variáveis de ambiente"""
    try:
        os.environ["KAGGLE_USERNAME"] = KAGGLE_USERNAME
        os.environ["KAGGLE_KEY"] = KAGGLE_KEY
        return True
    except Exception as e:
        print(f"ERRO na configuração: {str(e)}")
        return False

def download_dataset():
    """Baixa o dataset usando a API Kaggle"""
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi
        api = KaggleApi()
        api.authenticate()
        
        print("\nBaixando dataset...")
        api.dataset_download_files(
            "/kaggle/input/real-estat-sales-2001-2022/Real_Estate_Sales_2001-2022_GL.csv",
            path=DATA_DIR,
            unzip=True,
            force=True
        )
        return True
    except Exception as e:
        print(f"ERRO no download: {str(e)}")
        return False

def load_data():
    """Carrega os dados baixados"""
    try:
        csv_files = list(DATA_DIR.glob("*.csv"))
        if not csv_files:
            print("Nenhum arquivo CSV encontrado em data/")
            return None
            
        print(f"\nArquivos encontrados: {[f.name for f in csv_files]}")
        df = pd.read_csv(csv_files[0])
        print("\n✅ Dados carregados com sucesso!")
        return df
    except Exception as e:
        print(f"ERRO ao carregar dados: {str(e)}")
        return None

if __name__ == "__main__":
    print("=== Iniciando ingestão ===")
    
    # 1. Configuração
    if not setup_kaggle():
        exit(1)
    
    # 2. Download
    if not download_dataset():
        exit(1)
    
    # 3. Carregamento
    df = load_data()
    if df is not None:
        print("\nPrimeiras linhas:")
        print(df.head())