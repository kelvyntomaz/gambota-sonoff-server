# Sonoff Gambota Server

TODO

[ ] Change request GET to POST

[ ] Change links to request

[ ] Interpreting json to refreshing status of sonoff

[ ] Make config file working propely

[ ] Multiples Sonoffs for one webserver

### EN

This is a simple server, make in python to work with your sonoff factory firmware

**PS: Only tested with Sonoff R2 ( Simple Version )**

#### How To Configure

- First, Connect Sonoff in your wireless network, and blocked the sonoff to access the internet.

- Download this project to your server

- Install python3
    - Debian-like

    `apt-get install python3 python3-pip`

    - Redhat-like

    `yum install python3 python3-pip3`

- Install Dependencies

 `pip install websocket-client`

- Change the configuration file [here](config.yml)

- Execute the server

  `python3 webserver.py`  


### PT-BR

Esse é um servidor simples, escrito em python para você utilizar com o seu sonoff com o firmware original.

**OBS: Somente foi testado com o Sonoff R2 ( O mais Simples )**


#### Como Configurar

- Primeiro, Conecte o sonoff na sua rede Wifi e bloqueie o sonoff para acesso a internet

- Baixe esse repositório onde será o Server

- Instale o python3

  - Debian-like

    `apt-get install python3 python3-pip`

  - Redhat-like

    `yum install python3 python3-pip3`

- Instale As Dependencias

 `pip install websocket-client`

- Altere o arquivo de configuração [aqui](config.yml)

- Execute o servidor

  `python3 webserver.py`
