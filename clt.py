from Connection import Conn


if __name__ == '__main__':
    print('> get croc command you resive from srv')
    get_command:str = input('> ')
    clt: Conn = Conn()
    clt.Clt_Connection(get_command)