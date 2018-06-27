talk-asyncio-best
=================

Prérequis
---------

- Vagrant: [Download](https://www.vagrantup.com/downloads.html)
- Ansible: [Install](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#installing-the-control-machine)

Exécuter les démos
------------------

```bash
$ vagrant up
$ vagrant ssh
$ cd /vagrant
$ pip3 install -r requirements.txt
```

```bash
$ python3 demo1-tasks.py
```

```bash
$ python3 demo2-aiohttp.py
```

```bash
$ python3 demo3-sanic.py
$ curl http://localhost:8000
$ python3 demo4-websockets.py
```

```bash
$ python3 demo5-uvloop.py
```

```bash
$ python3 demo6-generators.py
```
