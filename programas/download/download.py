# coding: utf-8
import io
import sys
import urllib.request as request
#para executar rodar no terminal:
#python download.py http://livropython.com.br/dados.zip

#download de dados da Copa 2014

#Download de arquivo de tamanho conhecido
BUFF_SIZE = 1024
def download_length(response, output, length):
    times = length // BUFF_SIZE
    if length % BUFF_SIZE > 0:
        times += 1
    for time in range(times):
        output.write(response.read(BUFF_SIZE))
        print("Downloaded %d" % (((time * BUFF_SIZE)/length)*100))

#Como dito anteriormente, às vezes o servidor não responde o tamanho
#em bytes do arquivo que queremos. Nesses casos, realizamos leituras até que
#alguma não retorne nenhum byte. Basicamente, trocamos o loop com for
#e range() por um loop com while, visto que não conseguimos saber de
#antemão quando terminar. Quando a leitura não retorna nada, o comando
#break interrompe o while.

def download(response, output):
    total_downloaded = 0
    while True:
        data = response.read(BUFF_SIZE)
        total_downloaded += len(data)
        if not data:
            break
        output.write(data)
        print('Downloaded {bytes}'.format(bytes=total_downloaded))


def main():
    response = request.urlopen(sys.argv[1])
    out_file = io.FileIO("saida.zip", mode="w")
    content_length = response.getheader('Content-Length')
    if content_length:
        length = int(content_length)
        download_length(response, out_file, length)
    else:
        download(response, out_file)

    response.close()
    out_file.close()
    print("Finished")
if __name__ == "__main__":
    main()

#O que temos agora é um script que faz o download de um arquivo ZIP. De
#acordo com a resposta do servidor, ele opta por uma determinada estratégia
#para download do arquivo.