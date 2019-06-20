import os, sys
print '\x1b[1;32m[+]Masukkan Username Sama Password                  [+]'
print '[+]Kalau Gak Tau Bisa Tanyakan Pada Admin           [+]'
print '\x1b[1;31;1m[+]CP : +62823-8637-2115                            [+]'
print '\x1b[36;1m[+]                   => INPUT <=                   [+]'
username = 'hatakecnk'
password = 'xNot_Found'

def restart():
    ngulang = sys.executable
    os.execl(ngulang, ngulang, *sys.argv)


def main():
    uname = raw_input('Username : ')
    if uname == username:
        pwd = raw_input('Password : ')
        if pwd == password:
            os.system('sh xNot_Found.sh')
        else:
            print '\n\x1b[1;36mSorry Invalid Password !!!\x1b[00m'
            print 'Back Login\n'
            restart()
    else:
        print '\n\x1b[1;36mSorry Invalid Username !!!\x1b[00m'
        print 'Back Login\n'
        restart()


try:
    main()
except KeyboardInterrupt:
    os.system('clear')
    restart()
