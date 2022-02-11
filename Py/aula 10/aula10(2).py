
def escrever_texto(texto):
    arquivo=open("Arquivo.txt","w")
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(texto):
    arquivo=open("Arquivo.txt","a")
    arquivo.write(texto)
    arquivo.close()

if __name__=="__main__":
    escrever_texto("Primeira Linha \n")
    atualizar_arquivo("Segunda Linha \n")