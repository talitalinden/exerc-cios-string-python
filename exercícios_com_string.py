{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "collapsed_sections": [],
      "authorship_tag": "ABX9TyMZuBlzrOnZ0C0jvc7k7ZV6",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/talitalinden/exerc-cios-string-python/blob/main/exerc%C3%ADcios_com_string.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 3,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FTCWPgOJTpgh",
        "outputId": "11677692-c8bf-4d15-eb0d-cbc9dc446f8f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite a primeira frase: Domingo à tarde\n",
            "Digite a segunda frase: Descanso de domingo\n",
            "Tamanho de Domingo à tarde :  15 caracteres\n",
            "O tamanho de Descanso de domingo : 19 caracteres\n",
            "As duas frases tem tamanhos diferentes.\n"
          ]
        }
      ],
      "source": [
        "#Faça um programa que leia 2 strings e informe o conteúdo delas seguido do seu comprimento. \n",
        "#Informe também se as duas strings possuem o mesmo comprimento e são iguais ou diferentes no conteúdo.\n",
        "\n",
        "    #Compara duas strings\n",
        "    #String 1: Brasil Hexa 2006\n",
        "    #String 2: Brasil! Hexa 2006!\n",
        "    #Tamanho de \"Brasil Hexa 2006\": 16 caracteres\n",
        "    #Tamanho de \"Brasil! Hexa 2006!\": 18 caracteres\n",
        "    #As duas strings são de tamanhos diferentes.\n",
        "    #As duas strings possuem conteúdo diferente.\n",
        "\n",
        "string1 = str(input(\"Digite a primeira frase: \"))\n",
        "string2 = str(input(\"Digite a segunda frase: \"))\n",
        "\n",
        "print(\"Tamanho de\", string1, \": \", len(string1), \"caracteres\")\n",
        "print(\"O tamanho de\", string2, \":\", len(string2), \"caracteres\")\n",
        "\n",
        "if len(string1) == len(string2): #len calcula o comprimento\n",
        "    print(\"As duas frases são de tamanhos iguais.\")\n",
        "else:\n",
        "    print(\"As duas frases tem tamanhos diferentes.\")"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Faça um programa que permita ao usuário digitar o seu nome e em seguida mostre o nome do usuário de trás para frente utilizando \n",
        "#somente letras maiúsculas. Dica: lembre−se que ao informar o nome o usuário pode digitar letras maiúsculas ou minúsculas. \n",
        "\n",
        "nome_do_usuario = str(input(\"Digite o seu nome: \"))\n",
        "\n",
        "print(nome_do_usuario.upper() [: :-1])"
      ],
      "metadata": {
        "id": "_c_3gLHdTzjd",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "52a670ca-979b-484a-9926-b27c542e7435"
      },
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome: Talita Hanna Cabral\n",
            "LARBAC ANNAH ATILAT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical. \n",
        "\n",
        "nome = str(input(\"Digite o seu nome: \"))\n",
        "for i in nome:\n",
        "    print(str.upper(i))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "QR-sGL_j90ci",
        "outputId": "c5119751-1f5a-4272-993e-48ab1fad7345"
      },
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome: Talita Hanna\n",
            "T\n",
            "A\n",
            "L\n",
            "I\n",
            "T\n",
            "A\n",
            " \n",
            "H\n",
            "A\n",
            "N\n",
            "N\n",
            "A\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Nome na vertical em escada. Modifique o programa anterior de forma a mostrar o nome em formato de escada. \n",
        "\n",
        "nome = str(input(\"Digite o seu nome: \")).upper()\n",
        "for i in range(0, len(nome)+1):\n",
        "    print(nome[i:])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "wAo5eqUBHK1d",
        "outputId": "3cdd4f37-4f64-4039-c54a-2cd2ddef6272"
      },
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome: Talita Hanna\n",
            "TALITA HANNA\n",
            "ALITA HANNA\n",
            "LITA HANNA\n",
            "ITA HANNA\n",
            "TA HANNA\n",
            "A HANNA\n",
            " HANNA\n",
            "HANNA\n",
            "ANNA\n",
            "NNA\n",
            "NA\n",
            "A\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Nome na vertical em escada invertida. Altere o programa anterior de modo que a escada seja invertida. \n",
        "\n",
        "nome = str(input(\"Digite o seu nome: \")).upper()\n",
        "for i in range(0, len(nome)+1):\n",
        "    print(nome[i: :-1])"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "27wm05xTJEgF",
        "outputId": "5b1352a5-c26c-4363-9dc3-8dc0725aef86"
      },
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Digite o seu nome: Talita Hanna\n",
            "T\n",
            "AT\n",
            "LAT\n",
            "ILAT\n",
            "TILAT\n",
            "ATILAT\n",
            " ATILAT\n",
            "H ATILAT\n",
            "AH ATILAT\n",
            "NAH ATILAT\n",
            "NNAH ATILAT\n",
            "ANNAH ATILAT\n",
            "ANNAH ATILAT\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. \n",
        "\n",
        "data = int(input(\"Digite a sua data de nascimento: \"))\n",
        "mes = str"
      ],
      "metadata": {
        "id": "WAG4bDDMLLWE"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}