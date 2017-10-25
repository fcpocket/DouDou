# -*- coding: utf-8 -*-
from urllib import request
from urllib import error
from urllib import parse
from http import cookiejar
import  re
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader,Context
# Create your views here.

class User(object):
    def __init__(self,qyname,sbh,name,qytype,hytype,qyaddress,phoneg,phoney,fptype,sstype,skp,bsp,qtime,ztime,yinhang,zhanghao):
        self.qyname = qyname
        self.sbh = sbh
        self.name = name
        self.qytype = qytype
        self.hytype = hytype
        self.qyaddress = qyaddress
        self.phoneg = phoneg
        self.phoney = phoney
        self.fptype = fptype
        self.sstype = sstype
        self.skp = skp
        self.bsp = bsp
        self.qtime = qtime
        self.ztime = ztime
        self.yinhang = yinhang
        self.zhanghao = zhanghao



def sousuo(requeset1):
    t = loader.get_template("index.html")
    # 登陆地址

    login_url = 'http://bwcrm1.bwjf.com:7001/login.jsp'
    #login_url = 'http://114.55.106.114/login.jsp'
    # User-Agent信息
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
    # Headers信息
    head = {'User-Agnet': user_agent, 'Connection': 'keep-alive'}
    # 登陆Form_Data信息
    Login_Data = {}
    Login_Data['userId'] = 'yangzhihua1'  # 改成你自己的用户名
    Login_Data['password'] = '854321'  # 改成你自己的密码
    # 使用urlencode方法转换标准格式
    logingpostdata = parse.urlencode(Login_Data).encode('utf-8')
    # 声明一个CookieJar对象实例来保存cookie
    cookie = cookiejar.CookieJar()
    # 利用urllib.request库的HTTPCookieProcessor对象来创建cookie处理器,也就CookieHandler
    cookie_support = request.HTTPCookieProcessor(cookie)
    # 通过CookieHandler创建opener
    opener = request.build_opener(cookie_support)
    # 创建Request对象
    req = request.Request(url=login_url, data=logingpostdata, headers=head)

    # 面向对象地址
    Id = requeset1.GET.get("ID",None)
    print(Id)
    #客户基本信息
    #设备信息
    #服务合同
    date_url1 = 'http://bwcrm1.bwjf.com:7001/server/crm/public/jsp/khtab/khjbxx.jsp?qxxkdm=1406&pageSize=200&KHBH=' + Id
    date_url2 = 'http://bwcrm1.bwjf.com:7001/server/crm/public/jsp/khtab/sbxx.jsp?qxxkdm=1406&pageSize=200&KHBH=' + Id
    date_url3 = 'http://bwcrm1.bwjf.com:7001/server/crm/public/jsp/khtab/fwht.jsp?qxxkdm=1406&pageSize=200&KHBH=' + Id
    #date_url1 = 'http://114.55.106.114/server/crm/public/jsp/khtab/khjbxx.jsp?qxxkdm=1406&pageSize=200&KHBH='+Id
    #date_url2 = 'http://114.55.106.114/server/crm/public/jsp/khtab/sbxx.jsp?qxxkdm=1406&pageSize=200&KHBH='+Id
    #date_url3 = 'http://114.55.106.114/server/crm/public/jsp/khtab/fwht.jsp?qxxkdm=1406&pageSize=200&KHBH='+Id
    Date_Data = {}
    Date_Data['qxxkdm'] = '1406'
    Date_Data['devId'] = ''
    Date_Data['sign'] = ''
    # 使用urlencode方法转换标准格式
    datepostdata = parse.urlencode(Date_Data).encode('utf-8')
    req1 = request.Request(url=date_url1, data=datepostdata, headers=head)
    req2 = request.Request(url=date_url2, data=datepostdata, headers=head)
    req3 = request.Request(url=date_url3, data=datepostdata, headers=head)
    try:
        # 使用自己创建的opener的open方法
        #1-----------------
        response = opener.open(req)
        response1 = opener.open(req1)
        html1 = response1.read().decode('utf-8')
        index = html1.find('nowrap')
        # 打印查询结果
        # print(html)
        res_tr1 = r'<td class="normalTd".*?>(.*?)</td>'
        m_tr1 = re.findall(res_tr1, html1, re.S | re.M )
        if len(m_tr1)!=0:
            print(re.compile(html1))
            print(m_tr1)
            sbh = m_tr1[0]
            qyname = m_tr1[1]
            name = m_tr1[3]
            qytype = m_tr1[29].strip()
            hytype = m_tr1[31]
            qyaddress = m_tr1[6]
            phoneg = m_tr1[4]
            phoney = m_tr1[5]
            fptype = m_tr1[12]
            print(fptype)
            sstype = m_tr1[10]
            zhanghao = m_tr1[28]
            yinhang = m_tr1[27]

        #2---------------
        response = opener.open(req)
        response2 = opener.open(req2)
        html2 = response2.read().decode('utf-8')
        index = html2.find('nowrap')
        # 打印查询结果
        # print(html)
        res_tr2 = r'<td *.*?>(.*?)</td>'
        m_tr2 = re.findall(res_tr2, html2, re.S | re.M)
        if len(m_tr2)!=0:
            print("2")
            print(m_tr2)

            skp = m_tr2[1]
            bsp = m_tr2[2]


        #3-----------------
        response = opener.open(req)
        response3 = opener.open(req3)
        html3 = response3.read().decode('utf-8')
        index = html3.find('nowrap')
        # 打印查询结果
        # print(html)
        res_tr3 = r'<td class="nowrap".*?>(.*?)</td>'
        m_tr3 = re.findall(res_tr3, html3, re.S | re.M)
        if len(m_tr3)!=0:
            print(m_tr3)
            qtime = m_tr3[3]
            ztime  =m_tr3[4]




    except error.URLError as e:
        if hasattr(e, 'code'):
            print("HTTPError:%d" % e.code)
        elif hasattr(e, 'reason'):
            print("URLError:%s" % e.reason)


    user = User(qyname, sbh, name, qytype,hytype, qyaddress, phoneg, phoney, fptype, sstype, skp, bsp, qtime, ztime,yinhang,zhanghao)
    c = {"user": user}
    return HttpResponse(t.render(c))

def index(request):
    return render(request, 'index.html')




