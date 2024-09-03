#5) Você está em uma sala com três interruptores, cada um conectado a uma lâmpada em salas diferentes. Você não pode ver as lâmpadas da sala em que está, mas pode ligar e desligar os interruptores quantas vezes quiser. Seu objetivo é descobrir qual interruptor controla qual lâmpada. Como você faria para descobrir, usando apenas duas idas até uma das salas das lâmpadas, qual interruptor controla cada lâmpada?  

# Solução: Utilize as características das lâmpadas (quente e fria) para identificar qual interruptor controla cada uma.

def identificar_interruptores():
    import time

    print("Você está em uma sala com três interruptores (Interruptor 1, Interruptor 2, Interruptor 3).")
    print("Cada interruptor controla uma lâmpada em uma sala separada. Você precisa descobrir qual interruptor controla cada lâmpada.")
    
    # Passo 1: Solicitar que o usuário ligue o primeiro interruptor
    print("\nPasso 1: Ligue o primeiro interruptor (Interruptor 1) e deixe-o ligado por alguns minutos para que a lâmpada aqueça.")
    input("Pressione Enter quando estiver pronto para prosseguir.")

    # Simular o tempo em que a lâmpada fica ligada
    print("\nO primeiro interruptor está ligado e a lâmpada está aquecendo. Aguarde alguns minutos...")
    time.sleep(10)  # Espera de 10 segundos para simular o tempo de aquecimento

    # Solicitar que o usuário desligue o primeiro interruptor e ligue o segundo
    print("\nPasso 2: Desligue o primeiro interruptor e ligue o segundo interruptor (Interruptor 2).")
    input("Pressione Enter quando estiver pronto para ir até as salas das lâmpadas.")

    # Simulação das lâmpadas
    print("\nAgora, vá até as salas das lâmpadas e identifique cada uma delas:")
    print("1. A lâmpada que está acesa corresponde ao Interruptor 2.")
    print("2. A lâmpada que está apagada e quente corresponde ao Interruptor 1.")
    print("3. A lâmpada que está apagada e fria corresponde ao Interruptor 3.")
    
    # Mensagem final
    print("\nVocê pode agora identificar qual interruptor controla cada lâmpada.")
    print("Interruptor 1: lâmpada apagada e quente")
    print("Interruptor 2: lâmpada acesa")
    print("Interruptor 3: lâmpada apagada e fria")

# Chama a função para executar o processo
identificar_interruptores()

