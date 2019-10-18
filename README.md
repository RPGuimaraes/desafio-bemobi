
# desafio-bemobi  
#### Desafio Encurtador de URL - Raphael Guimarães  
  
A aplicação foi criada em Django, utilizando Mongodb e Docker 18.x. 
 
**Run**  
```  
docker-compose up --build  
```  
**Stop**  
```  
docker-compose down  
```  
  
## Client  
Após executar o projeto localmente, o client que consome a API pode ser acessado em:  
>http://localhost:8000  
  
## API  
A API possui três endpoint's:  
  
>POST: http://localhost:8000/create  
  
Essa url é utilizada para encurtar url's.  
  
**QueryParams**  
  
1. url:  parâmetro *obrigatório*. Deve ser uma url válida que será encurtada.  
2. alias: é opcional e deve conter apenas letras   
  
**Response: 200 OK**  
```  
{
  "alias": "http://localhost:8000/customalias",
  "url": "http://original_url",
  "statistic": {
    "time_taken": "000.000ms"
  }
}    
```  
>GET: http://localhost:8000/show-ranking  
  
Essa url é utilizada para exibir as 10 url's mais acessadas.  
  
**Response: 200 OK**  
```  
{
  "ranking": [
    {
      "alias": "custom_alias",
      "url": "http://original.url.com.br",
      "clicks": 0
    }
  ]
}  
```  
  
>GET: http://localhost:8000/{alias}  
  
Essa url é utilizada para redirecionar para uma url que foi previamente encurtada  
  
**Slug**  
  
1. alias: é qualquer alias válido préviamente criado por esta api.
