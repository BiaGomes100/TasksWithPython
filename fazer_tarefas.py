import pandas as pd
import pyautogui
import time
from datetime import datetime

# configurações de segurança
pyautogui.PAUSE = 1.0  # pausa de 1 segundo entre cada ação
pyautogui.FAILSAFE = True  # Permite abortar movendo o mouse para canto superior esquerdo

# Dicionário de posições dos ícones
posicoes = {
    'bloco_de_notas': (946, 742),  # Substitua pelas coordenadas do ícone do Bloco de Notas
    'navegador': (770, 746)        # Substitua pelas coordenadas do ícone do navegador
}

def executar_tarefa(tarefa, tipo, dado):
    """
    executa uma única tarefa com base no tipo e dado fornecido
    Retorna True se bem-sucedido, False caso contrário
    """
    try:
        if tipo == 'click':
            x, y = posicoes.get(dado, (0, 0))
            pyautogui.click(x, y)
        elif tipo == 'texto':
            pyautogui.write(dado)
        elif tipo == 'tecla':
            pyautogui.hotkey(*dado.split('+'))
        elif tipo == 'espera':
            time.sleep(float(dado))
        return True
    except Exception as e:
        print(f"Erro ao executar tarefa {tarefa}: {e}")
        return False

def ler_tarefas(arquivo):
    """Lê o arquivo de tarefas e retorna um DataFrame"""
    return pd.read_csv(arquivo)

def gerar_relatorio(tarefas_executadas, nome_arquivo='relatorio.xlsx'):
    """Gera um relatório em Excel com os resultados"""
    df = pd.DataFrame(tarefas_executadas)
    df.to_excel(nome_arquivo, index=False)
    print(f"Relatório gerado: {nome_arquivo}")

def main():
    print("Iniciando automação...")
    
    # ler tarefas do arquivo
    tarefas = ler_tarefas('tasks.csv')
    tarefas_executadas = []
    
    # executar cada tarefa
    for index, row in tarefas.iterrows():
        inicio = datetime.now()
        sucesso = executar_tarefa(row['Tarefa'], row['Tipo'], row['Dado'])
        duracao = (datetime.now() - inicio).total_seconds()
        
        # registrar resultado
        tarefas_executadas.append({
            'Tarefa': row['Tarefa'],
            'Status': 'Sucesso' if sucesso else 'Falha',
            'Tempo (segundos)': round(duracao, 2),
            'Tipo': row['Tipo'],
            'Dado': row['Dado']
        })
        
        print(f"Tarefa: {row['Tarefa']} - Status: {'Sucesso' if sucesso else 'Falha'}")
    
    # gerar relatório
    gerar_relatorio(tarefas_executadas)
    print("Automação concluída!")

if __name__ == "__main__":
    main()