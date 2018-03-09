import urllib
from odps.udf import annotate
from odps.udf import BaseUDTF
from odps.udf import BaseUDAF


# reserve, ip, log_time, status_code
@annotate(
    "string,string,string->string,string,string,int")
class udtf_utp_mgtv_ios_nu(BaseUDTF):

    def process(self, reserve, ip, log_time):
        if not ip:
            return

        params = {
            'pos' : 0
            ,'idfa': reserve
            ,'ip' : ip
            ,'from' : 'UCLLQ'
            ,'callback' : 'http://www.baidu.com'}
        params = urllib.urlencode(params)
        ret = urllib.urlopen("http://iphone.v0.mgtv.com/ggt.php", params)
        status_code = ret.getcode()

        args = []
        args.append(ip)
        args.append(log_time)
        args.append(status_code)

        self.forward(reserve, *args)

