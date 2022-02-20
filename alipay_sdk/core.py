"""
@author:liazylee
@license: Apache Licence
@time: 2022/2/18 15:35
@contact: li233111@gmail.com
# code is far away from bugs with the god animal protecting
    I love animals. They taste delicious.
              ┏┓      ┏┓
            ┏┛┻━━━┛┻┓
            ┃      ☃      ┃
            ┃  ┳┛  ┗┳  ┃
            ┃      ┻      ┃
            ┗━┓      ┏━┛
                ┃      ┗━━━┓
                ┃  神兽保佑    ┣┓
                ┃　永无BUG！   ┏┛
                ┗┓┓┏━┳┓┏┛
                  ┃┫┫  ┃┫┫
                  ┗┻┛  ┗┻┛
"""
from pathlib import Path

from alipay import AliPay
from alipay.utils import AliPayConfig

from conf.env import ALIPAY_APPID

BASE_DIR = Path(__file__).resolve().parent.parent
with open(BASE_DIR / 'key/app_private_key.pem', 'r') as f:
    app_private_key_string = f.read()
with open(BASE_DIR / 'key/ali_public_key.pem', 'r') as f:
    alipay_public_key_string = f.read()
print(alipay_public_key_string, app_private_key_string)

# with open(BASE_DIR / 'key/app_private_key.pem', 'r') as f:
#     app_private_key_string = f.read()
# with open(BASE_DIR / 'key/dev_public_key.pem', 'r') as f:
#     alipay_public_key_string = f.read()
# print(alipay_public_key_string, app_private_key_string)
alipay = AliPay(
    # appid="2021000118652617",  # 沙箱支付宝appid
    appid=ALIPAY_APPID,  # 正式支付宝appid
    app_notify_url=None,  # 默认回调 url
    app_private_key_string=app_private_key_string,
    # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
    alipay_public_key_string=alipay_public_key_string,
    sign_type="RSA2",  # RSA 或者 RSA2
    debug=True,  # 默认 False
    verbose=False,  # 输出调试数据
    config=AliPayConfig(timeout=15)  # 可选，请求超时时间

)
# dc_alipay = DCAliPay(
#     appid="appid",
#     app_notify_url="http://example.com/app_notify_url",
#     app_private_key_string=app_private_key_string,
#     app_public_key_cert_string=app_public_key_cert_string,
#     alipay_public_key_cert_string=alipay_public_key_cert_string,
#     alipay_root_cert_string=alipay_root_cert_string
# )

# 如果您没有听说过 ISV， 那么以下部分不用看了
# app_auth_code 或 app_auth_token 二者需要填入一个
# isv_alipay = ISVAliPay(
#     appid="",
#     app_notify_url=None,  # 默认回调 url
#     app_private_key_srting="",
#     # 支付宝的公钥，验证支付宝回传消息使用，不是你自己的公钥,
#     alipay_public_key_string="",
#     sign_type="RSA",  # RSA or RSA2
#     debug=False,  # False by default
#     app_auth_code=None,
#     app_auth_token=None
# )
