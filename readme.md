<p align="center">
    <h1 align="center">Projeto Ísis</h1>
    <a href="https://github.com/KillovSky/isis/blob/main/LICENSE"><img alt="GitHub License" src="https://img.shields.io/github/license/KillovSky/Isis?color=blue&label=License&style=flat-square"></a>
    <a href="https://github.com/KillovSky/isis"><img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/KillovSky/isis?label=Size%20%28With%20.git%20folder%29&style=flat-square"></a>
    <a href="https://api.github.com/repos/KillovSky/Isis/languages"><img alt="GitHub Languages" src="https://img.shields.io/github/languages/count/KillovSky/isis?label=Code%20Languages&style=flat-square"></a>
    <a href="https://github.com/KillovSky/Isis/blob/main/.github/CHANGELOG.md"><img alt="GitHub Version" src="https://img.shields.io/github/package-json/v/KillovSky/Isis?label=Latest%20Version&style=flat-square"></a>
    <a href="https://github.com/KillovSky/Isis/blob/main/.github/CHANGELOG.md"><img alt="Project Codename" src="https://img.shields.io/github/package-json/build_name/KillovSky/Isis?label=Latest%20Codename"></a>
    <a href="https://github.com/KillovSky/Isis/blob/main/.github/CHANGELOG.md"><img alt="Last Update" src="https://img.shields.io/github/package-json/build_date/KillovSky/Isis?label=Latest%20Update"></a>
    <a href="https://github.com/KillovSky/isis/commits/main"><img alt="GitHub Commits" src="https://img.shields.io/github/commit-activity/y/KillovSky/isis?label=Commits&style=flat-square"></a>
    <a href="https://github.com/KillovSky/isis/stargazers/"><img title="GitHub Stars" src="https://img.shields.io/github/stars/KillovSky/isis?label=Stars&style=flat-square"></a>
    <a href="https://github.com/KillovSky/isis/network/members"><img title="GitHub Forks" src="https://img.shields.io/github/forks/KillovSky/isis?label=Forks&style=flat-square"></a>
    <a href="https://github.com/KillovSky/isis/watchers"><img title="GitHub Watchers" src="https://img.shields.io/github/watchers/KillovSky/isis?label=Watchers&style=flat-square"></a>
    <a href="http://isitmaintained.com/project/killovsky/isis"><img alt="Issue Resolution" src="http://isitmaintained.com/badge/resolution/killovsky/isis.svg"></a>
    <a href="http://isitmaintained.com/project/killovsky/isis"><img alt="Open Issues" src="http://isitmaintained.com/badge/open/killovsky/isis.svg"></a>
    <a href="https://hits.seeyoufarm.com"><img src="https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2FKillovSky%2FIsis&count_bg=%2379C83D&title_bg=%23555555&icon=&icon_color=%23E7E7E7&title=Views&edge_flat=false"/></a>
    <a href="https://github.com/KillovSky/isis/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/KillovSky/isis?label=Pull%20Requests&style=flat-square"></a>
    <a href="https://github.com/KillovSky/isis/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/KillovSky/isis?label=Contribuidores&style=flat-square"></a>
</p>

# O que é?

O Projeto Ísis é um plugin opcional desenvolvido em Python para o [Projeto Íris](https://github.com/KillovSky/Iris). Este plugin permite a adição de funcionalidades personalizadas em Python, incluindo algoritmos avançados e modelos de IA como Transformers e GPT4All. Com o Projeto Ísis, você pode personalizar o Projeto Íris sem a necessidade de modificar seu código principal ou aprender Node.js (JavaScript).

## Requisitos

Para garantir o correto funcionamento do Projeto Ísis, o Projeto Íris deve estar ativo. Observe que a versão atual do Projeto Ísis é experimental e foi desenvolvida em pouco tempo para fins de aprendizado, podendo conter erros menores.

1. **Python 3**:
    - É recomendada a versão mais recente disponível, mas acima da v3.8 provavelmente funcionará.
2. **Projeto Íris**:
    - Deve estar instalada e em execução.
3. **Dependências do Projeto Íris**:
    - Instale todas as dependências necessárias do Projeto Íris para assegurar o correto funcionamento da Ísis.

## Instalação

Para instalar as dependências do Projeto Ísis, você tem duas opções:

1. **Usando NPM**:
   - Embora o Projeto Ísis **NÃO UTILIZE** JavaScript, você pode instalar os módulos Python via NPM por conta das configurações inseridas para facilitar o uso de quem veio pelo Node.js.
   - Utilize o seguinte comando:
     ```bash
     npm run install
     ```
   - Este comando executará o `pip` por meio do NPM para instalar os requisitos do Python.
   - O NPM também pode ser usado para iniciar, como dito na etapa **Execução**.

2. **Alternativamente**:
   - Instale diretamente com pip:
     ```bash
     pip install -r requirements.txt
     ```

## Execução

Não é necessário qualquer scan de QR, inserção de código ou demais, basta que sua Íris esteja rodando.

Após a instalação das dependências, você pode executar o Projeto Ísis de duas maneiras:

1. **Usando NPM**:
   - O Projeto Ísis pode ser iniciado via NPM com um dos seguintes comandos:
     ```bash
     npm start
     ```
     ou
     ```bash
     npm run start
     ```
   - Isso executará o script Python diretamente por meio do NPM.

2. **Alternativamente**:
   - Execute diretamente com Python:
     ```bash
     python start.py
     ```

## Modificação

Se você não tem experiência com Python, a maneira mais simples de modificar o Projeto Ísis é através do sistema `Cases`, localizado em `src/commands/cases/index.py`. Lá você encontrará um comando de exemplo que pode ser usado como base para criar novos comandos.

Todos os parâmetros do Projeto Íris estão acessíveis via `env['nomeDaVariavel']`, permitindo que você utilize as funcionalidades do Projeto Íris em seu código Python, seja ele síncrono, assíncrono, ou em threads.

## Configuração

Para testar o Projeto Ísis com versões anteriores do Projeto Íris, ajuste a porta HTTPS do Projeto Íris [localizada aqui](https://github.com/KillovSky/Iris/blob/main/lib/Functions/Works/Terminal/utils.json#L211) para 3000, ou edite a porta na configuração `config.json`, localizada na pasta `settings` do Projeto Ísis.

## Detalhes Adicionais

**Informações da Versão**:
- **Codinome**: MERCURY
- **Versão**: v1.0.0
- **Tipo**: BETA
- **Erros**: Nenhum bug grave detectado
- **Data de Lançamento**: 03/08/2024
- **Observações**: Esta versão pode apresentar problemas menores não graves devido à ausência de alguns parâmetros opcionais ainda não integrados no Projeto Íris. Atualizações futuras do Projeto Íris resolverão essas questões, garantindo a integração completa e o funcionamento adequado dos parâmetros. Não será necessário reinstalar o Ísis para aplicar essas atualizações, pois os parâmetros já estarão incorporados nas futuras versões da Íris, e nenhuma intervenção adicional será necessária no Projeto Ísis, a menos que haja novas atualizações da mesma.

## Desenvolvimento Futuro

Estarei trabalhando em novas funcionalidades e atualizações tanto para o Projeto Íris quanto para o Projeto Ísis, e eventualmente em versões para outras linguagens de programação. Fique atento às atualizações e acompanhe as redes sociais para mais informações!

Obrigado pelo seu interesse e apoio! Vamos continuar evoluindo juntos a um open-source melhor! ❤️