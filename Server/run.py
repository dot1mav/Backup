import os

# var
db_list: list = []
dir_list: list = []

#function
def check_txt() -> bool:
    if os.path.isfile('dir.txt') and os.path.isfile('db.txt'):
        return True
    else:
        return False

if __name__ == "__main__":
    if not(check_txt()):
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