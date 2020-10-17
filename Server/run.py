import os
import tqdm

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
        os.mkdir(BACKUP_DIR)

def make_backup_dir(dir: str) -> None:
    os.system(f'cp {dir} {BACKUP_DIR}')

def make_backup_db(db: str) -> None:
    pass

if __name__ == "__main__":
    os.system('clear')
    if not(check_txt()):
        print(f'pls create dir and db file...')
        exit(0)        
    with open('dir.txt', 'r') as dir_file:
        for item in dir_file:
            dir_list.append(str(item).replace('\n',''))
        dir_file.close()
    with open('db.txt', 'r') as db_file:
        for item in db_file:
            db_list.append(str(item).replace('\n',''))
        db_file.close()
    
    print(f'{db_list}\n{dir_list}')

    for dir in tqdm(dir_list, desc='Backup Directory...'):
        make_backup_dir(dir)
