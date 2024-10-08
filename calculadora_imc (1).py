# -*- coding: utf-8 -*-
"""CALCULADORA-IMC.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18V7IMh_Ejp42sNw_1THR6axo5GQc4pvA
"""

# Solicitar o peso e a altura do usuário
peso = float(input("Digite seu peso em quilogramas (kg): "))
altura = float(input("Digite sua altura em metros (m): "))

# Calcular o IMC
imc = peso / (altura ** 2)

# Exibir o resultado
print(f"Seu IMC é: {imc:.2f}")

# Interpretar o IMC
if imc < 18.5:
    print("Classificação: Abaixo do peso \n Observamos que você está abaixo do peso ideal. \n Recomendo consultar um especialista em nutrição para obter orientações adequadas e garantir um equilíbrio saudável.")
elif 18.5 <= imc < 24.9:
    print("Classificação: Peso saudável \n Observamos que seu peso está dentro da faixa considerada saudável. \n Para manter o equilíbrio e a saúde, pode ser útil continuar acompanhando sua nutrição com um especialista, se desejar.")
elif 25 <= imc < 29.9:
    print("Classificação: Sobrepeso \n Observamos que você está acima do peso ideal. \n Pode ser benéfico consultar um especialista em nutrição para receber orientações sobre como atingir um equilíbrio saudável.'")
else:
    print("Classificação: Obesidade \n Observamos que você está classificando-se como tendo obesidade. \n Recomendo fortemente consultar um especialista em nutrição e saúde para receber orientações adequadas e desenvolver um plano para alcançar um equilíbrio saudável.'")