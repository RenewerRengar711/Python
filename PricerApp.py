from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
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


class LoginScreen(GridLayout):

    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.rows = 3
        self.cols = 2

        self.dropdowns = DropDown()
        btnvs = Button(text='Valr', size_hint_y=None, height=44)
        btnvs.bind(on_release=lambda btnvs: self.dropdowns.select(btnvs.text))
        self.dropdowns.add_widget(btnvs)
        btnbs = Button(text='Binance', size_hint_y=None, height=44)
        btnbs.bind(on_release=lambda btnbs: self.dropdowns.select(btnbs.text))
        self.dropdowns.add_widget(btnbs)


        self.dropdownb = DropDown()
        btnvb = Button(text='Valr', size_hint_y=None, height=44)
        btnvb.bind(on_release=lambda btnvb: self.dropdownb.select(btnvb.text))
        self.dropdownb.add_widget(btnvb)
        btnbb = Button(text='Binance', size_hint_y=None, height=44)
        btnbb.bind(on_release=lambda btnbb: self.dropdownb.select(btnbb.text))
        self.dropdownb.add_widget(btnbb)


        buy_ex = Button(text='Exchange 1 (BUY)', size_hint=(None, None))
        buy_ex.bind(on_release=self.dropdownb.open)
        self.dropdownb.bind(on_select=lambda instance, x: setattr(buy_ex, 'text', x))
        self.add_widget(buy_ex)

        sell_ex = Button(text='Exchange 2 (SELL)', size_hint=(None, None))
        sell_ex.bind(on_release=self.dropdowns.open)
        self.dropdowns.bind(on_select=lambda instance, x: setattr(sell_ex, 'text', x))
        self.add_widget(sell_ex)

        self.add_widget(Label(text='ETH/ZAR'))
        self.add_widget(Label(text='ETH/ZAR'))
        self.binetz = Label(text=binprices())
        self.add_widget(self.binetz)
        self.vretz = Label(text=vrprices())
        self.add_widget(self.vretz)


class PricerApp(App):

    def build(self):
        self.title = "My App"
        return LoginScreen()


if __name__ == '__main__':
    PricerApp().run()
