{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "py_2.py",
      "provenance": [],
      "authorship_tag": "ABX9TyPkjIs3cyxJ6PDwwkaZZkIn",
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
        "<a href=\"https://colab.research.google.com/github/sahooaditya/ADITYA/blob/master/py_2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 120
        },
        "id": "I1FSEGF0SwUb",
        "outputId": "8825df72-d0a9-4969-b729-6f58517a0061"
      },
      "source": [
        "divisor, divident = 2, 1\n",
        "ans = divident / divisor\n",
        "print(ans)\n",
        "a, b, c, d = 2, 3, 4, 5\n",
        "\n",
        "ans = a + b * c / d\n",
        "print(ans)\n",
        "\n",
        "# ** is power\n",
        "exp = a ** b\n",
        "print(exp)\n",
        "\n",
        "mod = b % a\n",
        "print(mod)\n",
        "\n",
        "# // returns integer division result\n",
        "intDiv = d // a\n",
        "# / returns float division result\n",
        "div = d / a\n",
        "print(div, intDiv)\n",
        "\n",
        "\n",
        "'''\n",
        "PEMDAS\n",
        "Parentheses\n",
        "Exponents\n",
        "Multiplication\n",
        "Division\n",
        "Addition\n",
        "Subtraction\n",
        "'''"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "text": [
            "0.5\n",
            "4.4\n",
            "8\n",
            "1\n",
            "2.5 2\n"
          ],
          "name": "stdout"
        },
        {
          "output_type": "execute_result",
          "data": {
            "application/vnd.google.colaboratory.intrinsic+json": {
              "type": "string"
            },
            "text/plain": [
              "'\\nPEMDAS\\nParentheses\\nExponents\\nMultiplication\\nDivision\\nAddition\\nSubtraction\\n'"
            ]
          },
          "metadata": {
            "tags": []
          },
          "execution_count": 1
        }
      ]
    }
  ]
}