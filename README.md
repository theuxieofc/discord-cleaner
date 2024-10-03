# discord-cleaner


A ferramenta busca por injeções de código malicioso no arquivo index.js dos módulos principais do Discord. Se encontrar alguma injeção, oferece ao usuário a opção de salvar o arquivo original para revisão.
Após detectar uma injeção, limpa o arquivo restaurando-o ao seu estado normal, removendo efetivamente o conteúdo malicioso.
Depois de limpo, a ferramenta reinicia o aplicativo Discord apropriado para aplicar as mudanças.
Gerenciamento de Processos:

A ferramenta utiliza a biblioteca psutil para encerrar quaisquer instâncias em execução do Discord antes de reiniciar o aplicativo, garantindo que as mudanças tenham efeito corretamente.
Tratamento de Erros:

O código inclui tratamento de erros para vários cenários, como diretórios ou arquivos ausentes, garantindo que o usuário seja informado sobre quaisquer problemas encontrados durante a execução.
Seção de Ajuda:

O menu de ajuda fornece o nome do desenvolvedor e um link do GitHub, além de explicações sobre as principais funcionalidades da ferramenta e um aviso sobre os riscos potenciais associados a versões roubadas.
Funcionalidade Geral:
Esta ferramenta é essencial para usuários preocupados com a segurança de seus aplicativos do Discord. Ao buscar e remover injeções de código malicioso, ajuda a manter um ambiente seguro e protegido para os usuários, garantindo que a experiência no Discord permaneça inalterada.
