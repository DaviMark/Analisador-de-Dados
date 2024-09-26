from flask import Flask, request, jsonify, render_template
import pandas as pd

app = Flask(__name__)

file_path = 'banco/BaseFuncionarios.xlsx'

# Funções para responder às perguntas
def carregar_dados():
    return pd.read_excel(file_path)

def contar_linhas():
    df = carregar_dados()
    return len(df)

def contar_colunas():
    df = carregar_dados()
    return df.shape[1], df.columns.tolist()

def estado_civil():
    df = carregar_dados()
    return df['Estado_Civil'].value_counts().to_dict()

def sexo():
    df = carregar_dados()
    return df['Sexo'].value_counts().to_dict()

def data_contrato():
    df = carregar_dados()
    df['Data_de_contrato'] = pd.to_datetime(df['Data_de_contrato'])
    mais_curta = df.loc[df['Data_de_contrato'].idxmin()]
    mais_longa = df.loc[df['Data_de_contrato'].idxmax()]
    media = df['Data_de_contrato'].mean()

    return {
        "mais_curta": (mais_curta['Nome_completo'], mais_curta['Data_de_contrato']),
        "mais_longa": (mais_longa['Nome_completo'], mais_longa['Data_de_contrato']),
        "media": media
    }

def data_demissao():
    df = carregar_dados()
    df['Data_de_demissao'] = pd.to_datetime(df['Data_de_demissao'])
    demissoes = df[['Nome_completo', 'Data_de_demissao']].dropna()
    return demissoes

def salario_base():
    df = carregar_dados()
    salario_max = df.loc[df['Salario_Base'].idxmax()]
    salario_min = df.loc[df['Salario_Base'].idxmin()]
    media = df['Salario_Base'].mean()

    return {
        "maximo": (salario_max['Nome_completo'], salario_max['Salario_Base']),
        "minimo": (salario_min['Nome_completo'], salario_min['Salario_Base']),
        "media": media
    }

def nivel():
    df = carregar_dados()
    return df['Nível'].value_counts().to_dict()

def area():
    df = carregar_dados()
    return df['Área'].value_counts().to_dict()

def avaliacao_funcionario():
    df = carregar_dados()
    avaliacao_max = df.loc[df['Avaliação_do_Funcionario'].idxmax()]
    avaliacao_min = df.loc[df['Avaliação_do_Funcionario'].idxmin()]
    media = df['Avaliação_do_Funcionario'].mean()

    return {
        "maxima": (avaliacao_max['Nome_completo'], avaliacao_max['Avaliação_do_Funcionario']),
        "minima": (avaliacao_min['Nome_completo'], avaliacao_min['Avaliação_do_Funcionario']),
        "media": media
    }

def beneficios():
    df = carregar_dados()
    beneficio_max = df.loc[df['Beneficios'].idxmax()]
    beneficio_min = df.loc[df['Beneficios'].idxmin()]

    return {
        "maximo": (beneficio_max['Nome_completo'], beneficio_max['Beneficios']),
        "minimo": (beneficio_min['Nome_completo'], beneficio_min['Beneficios'])
    }

def vt():
    df = carregar_dados()
    vt_max = df.loc[df['VT'].idxmax()]
    vt_min = df.loc[df['VT'].idxmin()]

    return {
        "maximo": (vt_max['Nome_completo'], vt_max['VT']),
        "minimo": (vt_min['Nome_completo'], vt_min['VT'])
    }

def vr():
    df = carregar_dados()
    vr_max = df.loc[df['VR'].idxmax()]
    vr_min = df.loc[df['VR'].idxmin()]

    return {
        "maximo": (vr_max['Nome_completo'], vr_max['VR']),
        "minimo": (vr_min['Nome_completo'], vr_min['VR'])
    }

# Função principal para receber perguntas
def responder_pergunta(pergunta):
    pergunta = pergunta.lower()

    if "quantas linhas tem" in pergunta:
        return f"O arquivo tem {contar_linhas()} linhas."
    elif "quantas colunas tem" in pergunta:
        colunas_count, colunas = contar_colunas()
        return f"O arquivo tem {colunas_count} colunas: {', '.join(colunas)}."
    elif "qual o estado civil dos funcionarios" in pergunta:
        estado = estado_civil()
        return f"O estado civil das pessoas: {estado}."
    elif "qual o sexo dos funcionarios" in pergunta:
        sexo_info = sexo()
        return f"O sexo das pessoas: {sexo_info}."
    elif "quais sao as datas de contratos" in pergunta:
        contratos = data_contrato()
        return (f"A data de contrato mais curta é de {contratos['mais_curta'][0]}: {contratos['mais_curta'][1].date()}. "
                f"A data de contrato mais longa é de {contratos['mais_longa'][0]}: {contratos['mais_longa'][1].date()}. "
                f"A média das datas de contrato é {contratos['media'].date()}.")
    elif "quais sao as datas de demissoes" in pergunta:
        demissoes = data_demissao()
        return f"Data de demissão das pessoas:\n{demissoes.to_string(index=False)}"
    elif "quais sao os salarios" in pergunta:
        salarios = salario_base()
        return (f"O salário base mais alto é de {salarios['maximo'][0]}: R$ {salarios['maximo'][1]:.2f}. "
                f"O salário base mais baixo é de {salarios['minimo'][0]}: R$ {salarios['minimo'][1]:.2f}. "
                f"A média dos salários base é R$ {salarios['media']:.2f}.")
    elif "quais os niveis dos funcionarios" in pergunta:
        niveis = nivel()
        return f"O nível das pessoas: {niveis}."
    elif "quais as areas do funcionarios" in pergunta:
        areas = area()
        return f"A área das pessoas: {areas}."
    elif "quais sao as avaliacoes dos funcionarios" in pergunta:
        avaliacoes = avaliacao_funcionario()
        return (f"A avaliação do funcionário mais alta é de {avaliacoes['maxima'][0]}: {avaliacoes['maxima'][1]}. "
                f"A avaliação do funcionário mais baixa é de {avaliacoes['minima'][0]}: {avaliacoes['minima'][1]}. "
                f"A média das avaliações é {avaliacoes['media']:.2f}.")
    elif "quais sao os beneficios" in pergunta:
        beneficios_info = beneficios()
        return (f"O maior benefício é de {beneficios_info['maximo'][0]}: R$ {beneficios_info['maximo'][1]:.2f}. "
                f"O menor benefício é de {beneficios_info['minimo'][0]}: R$ {beneficios_info['minimo'][1]:.2f}.")
    elif "quais sao os vt" in pergunta:
        vt_info = vt()
        return (f"O maior VT é de {vt_info['maximo'][0]}: R$ {vt_info['maximo'][1]:.2f}. "
                f"O menor VT é de {vt_info['minimo'][0]}: R$ {vt_info['minimo'][1]:.2f}.")
    elif "quais sao os vr" in pergunta:
        vr_info = vr()
        return (f"O maior VR é de {vr_info['maximo'][0]}: R$ {vr_info['maximo'][1]:.2f}. "
                f"O menor VR é de {vr_info['minimo'][0]}: R$ {vr_info['minimo'][1]:.2f}.")
    else:
        return "Desculpe, não consigo responder a essa pergunta."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data['question']
    answer = responder_pergunta(question)  # Chame sua função de resposta
    return jsonify({"answer": answer})

if __name__ == '__main__':
    app.run(debug=True)
