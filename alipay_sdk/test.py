"""
@author:liazylee
@license: Apache Licence
@time: 2022/2/18 15:32
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
from alipay_sdk.core import alipay
from conf.env import RETRUN_URL

subject = "测试订单"




def send_order(no, payment_no, total_amount):
    subject = "订单" + no
    # 电脑网站支付，需要跳转到https://openapi.alipay.com/gateway.do? + order_string
    order_string = alipay.api_alipay_trade_page_pay(
        out_trade_no=payment_no,
        total_amount=str(total_amount),
        subject=subject,
        return_url=RETRUN_URL,
        # notify_url="",
    )
    print(order_string)
    # return "https://openapi.alipaydev.com/gateway.do?" + order_string
    return "https://openapi.alipay.com/gateway.do?" + order_string


print(send_order("123", "123", 0.01))

#
#
# def verify_order(data, signature):
#     success = alipay.verify(data, signature)
#     if success and data["trade_status"] in ("TRADE_SUCCESS", "TRADE_FINISHED"):
#         return True
#     return False
