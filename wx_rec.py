#coding=utf8
import itchat, time, threading
import gender_guess

itchat.auto_login(hotReload=True)

Gender_Flag = False

def fun(th_name,delay):
    count = 0
    while Gender_Flag and count < 50:
        time.sleep(delay)
        count = count+1
        print('%s is working no.%s time'%(th_name,count))

# 以下四类的消息的Text键下存放了用于下载消息内容的方法，传入文件地址即可
@itchat.msg_register('Picture')
def download_files(msg):
    fileDir = '%s%s.jpg'%(msg['Type'], int(time.time()))
    # print(msg['Text'])
    msg['Text'](fileDir)
    gender_result = gender_guess.guessGender(fileDir)
    itchat.send('%s received'%msg['Type'], toUserName='filehelper')
    itchat.send('%s'%gender_result[0], toUserName=msg['FromUserName'])

@itchat.msg_register('Text')
def text_reply(msg):
    global Gender_Flag
    msg_content = msg['Text']

    friend = itchat.search_friends(userName=msg['FromUserName'])
    print('[Received]',friend['NickName'],':',msg_content)


    if friend['NickName'] == 'Coura':
        print('remote control...')
        if msg_content == 'hello':
            print('receive hello')
        if msg_content == 'start':
            print('start gender-guessing...')
            Gender_Flag = True
            # 加一个线程打开tf
            th = threading.Thread(target=fun, args=('th_1', 2))
            th.start()
        if msg_content == 'end':
            print('finish gender-guessing...')
            Gender_Flag = False
            # 关闭线程



itchat.run()
