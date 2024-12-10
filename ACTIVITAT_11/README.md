## Readme de la pràctica 11 de M7

### Dibuix de la base de dades amb les taules
![dibuix base de dades](IMG_8186.jpg)

Al començament no vaig entendre bé el que es demanava a la pràctica i després va resultar que per exemple en el segon i tercer exercicis només calia que el endpoint retornés un text que en aquest cas concret era _començar partida_. Aixó per un costat exigia tenir o fer una altra taula a la base de dades per desar o emmagatzemar aquest _string_ que després mitjançant un GET es recuperaria des de la base de dades i retornaria en format json per l'endpoint. Aquestes són les característiques de la nova taula Cadenas: 
![dades de la nova taula creada](tabla_cadenas.jpg)


El punt 2 i 3 de la pràctica demanen dos endpoints per renderitzar el mateix text, així que amb el mateix endpoint funcionaria, la qüestió és que després, el resultat es mostraria en un altre contenidor de visualització (js/html). Per tot això només faré un endpoint: start_game/id que retorna un json.