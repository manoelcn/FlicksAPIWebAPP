# Descrição

FlicksAPIWebAPP é um projeto front-end que consome a FlicksAPI. Caso queira saber mais sobre a API, acesse: **https://github.com/manoelcn/FlicksAPI**

Esse projeto foi desenvolvido com o **framework Streamlit**, que permite a criação de aplicações web interativas de forma rápida e fácil.

## Instalação

Siga os passos abaixo para clonar e executar o projeto no seu computador:

1. **Clone o repositório**

    ``` git clone https://github.com/seu-usuario/FlicksAPIWebAPP.git ```

2. **Crie um ambiente virtual**
   
   ``` python -m venv venv ```

3. **Ative o ambiente virtual**
   
   - Windows: ``` venv\Scripts\activate ```
   - Linux/MacOs: ``` source venv/bin/activate ```

4. **Instale as dependências**
   
   ``` pip install -r requirements.txt ```

5. **Instale as dependências de desenvolvimento (opcional)**
   
   ``` pip install -r requirements_dev.txt ```

6. **Execute o WebApp Streamlit**

   ``` streamlit run app.py ```

7. **Acesse o projeto no seu navegador**

   Abra o navegador e acesse: **http://localhost:8501**

---

## Observações

- Este projeto está consumindo a API que está hospedada neste URL: **https://mcandidon.pythonanywhere.com**.
- Caso você queira consumir a API localmente ou o site onde a API está hospedada esteja fora do ar, faça o seguinte:
  1. Em todos os arquivos `repository.py`, que são responsáveis por obter os dados da API, mude a variável `self.__base_url` para o local onde a API está hospedada localmente.
  2. No arquivo `service.py`, que está no diretório `api`, mude a variável `self.__base_url` para o local onde a API está hospedada localmente.
- Para conseguir fazer login no web app, você precisará registrar-se na API.
