from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.dropdown import DropDown
from kivy.uix.button import Button
import requests
import json

'''Binance url endpoint = https://api.binance.com 
   Symbol url = /api/v3/ticker/price
   Valr url endpoint = https://api.valr.com/v1/public
   symbol url = /:currencyPair/marketsummary
'''


def vrprices():
    etz = requests.get('https://api.valr.com/v1/public/ETHZAR/marketsummary')
    data = etz.text
    parsed = json.loads(data)
    price = str(parsed["bidPrice"])
    return price


def binprices():
    etz = requests.get('https://api.binance.com/api/v3/ticker/price?symbol=ETHZAR')
    data = etz.text
    parsed = json.loads(data)
    price = str(parsed["price"])
    return price


class PricerApp(App):

    def build(self):
        Mbox = BoxLayout(orientation='vertical')

        Hbox1 = BoxLayout(orientation='horizontal')
        Hbox2 = BoxLayout(orientation='horizontal')
        Hbox3 = BoxLayout(orientation='horizontal')


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

        binetz = Label(text=binprices())
        vretz = Label(text=vrprices())


        Hbox1.add_widget(Label(text='Symbols'))
        Hbox1.add_widget(buy_ex)
        Hbox1.add_widget(sell_ex)
        Hbox1.add_widget(Label(text='Difference'))

        Hbox2.add_widget(Label(text='ETH/ZAR'))
        Hbox2.add_widget(binetz)
        Hbox2.add_widget(vretz)
        Hbox2.add_widget(Label(text='NaN'))

        Hbox3.add_widget(Label(text='BTC/ZAR'))
        Hbox3.add_widget(Label(text='NaN'))
        Hbox3.add_widget(Label(text='NaN'))
        Hbox3.add_widget(Label(text='NaN'))

        Mbox.add_widget(Hbox1)
        Mbox.add_widget(Hbox2)
        Mbox.add_widget(Hbox3)

        return Mbox


if __name__ == '__main__':
    PricerApp().run()
