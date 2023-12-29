### Aprendendo um pouco sobre Nginx e proxy_pass

##### O que consiste a tarefa:

Subir um docker com nginx que contenham duas rotas, uma com cache dos requests e outra sem cache.
As duas rotas devem apontar para o mesmo upstream que vai ser uma app em flask informando data e hora.

* Criar uma app em flask que ao ser chamada retorne data e hora
* Criar um docker nginx que se comunique com a app em flask
* Criar uma rota do nginx sem cache chamada nocache que se redirecione a chamada app em flask
* Criar uma rota do nginx com cache chamada cache que se redirecione a chamada app em flask e mantenha o retorno cacheado por 5 minutos


