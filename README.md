# Github Actions Workshop, Flisol 2024
  <a href="https://t.me/PereiraTechTalksJs/1276">
    <img src="https://img.shields.io/badge/Telegram-2CA5E0?style=flat-squeare&logo=telegram&logoColor=white" alt="Join Telegram Pereira Tech Talks" />
  </a>
  <a href="https://github.com/GHA-Flisol/webapp-template/issues/new/choose">
    <img src="https://img.shields.io/badge/issues-welcome-green?style=flat-square" alt="Issues welcome!" />
  </a>
  <a href="https://github.com/GHA-Flisol/webapp-template#readme">
    <img src="https://img.shields.io/github/stars/GHA-Flisol/webapp-template?label=GitHub%20Stars&style=flat-square" alt="Star webapp template on GitHub" />
  </a>


Este año, conmemoramos con orgullo el vigésimo aniversario de FLISoL, nombrado "FLISoL 20 años" celebrando la ilustre trayectoria del festival iniciado ya en el lejano 2005, marcando así un hito importante en su historia. Destacando el crecimiento y el éxito del festival, Pereira se reincorpora a FLISoL después de un año impresionante, atrayendo a más de 600 entusiastas del mundo del software libre. Github no es ajeno al mundo del [Software Libre](https://www.gnu.org/philosophy/open-source-misses-the-point.en.html) y mundo Open Source , por el contrario muchas veces encontramos  majestuosas piezas de software escritas almancenas en Github o en Gitlab.

En éste taller introductorio y práctico de GitHub Actions, te sumergirás en el emocionante mundo de la automatización del desarrollo de software.
Nuestros guias Alejandro,Hector te ayudaran a través de conceptos fundamentales y te proporcionarán las habilidades necesarias para implementar algunos flujos de trabajo utilizando Github Actions para
construir tus Flujos de Integracion Continua.

## Requisitos previos

- Conocimientos básicos de Git y Github
- Experiencia básica en desarrollo de software
- Computador (Opcional)

## Instrucciones del Taller

Este proyecto ha sido creado exclusivamente para impartir el Workshop de Github Actions que se dicta en el Flisol 2024, [vease para mas informacion](https://flisol.info/FLISOL2024/Colombia/Pereira).

Este proyecto es una web api construida desde cero con los elementos mas basicos de un proyecto web que hace uso de :
- FastAPI
- PyTest
- pre-commit hooks

Para iniciar el taller click en el siguiente boton:

[![start-course](https://user-images.githubusercontent.com/1221423/235727646-4a590299-ffe5-480d-8cd5-8194ea184546.svg)](https://github.com/new?template_owner=GHA-Flisol&template_name=webapp-template&owner=%40me&name=github-actions-flisol2024&description=Workshop+de+Github+Actions+Flisol+2024&visibility=public)

Esto creara un **Fork** de este repositorio en tu cuenta personal de Github con el template basico que tiene la siguiente estructura :

```
├── Dockerfile
├── README.md
└── src
    ├── __init__.py
    ├── __pycache__
    ├── main.py
    ├── models.py
    ├── poetry.lock
    ├── pyproject.toml
    ├── requirements.txt
    └── test_main.py
```

Como observaras este proyecto tiene todo el codigo dentro de la carpeta `src/` para proceder a hacer el Workshop.

Alternativamente puedes hacer el desarrollo del taller completamente en linea utilizando [github.dev](https://github.dev/) al crear el Fork puedes presionar la tecla `.` esto abrira una version especial de `Vscode` en linea con el repo o podras utizar tu computador o el computador provisto en la sala.


### Desarollo Local

Despues de crear el Fork en tu cuenta personal debemos clonar el repositorio en tu entorno de trabajo:

#### Paso 1: Clonar el Repo
```sh
$ git clone https://github.com/cuenta-personal/github-actions-flisol2024 workshop-gha
$ cd workshop-gha
```

ahora necesitaremos instalar un virtualenvironment

#### Paso 2: Validar python3.10
Los siguientes pasos serían para el sistema operativo Ubuntu

```sh
$ sudo add-apt-repository ppa:deadsnakes/ppa
$ sudo apt update
$ sudo apt install python3.10 python3.10-venv python3.10-dev -y
$ python3.10
```

Al finalizar éste proceso debería aparecer una línea de comandos de python3.10

#### Paso 2: Crear un entorno Virtual

Los siguientes comandos se deben correr en la carpeta raiz del proyecto.

__ubuntu/debian/otros__ :
```sh
$ python3.10 -m venv env
$ source env/bin/activate
$ pip install -r src/requirements.txt
```

__mac__ :
```sh
$ brew install pyenv-virtualenv
$ pyenv virtualenv 3.10 workshop
$ pyenv activate workshop
$ pip install poetry
$ cd src
$ poetry install
```

#### Paso 3: Probar la aplicación

Ya teniendo el repositorio en local y las dependencias de python instaladas vamos a probar la aplicación de prueba de fastapi en local que está en el folder src/, para poder correr la aplicación sería de la siguiente forma:
```sh
$ fastapi run main.py --port 8080 --reload
```
En nuestro navegador al dirigirnos a la dirección http://localhost:8080/api/v1/all_users nos debería devolver un listado de usuarios que están en el sistema. Pero si nos dirigimos a la siguiente dirección

```
http://localhost:8080/
```

En ésta direción nos debería arrojar un mensaje de error 404. Ésto por el hecho de que en nuestra aplicación no hay una forma de procesar ésta petición, pero será lo siguiente que vamos a arreglar.

## Autores


- Hector Fabio Jimenez Saldarriaga [@h3ct0rjs](https://github.com/h3ct0rjs)
- Alejandro Vargas Bernal [@alejandro-vargas1](https://github.com/alejandro-vargas1)


## Licencia

[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
