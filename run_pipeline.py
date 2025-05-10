# run_pipeline.py

import subprocess

def run_pipeline():
    print("🚀 Iniciando execução do pipeline...")

    subprocess.run(["python3", "scripts/01_ingestao.py"], check=True)
    subprocess.run(["python3", "scripts/02_transformacao.py"], check=True)
    subprocess.run(["python3", "scripts/03_carga.py"], check=True)
    subprocess.run(["python3", "scripts/04_consumo.py"], check=True)

    print("🏁 Pipeline executado com sucesso!")

if __name__ == "__main__":
    run_pipeline()