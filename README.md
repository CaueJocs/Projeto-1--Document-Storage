# Projeto-1--Document-Storage

Integrantes: 
Vinicius henrique Silva 22.122.063-5

Luan Petroucic Moreno 22.122.076-7

Caue Jacomini Zanatti 22.122.024-7


# Como convertemos os dados do projeto do semestre passado?

Usamos as bibliotecas do psycopg2 para podermos fazer selects dentro do nosso código de Python "createJson", um arquivo que fará a conversão necessária entre as informações do banco relacional para o banco não relacional.

Todos os JSONs usado para as coleções estão na pasta JSONs, mas caso queira testar como eles foram criados, rodar o arquivo createJson.


# PRÉ-REQUISITOS:

Ter as bibliotecas PSYCOPG2 e PYMONGO instalados


# DESCRIÇÃO DE USO:

1.Abrir a pasta scriptsPython e encontrar o arquivo "criaColeção".

2.Esse arquivo contém a variável URI, que é a conection string para o nosso banco.

Caso queira re-configurar para conectar ao seu proprio banco, trocar {allAccess} para seu usuário, e {P8OxiNrhuJ4YH3bI} para sua senha. Caso opte para seguir com o banco que criamos, apenas retire as chaves que envolvem os dois itens.

3.Execute o arquivo criaColeção

4.Abrir o MONGODB Compass e se conectar no mesmo DB escolhido acima.

5.Verificar que as coleções foram criadas e os dados foram inseridos com os arquivos JSON.

6.Para rodar as queries, abrir o arquivo queries.txt e executa-las no shell do monbodb compass
