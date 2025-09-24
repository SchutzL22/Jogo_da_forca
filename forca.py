# Trabalho 1 - Jogo da forca
# Nome do Estudante: Lucas Alexandre Vieira Schutz

import random
import string
import os
import time

ARQUIVO_LISTA_PALAVRAS = "palavras.txt"
# ARQUIVO_LISTA_PALAVRAS = os.path.join(os.path.dirname(__file__), "palavras.txt")
# Linha acima para caso de erro ao carregar
# Deu erro no meu, porque abri num arquivo com todos os meus projetos em pastas separadas
# Este codigo faz procurar na pasta específica onde está sendo rodado o arquivo

def carregar_palavras():
    """
    SAÍDA: lista, uma lista de palavras válidas.  As palavras
    são strings em letra minúscula.

    Dependendo do tamanho da lista de palavras, esta função pode
    demorar um pouco para terminar.
    """
    print("Carregando lista de palavras de arquivo...")
    noArquivo = open(ARQUIVO_LISTA_PALAVRAS, 'r')
    linha = noArquivo.readline()
    lista_de_palavras = linha.split()
    print(" ", len(lista_de_palavras), "palavras carregadas.")
    return lista_de_palavras

def escolhe_palavra(lista_de_palavras):
    """
    ENTRADA: 'lista_de_palavras': uma lista de palavras (strings)
    SAÍDA: Uma palavra escolhida da lista
    """
    return random.choice(lista_de_palavras)

lista_de_palavras = carregar_palavras()

def jogador_venceu(palavra_secreta, letras_escolhidas):
    """
    ENTRADA: 'palavra_secreta', uma string em letras minúsculas que o usuário
             deve adivinhar
             'letras_escolhidas': lista de letras minúsculas que o jogador
             escolheu até agora para adivinhar a palavra
    SAÍDA: True, se todas as letras de 'palavra_secreta' estão em 
           'letras_escolhidas' e False caso contrário
    """
    for letra in palavra_secreta:
        if letra not in letras_escolhidas:
            return False
    return True


def progresso_atual_da_palavra(palavra_secreta, letras_escolhidas):
    """
    ENTRADA: 'palavra_secreta', string em letra minúscula que usuário está
             adivinhando.
             'letras_escolhidas', uma lista de letras minúsculas que o jogador
             escolheu até agora
    SAÍDA: Uma string formada por letras e asteriscos (*) que representam letras
           na palavra secreta que ainda não foram adivinhadas
    """
    resultado = ""
    for letra in palavra_secreta:
        if letra in letras_escolhidas:
            resultado += letra
        else:
            resultado += "*"
    return resultado


def letras_ainda_disponiveis(letras_escolhidas):
    """
    ENTRADA: 'letras_escolhidas', lista de letras minúsculas que o usuário
             escolheu até agora.
    SAÍDA: Uma string formada por todas as letras que ainda não foram escolhidas.
           As letras devem ser retornadas em ordem alfabética.
    """
    alfabeto = "abcdefghijklmnopqrstuvwxyz"
    disponiveis = ""
    for letra in alfabeto:
        if letra not in letras_escolhidas:
            disponiveis += letra
    return disponiveis


