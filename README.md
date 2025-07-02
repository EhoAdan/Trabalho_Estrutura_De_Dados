# Trabalho_Estrutura_De_Dados
Aqui temos um trabalho final para a disciplina de estrutura de dados da faculdade.

Segue descrição do trabalho abaixo:

Caros,

Implementação de um esquema de indexação complementar Multilista ou Lista Invertida (vocês escolhem).

A ideia é que vocês identifiquem um problema e implementem a solução usando multilista ou lista invertida, com no mínimo 3 diretórios.

A solução vai ter que oferecer:

uma estrutura (de livre escolha) que mantenha os dados e que permita a busca por identificador único. Os elementos devem ter diversos campos, inclusive 3 que permitam consultas por critérios (como visto em aula, p.ex, matrícula+nome+curso+cidade de origem+time que torce - esses 3 últimos podem ser usados para consultas por critérios). Essa estrutura DEVE SER uma classe, que será instanciada ao menos 1 vez num programa principal. Essa classe deve ter suas operações básicas para manipulação (inserir novo elemento, buscar elemento pelo identificador, excluir elemento pelo identificador)
para fazer a consulta por critérios sobre essa estrutura implementada, será necessário implementar 3 diretórios em 3 campos diferentes (todos os que atendem determinado critério). Desses 3 diretórios, ao menos 1 deve ser de dados contínuos (valores numéricos contínuos, como salário, preço, etc) e os demais, de dados discretos.
Os diretórios DEVEM SER instâncias de uma classe, com suas operações próprias (decidam quais são essas operações e documentem - a escolha vai ser avaliada). Então, para indexar 3 campos, essa classe diretório deve ser instanciada 3 vezes. PERCEBAM QUE os diretórios NÃO SÃO ATRIBUTOS da classe criada no item 1. Eles são 'responsabilidade' do programa principal, objetos controlados pelo programa, assim como o objeto instanciado a partir da classe do item 1.
PERCEBER também que o diretório para 'dados contínuos' tem característica diferente do diretório para dados discretos
Oferecer a consulta simples nesses 3 diretórios E TAMBÉM oferecer consultas combinadas (A e B), (A e C) e (B e C). Ou seja, o programa deverá indexar, no mínimo 3 colunas de dados do conjunto, oferecendo consulta simples a partir das 3 colunas bem como consulta composta por 2 das colunas.
Exemplos de consulta simples: todos os torcedores do Figueirense; todos os estudantes oriundos de Criciúma, etc.
Exemplo de consulta composta: torcedores do Figueirense que são oriundos de Criciúma.

A solução do problema deverá ter uma opção de "carga de dados", em que um conjunto prévio de dados será introduzido na estrutura de dados escolhida, bem como uma opção para inclusão de novos dados pelo usuário (ou seja, eu).

O usuário deve poder executar as seguintes operações:

carga de dados (pode ser uma série de comandos de inclusão, pré-definidos no próprio código ou ler alguma coisa do disco)
consulta simples -> escolha de uma coluna de dados e especificação de um valor para busca -> com exibição do resultado da busca (exemplo: escolha da coluna Times, seguido da especificação do time "Figueirense")
consulta composta -> especificação de dois valores para a busca -> com exibição do resultado da busca
inclusão de novo elemento
busca de elemento (a partir de seu identificador)
remoção de elemento existente (a partir de seu identificador)
exibir todos os dados
Essas operações serão feitas a partir de uma interface com menus - texto ou gráfica, não importa

Outras orientações para o trabalho:

- deve ser implementado por uma equipe de até 2 integrantes
- deve ser implementado em uma linguagem de programação de alto nível, obedecendo preceitos de boa programação e de orientação a objetos
- deve ser entregue funcionando e com todos os arquivos necessários para a avaliação do professor quanto ao funcionamento, permitindo que seja compilado/executado em ambiente padrão
- deve ser acompanhado por documentação que apresente, no mínimo: o projeto de solução do problema e as decisões de projeto ("escolhemos usar multilista porque blablabla", "dividimos em 3 classes x, y e z porque assim blebleblé"...), a modularização adotada. As decisões devem ser descritas, e também justificadas/defendidas.
Para entregar, coloquem tudo em um único arquivo .ZIP ou equivalente e submetam aqui pelo moodle.
