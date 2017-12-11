# TVHeadend Script Guida TV
Un progetto per acquisire la guida TV dei canali Italiani e mostrarla in [TVHeadend](https://tvheadend.org/).

#### Breve descrizione

Basato su un precedente script creato da Mathias F. Svendsen e ottimizzato da Andrea Draghetti ho adattato il codice alla distribuzione di kodi [LibreELEC](https://libreelec.tv). 

#### Installazione

Per attivare e installare lo script procedete come segue:

* Accedere mediante SSH a LibreElec (kodi)
* Copiare o creare il file tv_grab_italy.py all'interno della directory /storage/.kodi/addons/service.tvheadend42/bin/
* Rinominare il file eliminando l'estensione .py
* Assegnarne i permessi 755 (chmod 755 tv_grab_italy)
* Dalla WebGUI accedere al pannello Configuration (Configurazione) > Channel (Canale) > EPG Grabber Modules (Moduli dell'estrattore EPG) > selezionare il Grabber riconoscibile dall'etichetta "XMLTV: TV Italy..."

#### License

Copyright (c) 2017 Gitner
Released under the GPL 3 license.
