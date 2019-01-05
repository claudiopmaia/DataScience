''' Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
    calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
'''

tamanhoAquivo = float(input('Tamanho do arquivo (MB): '))
velocidadeDownload = float(input('Velocidade de Internet (MBps): '))
print('Tempo aproximadamente para o download: %.0f Minutos ' % ((tamanhoAquivo / velocidadeDownload) * 60))









