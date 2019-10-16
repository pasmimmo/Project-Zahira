import json
from pathlib import Path
settings_path=Path.joinpath(Path.home(),'.config/SlideScripty','SlideSettings.json')
print(settings_path)

def read_settings():
    with open(settings_path) as settings_file:
        settings=json.load(settings_file)
    return settings
def write_settings():
    settings={
        'img_path':input('inserisci la path delle immagini: ')
    }
    f=open(settings_path,'w')
    f.writelines(json.dumps(settings))
    f.close()
    print('settings salvati correttamente')
try:
    print(f'le attuali impostazioni sono {read_settings()}')
except FileNotFoundError:
    print('le impostanzioni non sono valite')
if(input('vuoi cambiarle/crearle? s/n: ') is 's'):
    write_settings()