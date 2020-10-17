import os
from tqdm import tqdm

# var
db_list: list = []
dir_list: list = []
BACKUP_DIR: str = 'bk'

#function
def check_txt() -> bool:
    if os.path.isfile('dir.txt') and os.path.isfile('db.txt'):
        return True
    else:
        return False

def create_temp() -> None:
    if not(os.path.isdir(BACKUP_DIR)):
        os.system(f'mkdir {BACKUP_DIR}')
        os.system(f'mkdir {BACKUP_DIR}/directorys')
        os.system(f'mkdir {BACKUP_DIR}/Databases')

def make_backup_dir(directory: str) -> None:
    temp: str = directory.split('/')[-1]
    os.system(f'cp -r {directory} {BACKUP_DIR}/directorys/{temp}')
    del temp

def make_backup_db(db: str) -> None:
    os.system(f'sudo mysqldump {db} > {BACKUP_DIR}/Databases/{db}.sql')

if __name__ == "__main__":
    os.system('clear')
    if not(check_txt()):
        print(f'pls create dir and db file...')
        exit(0)
    create_temp()        
    with open('dir.txt', 'r') as dir_file:
        for item in dir_file:
            dir_list.append(str(item).replace('\n',''))
        dir_file.close()
    with open('db.txt', 'r') as db_file:
        for item in db_file:
            db_list.append(str(item).replace('\n',''))
        db_file.close()
    
    print(f'{db_list}\n{dir_list}')

    for directory in tqdm(dir_list, desc='Backup Directory...'):
        make_backup_dir(directory)

    for db_name in tqdm(db_list, desc='Backup Database...'):
        make_backup_db(db_name)
