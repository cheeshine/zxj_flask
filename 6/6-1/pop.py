from poplib import POP3 			#导入内置邮件处理模块
import re,email,email.header		#导入内置文件处理模块
from p_email import mypass			#导入内置模块
def jie(msg_src,names):			#定义解码邮件内容函数jie()
    msg = email.message_from_bytes(msg_src)
    result = {}                     	#变量初始化
    for name in names:              	#遍历name
        content = msg.get(name)		#获取name
        info = email.header.decode_header(content)#定义变量info
    if info[0][1]:
            if info[0][1].find('unknown-') == -1:#如果是已知编码
                    result[name] = info[0][0].decode(info[0][1])
            else:                  		#如果是未知编码
                try:               		#异常处理
                    result[name] = info[0][0].decode('gbk')
                except:
                    result[name] = info[0][0].decode('utf-8')
    else:
            result[name] = info[0][0]  #获取解码结果
    return result					#返回解码结果
if __name__ == "__main__":
    pp = POP3("pop.sina.com")        #实例化邮件服务器类
    pp.user('guanxijing820111@sina.com') #传入邮箱地址
    pp.pass_(mypass)                	#密码设置
    total,totalnum = pp.stat()		#获取邮箱的状态
    print(total,totalnum)			#打印显示统计信息
    for i in range(total-2,total):	#遍历获取最近的两封邮件
        hinfo,msgs,octet = pp.top(i+1,0)#返回bytes类型的内容
        b=b''
        for msg in msgs:             	#遍历msg
            b += msg+b'\n'
        items = jie(b,['subject','from'])  #调用函数jie()返回邮件主题
        print(items['subject'],'\nFrom:',items['from'])#调用函数jie()返回发件人的信息
        print()                     	#打印空行
    pp.close()                      	#关闭连接
