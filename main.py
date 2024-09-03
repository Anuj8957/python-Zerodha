
from kite_trade import *
# # Second way is provide 'enctoken' manually from 'kite.zerodha.com' website
# # Than you can use login window of 'kite.zerodha.com' website Just don't logout from that window
# # # Process shared on YouTube 'TradeViaPython'
import time
enctoken = ""
kite = KiteApp(enctoken=enctoken)

# print(kite.instruments('NSE'))
from kiteconnect import KiteTicker
user_id = kite.profile()["user_id"]
kws = KiteTicker(api_key="ANUJ", access_token=enctoken+"&user_id="+user_id)

# def on_ticks(ws, ticks):
#     print(ticks)
#
# kws.on_ticks = on_ticks
# kws.connect(threaded=True)
# while not kws.is_connected():
#     time.sleep(1)
# print("WebSocket : Connected")
# kws.subscribe([256265, 260105, 738561, 5633])
# kws.set_mode(kws.MODE_QUOTE, [256265, 260105, 738561, 5633])
# time.sleep(30)
# kws.unsubscribe([256265, 260105, 738561, 5633])

order = kite.place_order(variety=kite.VARIETY_REGULAR,
                         exchange=kite.EXCHANGE_NSE,
                         tradingsymbol="HINDZINC",
                         transaction_type=kite.TRANSACTION_TYPE_SELL,
                         quantity=4,
                         product=kite.PRODUCT_CNC,
                         order_type=kite.ORDER_TYPE_MARKET,
                         price=None,
                         validity=None,
                         disclosed_quantity=None,
                         trigger_price=None,
                         squareoff=None,
                         stoploss=None,
                         trailing_stoploss=None,
                         tag="ANUJ")

print(order)

# while True:
#     print(kite.positions())
#
#     time.sleep(1)