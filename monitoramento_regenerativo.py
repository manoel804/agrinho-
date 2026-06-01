import numpy as np
import matplotlib.pyplot as plt

# 1. Simulação de dados de uma fazenda em transição regenerativa (12 meses)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
MeseIndex = np.arange(len(meses))

# Indicador 1: Matéria Orgânica do Solo (MOS %) - Aumenta com plantio direto e cobertura
materia_organica = [2.1, 2.2, 2.2, 2.4, 2.5, 2.7, 2.8, 2.9, 3.1, 3.2, 3.4, 3.5]

# Indicador 2: Carbono Retido no Solo (Toneladas por Hectare)
carbono_retido = [12.0, 12.2, 12.5, 13.1, 13.8, 14.2, 15.0, 15.5, 16.2, 17.0, 17.8, 18.5]

# 2. Configuração do gráfico para exportação visual
fig, ax1 = plt.subplots(figsize=(10, 6))

# Configurando o primeiro eixo (Matéria Orgânica - Linha Verde)
color = '#2ca02c'
ax1.set_xlabel('Meses de Monitoramento', fontweight='bold', labelpad=12)
ax1.set_ylabel('Matéria Orgânica do Solo (%)', color=color, fontweight='bold')
linha1 = ax1.plot(meses, materia_organica, color=color, marker='o', linewidth=2.5, label='Matéria Orgânica (%)')
ax1.tick_params(axis='y', labelcolor=color)
ax1.grid(True, linestyle='--', alpha=0.5)

# Criando um segundo eixo Y na mesma tela (Carbono - Barra Azul)
ax2 = ax1.twinx()
color = '#1f77b4'
ax2.set_ylabel('Carbono Retido (Ton/Ha)', color=color, fontweight='bold')
linha2 = ax2.plot(meses, carbono_retido, color=color, marker='s', linestyle='--', linewidth=2, label='Carbono Retido (Ton/Ha)')
ax2.tick_params(axis='y', labelcolor=color)

# Título e layout
plt.title('Evolução dos Indicadores de Agricultura Regenerativa', fontsize=14, fontweight='bold', pad=15)
fig.tight_layout()

# Unificando as legendas dos dois eixos em apenas uma caixa
linhas = linha1 + linha2
legendas = [l.get_label() for l in linhas]
ax1.legend(linhas, legendas, loc='upper left')

# 3. Salva o gráfico em uma pasta local para subir no seu GitHub
# Certifique-se de que a pasta 'imagens' existe ou salve direto na raiz mudando o caminho
try:
    plt.savefig('imagens/grafico_regenerativo.png', dpi=300)
    print("Sucesso! Imagem gerada e salva em 'imagens/grafico_regenerativo.png'")
except FileNotFoundError:
    plt.savefig('grafico_regenerativo.png', dpi=300)
    print("Sucesso! Pasta 'imagens' não encontrada. Imagem salva na raiz como 'grafico_regenerativo.png'")

# Exibe o resultado na tela
plt.show()
