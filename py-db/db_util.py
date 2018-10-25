from urllib import request,parse
class DBUtil(object):
    def sendPost(self,url,paramName,param):
        #转为字节
        param = param.encode('utf-8')
        #加密
        param = parse.quote(param)
        out = (paramName+'='+param).encode('utf-8')
        result = request.urlopen(url, out).read()
        return result.decode()