def forca(palavra_secreta, com_ajuda):
    """
    ENTRADA: 'palavra_secreta', uma string representando uma palavra a ser
             adivinhada
             'com_ajuda', um valor booleano que ativa a funcionalidade de ajuda
             se verdadeiro

    Isso inicia um jogo interativo de Forca.

    * No começo do jogo, deixe o usuário saber quantas letras
      a string 'palavra_secreta' contém e quantas tentativas ele tem de
      escolher letras.

    * O usuário deve começar com 10 tentativas.

    * Antes de cada rodada, você deve mostrar ao usuário quantas tentativas
      ele ainda tem  e as letras que ele ainda não escolheu.

    * Peça ao usuário para escolher uma letra por rodada. Lembre-se de
      checar se o usuário realmente está inserindo uma só letra (ou
      o caractere de ajuda  '!' se a funcionalidade de ajuda está ativa)

    * Se o usuário escolher uma consoante incorreta, ele perde UMA tentativa,
      mas se ele escolher uma vogal incorreta (a, e, i, o, u),
      então ele perde DUAS tentativas.

    * O usuário deve receber informações imediatamente
      após cada tentativa de escolher uma letra para que ele saiba
      se a letra escolhida aparece na palavra secreta.

    * Depois de cada escolha, você deve mostrar ao usuário a palavra
      parcialmente adivinhada até agora.

    -----------------------------------
    A funcionalidade 'com_ajuda' 
    -----------------------------------
    * Se a escolha for o símbolo !, você deve revelar ao usuário uma das letras
      faltantes da palavra ao custo de 3 tentativas. Se o usuário não tem
      3 tentativas restantes, imprima uma mensagem de aviso. Do contrário,
      adicione esta letra à lista de letras adivinhadas e continue jogando
      normalmente.
    """
    tentativas = 10
    letras_escolhidas = []

    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')
    print("🎉 Bem-vindo ao jogo da Forca! 🎉")
    print(f"A palavra secreta tem {len(palavra_secreta)} letras.")
    time.sleep(2)
    os.system('cls' if os.name == 'nt' else 'clear')

    while tentativas > 0 and not jogador_venceu(palavra_secreta, letras_escolhidas):
        print(f"\nTentativas restantes: {tentativas}")
        print("Letras disponíveis:", letras_ainda_disponiveis(letras_escolhidas))
        print("Palavra:", progresso_atual_da_palavra(palavra_secreta, letras_escolhidas))

        chute = input("Digite uma letra (ou '!' para ajuda): ").lower()

        if chute == "!" and com_ajuda:
            if tentativas < 3:
                print("😢 Você não tem tentativas suficientes para usar ajuda!")
            else:
                faltando = [l for l in palavra_secreta if l not in letras_escolhidas]
                if faltando:
                    letra_revelada = random.choice(faltando)
                    letras_escolhidas.append(letra_revelada)
                    tentativas -= 3
                    print(f"🆘 Ajuda usada! -3 tentativas! A letra '{letra_revelada}' foi revelada.")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')

        if len(chute) != 1 or chute not in "abcdefghijklmnopqrstuvwxyz!":
            print("❌ Digite apenas uma letra do alfabeto!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        if chute in letras_escolhidas:
            print("⚠️ Você já tentou essa letra!")
            time.sleep(2)
            os.system('cls' if os.name == 'nt' else 'clear')
            continue

        letras_escolhidas.append(chute)

        if chute in palavra_secreta:
            print(f"✅ Boa! A letra '{chute}' está na palavra.")
        elif chute == "!":
            continue
        else:
            if chute in "aeiou":
                tentativas -= 2
                print(f"❌ Ahh, '{chute}' não está na palavra! -2 tentativas!")
            else:
                tentativas -= 1
                print(f"❌ Ahh, '{chute}' não está na palavra! -1 tentativa!")

        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')

    if jogador_venceu(palavra_secreta, letras_escolhidas):
        pontos = calcular_pontuacao(tentativas, palavra_secreta)
        print(f"🎉 Parabéns! Você venceu! A palavra era: {palavra_secreta} 😎")
        print(f"🏆 Sua pontuação foi: {pontos}")
        print(f"Você usou {tentativas} tentativas!")
    else:   
        print(f"😢 Você perdeu! A palavra era: {palavra_secreta}")
        print("🏆 Sua pontuação foi: 0")
        print(f"Você usou {tentativas} tentativas!")



def calcular_pontuacao(tentativas, palavra_secreta):
    if tentativas <= 0:
        return 0
    letras_distintas = len(set(palavra_secreta))
    return tentativas + 4 * letras_distintas + 3 * len(palavra_secreta)


if __name__ == "__main__":
    palavra_secreta = escolhe_palavra(lista_de_palavras)
    com_ajuda = True
    forca(palavra_secreta, com_ajuda)