from time import sleep
from threading import Thread

# class MinhaThread(Thread):
#     def __init__(self, texto: str, tempo: int) -> None:
#         self._texto = texto
#         self._tempo = tempo
#         super().__init__() # Chamando o init da classe mãe (Thread)

#     def run(self) -> None:
#         sleep(self._tempo)
#         print(self._texto)

# mt = MinhaThread('Minha Thread 1', 3)
# mt.start() # Aqui a execução da thread é disparada e eu prossigo a execução da thread principal.

# for i in range(1,5):
#     print(f'{i=}')
#     sleep(1)

def minhaFuncao(nome: str):
    sleep(3)
    print('Executando ', nome)

minhaThread = Thread(target=minhaFuncao, args=('Thread1',))
minhaThread.start()
minhaThread.join()

# while minhaThread.is_alive():
#     sleep(1)
#     print('Aguardando a thread terminar...')

print('Thread não estrá mais em execução:', minhaThread.is_alive())
# for i in range(1,5):
#     print(f'{i=}')
#     sleep(1)