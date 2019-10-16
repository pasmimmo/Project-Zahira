echo '[i] Prima di tutto creo le cartelle di SlideScripty in .config'
mkdir ~/.config/SlideScripty
unzip SlideScripty.zip -d ~/.config/SlideScripty/
echo '[L] Avvio Installazione di Vlc'
sudo apt install vlc -y
echo '[L] Setto VLC'
mkdir ~/.config/vlc
mv ~/.config/SlideScripty/install_scripts/vlc_settings_file/vlc-qt-interface.conf ~/.config/vlc/
mv ~/.config/SlideScripty/install_scripts/vlc_settings_file/vlcrc ~/.config/vlc/
clear
echo '[i] Adesso imposteremo la directory da monitorare'
python3 ~/.config/SlideScripty/install_scripts/SlideSettings.py
echo '[L] Avvio installazione FFMPEG installer...'
sudo apt install ffmpeg -y
echo '[i] ffmpeg installato correttamente'
echo '[i] Installeremo le librerie di python 3'
sudo pip3 install watchdog
echo '[P] Python Whatchdog Library installato correttamente'
sudo pip3 install schedule
echo '[P] Python Schedule Library installato correttamente'
rm install.sh
rm SlideScripty.zip
echo '[*] Installazione Terminata'
python3 SlideScripty.py


