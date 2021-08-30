<!-- [![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url] -->

<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/jesuschm/zought">
    <img src="https://user-images.githubusercontent.com/548486/131215048-3e3223d2-5856-4687-b2ee-1774e2216726.png" alt="Logo">
  </a>

  <!-- <h3 align="center">Zoughts</h3>-->
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.
* <a href="https://docs.python.org/3/using/index.html">Python 3</a>
* <a href="https://packaging.python.org/tutorials/installing-packages/">Pip</a>
* <a href="https://docs.docker.com/engine/install/">Docker engine</a>
* <a href="https://docs.docker.com/compose/install/">Docker-compose</a>
  
### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/jesuschmn/zoughts.git
   ```
2. Docker compose
  ```sh
    docker-compose up -d
  ```
3. [Optional] Create a superuser
  ```sh
  docker exec -it container_id python manage.py createsuperuser
  ```
  
### Usage
For development, with the repo cloned, you have to do the following:

1. Create and activate the virtual environment (<a href="https://docs.python.org/3/using/index.html">info</a>)
2. Install requirements
  ```sh
    pip install -r requirements.txt
  ```
3. Change the settings of the projects. Specifically, the DATABASE HOST value like this:
```py
DATABASES = {
    'default': {
        ...
        'HOST': 'localhost',
        ...
    }   
}
```
4. Then up the postgresql database with the following command:
```sh
  docker-compose up -d bd
```
5. Last, just start the server executing:
```sh
  python manage.py runserver
```
And start coding and chill.

## Requirements
To see the list of requirements done and which ones are still in develop you can read the following file: [jesuschm/zoughts/blob/develop/Requirements.md](Requirements.md)
<!-- CONTACT -->
## Contact

Jesús Chacón - <a href="https://twitter.com/jchaconmontero">Twitter</a> - jesuschaconmontero@gmail.com

Project Link: [https://github.com/jesuschmn/zoughts](https://github.com/jesuschmn/zoughts)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[linkedin-url]: https://www.linkedin.com/in/jchaconmontero/
