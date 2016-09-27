1) Criar o banco de dados:
        - Cada item é uma questão.
            Cada questão contém um texto (string).
            Cada questão contém um assunto (número de 1-8).
            Cada questão contém um número identificador.
            
        - Número totais de questões: ____
        - Número totais de questões por grupo:
                1: ___
                2: ___
                3: ___
                4: ___
                5: ___
                6: ___
                7: ___
                8: ___
        
2) Separar o banco de dados de acordo com o "k-fold" dado.
   
        Se eu tenho x questões do grupo 1, então eu preciso retirar x%k questões para que eu consiga dividi-lo em k grupos.
        Faço isso para cada um dos grupos.
        Minha parte K é formada por cada parte de um grupo.
        
-----------------------------------------------------

Começando o algoritmo:

Para cada k de k-fold:
    
    Leio minha entrada. Faço uma lista de string, na qual cada string é um documento (texto de uma questão).
    
    Faço a tabela Tf-idf desses documentos e termos.
    
    Faço o SVD da tabela Tf-idf.
    
    Treino o kmeans com cada linha de documento no SVD (No caso, é sigma*UT)
    
    Recebo uma lista de labels do tamanho do número de documentos onde cada index corresponde o grupo do kmeans que aquela questão ficou.
    
    Eu vejo para cada valor do grupo do kmeans, qual assunto de questão é maioria. Então, crio um dicionário que converte o valor do kmeans no grupo real daquelas questões.    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
