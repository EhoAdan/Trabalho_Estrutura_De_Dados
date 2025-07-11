Grupo:
Adan Samuel Prüss
Marcos André Sant'Anna

Linguagem Python

Projeto de Solução do Problema: Com a intenção de reorganizar seu quadro de funcionários, implementar salários mais justos e considerar a opção de um modelo home office, uma empresa de Florianópolis precisa de uma "Estrutuda de Dados" que receba salário, cargo e cidade de residência de seus funcionários, assim como seus nomes e/ou identificadores únicos. Dessa forma, ela espera conseguir ter uma visão melhor das pessoas que trabalham na empresa.

Escolhemos trabalhar com lista invertida neste trabalho pelo grande motivo de que: Parecia ser o de mais fácil e intuitiva implementação, devido a divisão mais clara entre diretório e o resto da estrutura (não ter que lidar com lista encadeada)

Dividimos o trabalho em:

- Diretório (onde guardamos as chaves com seus índices, ou seja, a nossa lista invertida em si)

- Cadastro (manipulação da tabela, análogo a classe Controller, nosso "dicionário maior")

- Main (Iniciliza, recebe dados, conversa com o usuário, nossos "dicionários menores")

- A escolha da estrutura foi toda feita pensando em como poderíamos otimizar o uso do código com o menor número possível de linhas, tudo sem aumentar excessivamente o número de dicionários que precisaríamos integrar, dessa forma, uma única função que usa uma certa ID poderia ficar sendo repassada do dicionário total/completo para os dicionários menores, como pode ser visto nos comentários dos diretórios.

Demais justificativas e descrições das decisões podem ser encontradas nos comentários acompanhando o código