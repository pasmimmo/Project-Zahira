mkdir ~/.SlideScripty
unzip SlideScripty.zip -d ~/.SlideScripty/
mv ~/.SlideScripty/install_scripts/vlc_settings_file/vlc-qt-interface.conf ~/.config/vlc/
mv ~/.SlideScripty/install_scripts/vlc_settings_file/vlcrc ~/.config/vlc/
clear
echo 'file scompattati'
echo 'adesso imposteremo la directory da monitorare'
cd ~/.SlideScripty/install_scripts/
python3 SlideSettings.py
echo '[*] avvio installer...'
sudo apt install ffmpeg -y
echo '[i] ffmpeg installato correttamente'
sudo apt install vlc -y
echo '[i] VLC Media Player installato correttamente'
sudo pip3 install watchdog
echo '[P] Python Whatchdog Library installato correttamente'
sudo pip3 install schedule
echo '[P] Python Schedule Library installato correttamente'
echo '[*] Installazione Terminata'


