import requests

class Safetree:
    def __init__(self):
        self.sess = requests.session()

    def login(self, user, pwd):
        url = 'https://jiangsulogin.safetree.com.cn/LoginHandler.ashx?' \
              'jsoncallback=&userName={user}&password={pwd}&checkcode=&type=login&loginType=1'\
            .format(user=user, pwd=pwd)
        r = self.sess.get(url)
        print(r.text)

    def finish(self, n):
        url = 'https://xuzhou.safetree.com.cn/WebApi/SpecialService/FinishWork?jsoncallback=jQuery16107306948434400364_1512459379470&r=0.06516191571172358&SpecialID=141&WorkStep={}'.format(n)
        r = self.sess.get(url)
        print(r.text)



if __name__ == '__main__':
    with open('user.txt') as f:
        for line in f:
            s = Safetree()
            print(line)
            s.login(line.strip(), '123456')
            s.finish(1)
            s.finish(2)