import pandas as pd
import os

def main():
    input_path = 'data/Global_Cybersecurity_Threats_2015-2024.csv'
    output_path = 'data/dados_transformados.csv'

    if not os.path.exists(input_path):
        print(f"❌ Arquivo não encontrado: {input_path}")
        return

    try:
        df = pd.read_csv(input_path)

        df = df[
            [
                'Country',
                'Year',
                'Attack Type',
                'Target Industry',
                'Financial Loss (in Million $)',
                'Number of Affected Users',
                'Attack Source',
                'Security Vulnerability Type',
                'Defense Mechanism Used',
                'Incident Resolution Time (in Hours)'
            ]
        ]

        # Renomeando para português
        df.columns = [
            'pais',
            'ano',
            'tipo_ataque',
            'industria_alvo',
            'perda_financeira_milhoes_usd',
            'usuarios_afetados',
            'origem_ataque',
            'tipo_vulnerabilidade',
            'mecanismo_defesa',
            'tempo_resolucao_horas'
        ]

        os.makedirs('data', exist_ok=True)
        df.to_csv(output_path, index=False)
        print(f"✅ Dados transformados e salvos em '{output_path}'")

    except Exception as e:
        print(f"❌ Erro ao processar os dados: {e}")

if __name__ == "__main__":
    main()
