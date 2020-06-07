from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import requests
import json
# some random information I store to get quickly
'''
Binance url endpoint = https://api.binance.com 
Symbol url = /api/v3/ticker/price
Valr url endpoint = https://api.valr.com/v1/public
symbol url = /:currencyPair/marketsummary
'''
buy_ex = ''
sell_ex = ''
eth_p1 = ''
eth_p2 = ''
exchange = ('Binance', 'Valr')
# function to grab the price depending on the dropdown list
'''def get_price():
    if buy_ex == exchange[0]:
        eth_p1 = binprices_ethz()
        return eth_p1
    if sell_ex == exchange[0]:
        eth_p2 = binprices_ethz()
        return eth_p2
    if buy_ex == exchange[1]:
        eth_p1 = vrprices_ethz()
        return eth_p1
    if sell_ex == exchange[1]:
        eth_p2 = vrprices_ethz()
        return eth_p2
    elif buy_ex != exchange:
        eth_p1 = 'NaN'
        return eth_p1
    elif sell_ex != exchange:
        eth_p2 = 'NaN'
        return eth_p2
'''

# function that grabs Valr ETH/ZAR price
def vrprices_ethz():
    etz = requests.get('https://api.valr.com/v1/public/ETHZAR/marketsummary')
    data = etz.text
    parsed = json.loads(data)
    price = str(parsed["bidPrice"])
    return price

# function that grabs Binance ETH/ZAR price
def binprices_ethz():
    etz = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHZAR')
    data = etz.text
    parsed = json.loads(data)
    price = str(parsed["price"])
    return price

# The main widget where all other widgets are stored in (The window)
class PricerApp(App):

    def build(self):
        mbox = BoxLayout(orientation='vertical')

        hbox1 = BoxLayout(orientation='horizontal')
        hbox2 = BoxLayout(orientation='horizontal')
        hbox3 = BoxLayout(orientation='horizontal')

        dropdowns = DropDown()
        btnvs = Button(text='Valr', size_hint_y=None, height=44)
        btnvs.bind(on_release=lambda btnvs: dropdowns.select(btnvs.text))
        dropdowns.add_widget(btnvs)
        btnbs = Button(text='Binance', size_hint_y=None, height=44)
        btnbs.bind(on_release=lambda btnbs: dropdowns.select(btnbs.text))
        dropdowns.add_widget(btnbs)

        dropdownb = DropDown()
        btnvb = Button(text='Valr', size_hint_y=None, height=44)
        btnvb.bind(on_release=lambda btnvb: dropdownb.select(btnvb.text))
        dropdownb.add_widget(btnvb)
        btnbb = Button(text='Binance', size_hint_y=None, height=44)
        btnbb.bind(on_release=lambda btnbb: dropdownb.select(btnbb.text))
        dropdownb.add_widget(btnbb)

        buy_ex = Button(text='Exchange 1 (BUY)', size=(10,10), font_size=22)
        buy_ex.bind(on_release=dropdownb.open)
        dropdownb.bind(on_select=lambda instance, x: setattr(buy_ex, 'text', x))

        sell_ex = Button(text='Exchange 2 (SELL)', size=(10,10),  font_size=22)
        sell_ex.bind(on_release=dropdowns.open)
        dropdowns.bind(on_select=lambda instance, x: setattr(sell_ex, 'text', x))

        binetz = Label(text=binprices_ethz())
        vretz = Label(text=vrprices_ethz())

        hbox1.add_widget(Label(text='Symbols'))
        hbox1.add_widget(buy_ex)
        hbox1.add_widget(sell_ex)
        hbox1.add_widget(Label(text='Difference'))

        hbox2.add_widget(Label(text='ETH/ZAR'))
        hbox2.add_widget(binetz)
        hbox2.add_widget(vretz)
        hbox2.add_widget(Label(text='NaN'))

        hbox3.add_widget(Label(text='BTC/ZAR'))
        hbox3.add_widget(Label(text='NaN'))
        hbox3.add_widget(Label(text='NaN'))
        hbox3.add_widget(Label(text='NaN'))

        mbox.add_widget(hbox1)
        mbox.add_widget(hbox2)
        mbox.add_widget(hbox3)

        return mbox

# Loop that runs the app


if __name__ == '__main__':
    PricerApp().run()
