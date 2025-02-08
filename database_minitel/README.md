
# minitel.py for Biotec escape game

## Usage

Procédure de démarrage du Minitel

Avant d'allumer la PI et le minitel :

Fnct + Sommaire

Fnct + T (en même temps) puis A
Fnct + T (en même temps) puis E
Fnct + P (en même temps) puis 4

Démarrer la raspberry


## Conf Raspberry Pi

### Install python & autorun au login
**TODO**

### Login silencieux (pour pas afficher le "last login", la version de kernel linux etc)
touch /home/biotec/.hushlogin

### Autoriser le login ssh en tant que root (vu que biotec a un autorun sur le script python minitel)
modif dans sshd_config

### Utilisateur poweroff

Se logguer en SSH en tant que poweroff / poweroff pour éteindre la pi.

sudo adduser poweroff
sudo adduser poweroff sudo

sudo visudo
```
poweroff        ALL=NOPASSWD: /usr/sbin/poweroff
```


sudo vi /home/poweroff/poweroff.sh
```
#!/bin/sh

sudo /usr/sbin/poweroff
```

sudo chown poweroff:poweroff /home/poweroff/poweroff.sh
sudo chmod +x /home/poweroff/poweroff.sh
sudo chsh --shell /home/poweroff/poweroff.sh poweroff

