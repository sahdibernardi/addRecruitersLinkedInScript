# 🇺🇸 LinkedIn Recruiter Connector

This project automates the connection with technical recruiters on LinkedIn using Selenium.

## Requirements

- Python 3.6+
- pip (Python package installer)
- Google Chrome

## Setup

### 1. Create and activate a virtual environment (optional, but recommended)

```
python3 -m venv venv
source venv/bin/activate
```
### 2. Install the dependencies

```
pip install -r requirements.txt
```

### 3. Create a \`.env\` file

Create a file named \`.env\` in the project's root directory and add your LinkedIn credentials:

```
LINKEDIN_USERNAME=youremail
LINKEDIN_PASSWORD=yourpassword
```

**Note:** Do not share this file or your credentials in a public repository.

### 4. Install Google Chrome and ChromeDriver

Download and install Google Chrome:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

The script will automatically install the required ChromeDriver.

## Execution

### 1. Run the script

```
python scriptAddRecruiters.py
```

### 2. Complete the two-step verification

After logging in, the script will pause for you to complete the two-step verification. Follow the instructions on the LinkedIn screen and then press Enter in the terminal to continue.

## Customization

### Search URL

You can customize the search URL to look for different types of recruiters or adjust location filters.

```
URL = "https://www.linkedin.com/search/results/people/?keywords=Tech%20Recruiter&origin=SWITCH_SEARCH_VERTICAL&sid=yN)"
```

### Connection Limit

You can adjust the connection limit by changing the \`max\` variable in the script.

```
max = 60
```

## Contribution

Contributions are welcome! Please open an issue or a pull request to discuss the changes you would like to make.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.


______________________________________________________________________

# 🇧🇷 Gerador de Conexão no Linkedin Com Recrutadores

Este projeto automatiza a conexão com recrutadores técnicos no LinkedIn usando o Selenium.

## Requisitos

- Python 3.6+
- pip (Python package installer)
- Google Chrome

## Configuração

### 1. Crie e ative um ambiente virtual (opcional, mas recomendado)

```
python3 -m venv venv
source venv/bin/activate
```

### 2. Instale as dependências

```
pip install -r requirements.txt
```

### 3. Crie um arquivo \`.env\`

Crie um arquivo chamado \`.env\` no diretório raiz do projeto e adicione suas credenciais do LinkedIn:

```
LINKEDIN_USERNAME=seuemail
LINKEDIN_PASSWORD=suasenha
```

**Nota:** Não compartilhe este arquivo ou suas credenciais em um repositório público.

### 4. Instale o Google Chrome e o ChromeDriver

Baixe e instale o Google Chrome:

```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb
```

O script instalará automaticamente o ChromeDriver necessário.

## Execução

### 1. Execute o script

```
python scriptAddRecruiters.py
```

### 2. Complete a verificação de duas etapas

Após o login, o script irá pausar para que você possa completar a verificação de duas etapas. Siga as instruções na tela do LinkedIn e depois pressione Enter no terminal para continuar.

## Personalização

### URL de busca

Você pode personalizar a URL de busca para procurar por diferentes tipos de recrutadores ou ajustar os filtros de localização.

```
URL = "https://www.linkedin.com/search/results/people/?keywords=Tech%20Recruiter&origin=SWITCH_SEARCH_VERTICAL&sid=yN)"
```

### Limite de Conexões

Você pode ajustar o limite de conexões alterando a variável \`max\` no script.

```
max = 60
```

## Contribuição

Contribuições são bem-vindas! Por favor, abra um issue ou um pull request para discutir as mudanças que você gostaria de fazer.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
