# -*- coding:utf-8 -*-

import urllib
import urllib2
import cookielib
import re
import webbrowser

#模拟登录淘宝类
class Taobao:

    #初始化方法
    def __init__(self):
        #登录的URL
        self.loginURL = "https://login.taobao.com/member/login.jhtml"
        #登录POST数据时发送的头部信息
        self.loginHeaders =  {
            'Host':'login.taobao.com',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Referer' : 'https://login.taobao.com/member/login.jhtml',
            'Content-Type': 'application/x-www-form-urlencoded',
            'Connection' : 'Keep-Alive'
        }
        #用户名
        self.username = 'mlgb_1994'
        #ua字符串，经过淘宝ua算法计算得出，包含了时间戳,浏览器,屏幕分辨率,随机数,鼠标移动,鼠标点击,其实还有键盘输入记录,鼠标移动的记录、点击的记录等等的信息
        self.ua='009#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'        #密码，在这里不能输入真实密码，淘宝对此密码进行了加密处理，256位，此处为加密后的密码
        self.password2='719a0a04dbfda49235e2e3f2625f04fabc1b950cee961c2806dece691dbcea950e509abd779169a7a66db3b554f69ee329a46c77eb0626ab6da8a3fde27a9247e83aedac5ed0b15173d78f70d1f396b93074c273fc38f5cba4b67177835b6f6fa483833ecfee11a170c99d05a9e5f1f53b7d1e4901b4af1c6b2cfee5ba2741d4'
        self.post = post = {
            'ua':self.ua,
            'TPL_checkcode':'',
            'CtrlVersion': '1,0,0,7',
            'TPL_password':'',
            'TPL_redirect_url':'https://mm.taobao.com/self/model_info.htm?user_id=687471686',
            'TPL_username':self.username,
            'loginsite':'0',
            'newlogin':'0',
            'from':'tb',
            'fc':'default',
            'style':'default',
            'css_style':'',
            'tid':'XOR_1_000000000000000000000000000000_625C4720470A0A050976770A',
            'support':'000001',
            'loginType':'4',
            'minititle':'',
            'minipara':'',
            'umto':'NaN',
            'pstrong':'3',
            'llnick':'',
            'sign':'',
            'need_sign':'',
            'isIgnore':'',
            'full_redirect':'',
            'popid':'',
            'callback':'',
            'guf':'',
            'not_duplite_str':'',
            'need_user_id':'',
            'poy':'',
            'gvfdcname':'10',
            'gvfdcre':'',
            'from_encoding ':'',
            'sub':'',
            'TPL_password_2':self.password2,
            'loginASR':'1',
            'loginASRSuc':'1',
            'allp':'',
            'oslanguage':'zh-CN',
            'sr':'1366*768',
            'osVer':'windows|6.1',
            'naviVer':'firefox|35'
        }
        #将POST的数据进行编码转换
        self.postData = urllib.urlencode(self.post)
        #设置cookie
        self.cookie = cookielib.LWPCookieJar()
        #设置cookie处理器
        self.cookieHandler = urllib2.HTTPCookieProcessor(self.cookie)
        #设置登录时用到的opener，它的open方法相当于urllib2.urlopen
        self.opener = urllib2.build_opener(self.cookieHandler,urllib2.HTTPHandler)
        #赋值J_HToken
        self.J_HToken = ''
        #登录成功时，需要的Cookie
        self.newCookie = cookielib.CookieJar()
        #登陆成功时，需要的一个新的opener
        self.newOpener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.newCookie))
        #引入工具类


    #得到是否需要输入验证码，这次请求的相应有时会不同，有时需要验证有时不需要
    def needCheckCode(self):
        #第一次登录获取验证码尝试，构建request
        request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
        #得到第一次登录尝试的相应
        response = self.opener.open(request)
        #获取其中的内容
        content = response.read().decode('gbk')
        #获取状态吗
        status = response.getcode()
        #状态码为200，获取成功
        if status == 200:
            print "获取请求成功"
            #\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801这六个字是请输入验证码的utf-8编码
            pattern = re.compile(u'\u8bf7\u8f93\u5165\u9a8c\u8bc1\u7801',re.S)
            result = re.search(pattern,content)
            #如果找到该字符，代表需要输入验证码
            if result:
                print "此次安全验证异常，您需要输入验证码"
                return content
            #否则不需要
            else:
                #返回结果直接带有J_HToken字样，表明直接验证通过
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern,content)
                if tokenMatch:
                    self.J_HToken = tokenMatch.group(1)
                    print "此次安全验证通过，您这次不需要输入验证码"
                    return False
        else:
            print "获取请求失败"
            return None

    #得到验证码图片
    def getCheckCode(self,page):
        #得到验证码的图片
        pattern = re.compile('<img id="J_StandardCode_m.*?data-src="(.*?)"',re.S)
        #匹配的结果
        matchResult = re.search(pattern,page)
        #已经匹配得到内容，并且验证码图片链接不为空
        if matchResult and matchResult.group(1):
            return matchResult.group(1)
        else:
            print "没有找到验证码内容"
            return False


    #输入验证码，重新请求，如果验证成功，则返回J_HToken
    def loginWithCheckCode(self):
        #提示用户输入验证码
        checkcode = raw_input('请输入验证码:')
        #将验证码重新添加到post的数据中
        self.post['TPL_checkcode'] = checkcode
        #对post数据重新进行编码
        self.postData = urllib.urlencode(self.post)
        try:
            #再次构建请求，加入验证码之后的第二次登录尝试
            request = urllib2.Request(self.loginURL,self.postData,self.loginHeaders)
            #得到第一次登录尝试的相应
            response = self.opener.open(request)
            #获取其中的内容
            content = response.read().decode('gbk')
            #检测验证码错误的正则表达式，\u9a8c\u8bc1\u7801\u9519\u8bef 是验证码错误五个字的编码
            pattern = re.compile(u'\u9a8c\u8bc1\u7801\u9519\u8bef',re.S)
            result = re.search(pattern,content)
            #如果返回页面包括了，验证码错误五个字
            if result:
                print "验证码输入错误"
                return False
            else:
                #返回结果直接带有J_HToken字样，说明验证码输入成功，成功跳转到了获取HToken的界面
                tokenPattern = re.compile('id="J_HToken" value="(.*?)"')
                tokenMatch = re.search(tokenPattern,content)
                #如果匹配成功，找到了J_HToken
                if tokenMatch:
                    print "验证码输入正确"
                    self.J_HToken = tokenMatch.group(1)
                    return tokenMatch.group(1)
                else:
                    #匹配失败，J_Token获取失败
                    print "J_Token获取失败"
                    return False
        except urllib2.HTTPError, e:
            print "连接服务器出错，错误原因",e.reason
            return False


    #通过token获得st
    def getSTbyToken(self,token):
        tokenURL = 'https://passport.alipay.com/mini_apply_st.js?site=0&token=%s&callback=stCallback6' % token
        request = urllib2.Request(tokenURL)
        response = urllib2.urlopen(request)
        #处理st，获得用户淘宝主页的登录地址
        pattern = re.compile('{"st":"(.*?)"}',re.S)
        result = re.search(pattern,response.read())
        #如果成功匹配
        if result:
            print "成功获取st码"
            #获取st的值
            st = result.group(1)
            return st
        else:
            print "未匹配到st"
            return False

    #利用st码进行登录,获取重定向网址
    def loginByST(self,st,username):
        stURL = 'https://login.taobao.com/member/vst.htm?st=%s&TPL_username=%s' % (st,username)
        headers = {
            'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:35.0) Gecko/20100101 Firefox/35.0',
            'Host':'login.taobao.com',
            'Connection' : 'Keep-Alive'
        }
        request = urllib2.Request(stURL,headers = headers)
        response = self.newOpener.open(request)
        content =  response.read().decode('gbk')
        #检测结果，看是否登录成功
        pattern = re.compile('top.location = "(.*?)"',re.S)
        match = re.search(pattern,content)
        if match:
            print "登录网址成功"
            location = match.group(1)
            return True
        else:
            print "登录失败"
            return False
    def getpage(self,pointurl):
        url=self.newOpener.open(pointurl)
        page=url.read()
        return page


    #程序运行主干
    def main(self):
        #是否需要验证码，是则得到页面内容，不是则返回False
        needResult = self.needCheckCode()
        #请求获取失败，得到的结果是None
        if not needResult ==None:
            if not needResult == False:
                print "您需要手动输入验证码"
                checkCode = self.getCheckCode(needResult)
                #得到了验证码的链接
                if not checkCode == False:
                    print "验证码获取成功"
                    print "请在浏览器中输入您看到的验证码"
                    webbrowser.open_new_tab(checkCode)
                    self.loginWithCheckCode()
                #验证码链接为空，无效验证码
                else:
                    print "验证码获取失败，请重试"
            else:
                print "不需要输入验证码"
        else:
            print "请求登录页面失败，无法确认是否需要验证码"


        #判断token是否正常获取到
        if not self.J_HToken:
            print "获取Token失败，请重试"
            return
        #获取st码
        st = self.getSTbyToken(self.J_HToken)
        #利用st进行登录
        result = self.loginByST(st,self.username)
        if result:
            print '登陆成功'
        else:
            print "登录失败"
