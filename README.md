
# Instruções

Para executar esse projeto localmente é necessário ter instalados os pacotes:
 - docker
 - docker-compose

Depois de clonado o repositório, o comando ``` docker-compose up -d ``` deve ser executado dentro da pasta, assim que a instalação terminar a aplicação estará rodando na porta 3000 do localhost.

É importante notar que a aplicação só funcionará se o serviço no browser for executado na mesma máquina em que os containers estão rodando.

  ---

Nessa aplicação foram usadas três principais tecnologias:

  

**Docker:**

O Docker foi utilizado para facilitar a execução do projeto, já que com ele o projeto é carregado com um único comando.

Além disso ao utilizar o  Docker é possível garantir que todos os pacotes necessários serão instalados, sem que o usuário tenha que fazer isso manualmente.
  

**Flask:**

O Flask foi utilizado como a API pois é uma ferramenta com a qual tenho mais familiaridade.

A API recebe uma chamada POST com o número, calcula o primeiro número duodígito em seus múltiplos e retorna o número e o tempo decorrido no cálculo.


**Angular:**

O Angular foi utilizado como o front-end da aplicação já que não tinha familiaridade com nenhuma tecnologia do tipo e esse foi o recomendado para esta tarefa.

Na criação do container com a aplicação primeiro são copiados os arquivos para o container, então é feito o build e o resultado é servido pelo Nginx.

É importante notar que a aplicação aceita como entrada qualquer número real com os decimais separados por ponto, e que com números grandes ou com muitos decimais tende a ter tempos de resposta mais altos, na casa das dezenas de segundos.