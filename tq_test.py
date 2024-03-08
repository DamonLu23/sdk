from tqsdk import TqApi, TqAuth


"""
合约代码格式为交易所代码.合约代码，交易所代码如下：
CFFEX: 中金所
SHFE: 上期所
DCE: 大商所
CZCE: 郑商所
INE: 能源交易所(原油)
SSE: 上交所
SZSE: 深交所
GFEX: 广期所
"""

name_to_code = {"贵州茅台": "SSE.600519",
       "沪深300指数": "CFFEX.IF2403",
       "中国A50主连": "KQD.m@HKFE.MCA"}
code_to_name = {value: key for key, value in name_to_code.items()}

api = TqApi(auth=TqAuth("damonlu", "luhao1028"))
aim = "中国A50主连"
quote = api.get_quote(name_to_code[aim])

print(code_to_name[name_to_code[aim]], quote.datetime, "价格:", quote.last_price)
if 1:
    while True:
        api.wait_update()
        print(code_to_name[name_to_code[aim]], quote.datetime, "价格:", quote.last_price)

# api.close()