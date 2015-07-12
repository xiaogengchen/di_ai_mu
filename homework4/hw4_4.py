# !/usr/bin/env python
# -*-coding:utf-8-*-

u'''
用户注册。 建立一个用户数据库(包括登录名、 密码和上次登录时间戳)类(参考练习 7-5和 9-12)，
                  来管理一个系统，该系统要求用户在登录后才能访问某些资源。这个数据库类对用户进行
                  管理，并在实例化操作时加载之前保存的用户信息，提供访问函数来添加或更新数据库的信息。
                  在数据修改后，数据库会在垃圾回收时将新信息保存到磁盘。(参见__del__()).
'''

db = {}
def newuser():
    prompt = 'login desired: '
    while True:
        name = raw_input(prompt)
        if db.has_key(name):
            prompt = 'name taken, try another: '
            continue
        else:
            break
    pwd = raw_input("password: ")
    db[name]  = pwd
    
def olduser():
    name = raw_input('login: ')
    pwd = raw_input('passwd: ')
    passwd = db.get(name)
    if passwd == pwd:
        print 'welcome back', name
    else:
        print 'login incorrect'
        
def showmenu():
    prompt = '''
(N)ew User Login
(E)xisting User Login
(Q)uit
Enter choice:'''
    done = False
    while not done:
        chosen = False
        while not chosen:
            try:
                choice = raw_input(prompt).strip()[0].lower()
            except (EOFError, KeyboardInterrupt):
                choice = 'q'
            print '\nYou picked:[%s]' % choice
            if choice not in 'neq':
                print 'invalid option, try again'
            else:
                chosen = True
        if choice == 'q':done = True
        if choice == 'n':newuser()
        if choice == 'e':olduser()

if __name__ == "__main__":
    showmenu()
