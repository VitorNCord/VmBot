🤖 Automação de Tarefas com Python: Script para Interagir com um Site Específico 🌐

Olá, pessoal! 👋

Recentemente, desenvolvi um script Python que simplifica e agiliza a realização de ajustes de planograma em lojas. Quero compartilhar com vocês os detalhes desse projeto e como ele pode ser útil para outros profissionais.

O Problema: Alterar Itens em Múltiplas Lojas
Ao trabalhar com planogramas de lojas, frequentemente nos deparamos com a necessidade de alterar um item específico em várias unidades. No entanto, o sistema do site que utilizamos não permite colar todos os números de máquina de uma vez. Cada busca de máquina precisa ser feita manualmente, copiando e colando individualmente. Imagine ter que fazer isso para 50 máquinas ou mais! Era um processo demorado e propenso a erros.

A Solução: Nosso Script Automatizado
Para resolver esse problema, criei um script Python que automatiza a interação com o site. Eis como ele funciona:

Configuração do Chrome e do ChromeDriver:
O script configura o Chrome para ser usado com o Selenium, definindo opções como o nível de log e excluindo mensagens de log do DevTools.
O serviço do ChromeDriver é configurado sem logs, garantindo um funcionamento mais eficiente.
Inicialização do Driver do Selenium:
O driver do Selenium é inicializado com as opções configuradas e o serviço do ChromeDriver.
O navegador é aberto e direcionado para a URL específica do site.
Simulação de Processamento:
Utilizamos uma barra de progresso (do pacote tqdm) para simular o processamento.
Um loop é executado 100 vezes, atualizando a barra de progresso e aguardando 0,01 segundo em cada iteração.
Função maquina():
Essa função é o coração do programa.
Ela busca o campo de pesquisa de máquinas no site.
Entra em um loop onde o usuário pode digitar o número da máquina ou outras opções.
Se o usuário digitar ‘2’, o programa sai.
Se o usuário digitar ‘1’, o programa reinicia o processamento.
Caso contrário, o script tenta pesquisar a opção digitada e selecioná-la no site.
Tratamento de Exceções:
O código lida com exceções, como quando o campo de pesquisa não é encontrado ou quando a opção não está visível após uma tentativa.
Ele faz até 3 tentativas para encontrar a opção correta.
Contribuições e Melhorias Futuras
Já fizemos melhorias no script desde sua criação original. Estamos planejando adicionar uma interface amigável para facilitar a interação com os usuários. Além disso, estamos trabalhando em uma função que permitirá alterar pares de vários itens em uma única loja. Isso vai liberar ainda mais tempo para nossa equipe se dedicar a análises e insights valiosos.
