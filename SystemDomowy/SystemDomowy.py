from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.core.window import Window
from kivy.uix.widget import Widget


class WindowManager(ScreenManager):
    pass
class MainWindow(Screen):#glowna strona aplikacji
    email=ObjectProperty(None)#dane do oczytu inputu uzytkownika by moc na nich dzialac
    password=ObjectProperty(None)
    authcode=ObjectProperty(None)

    def logowanie(self):
        plik=open('haslo.txt','r')#tylko jedno haslo pasuje do logowania (in progress)
        plik.readlines

        print("email: ", self.email.text,"haslo: ",self.password.text,"kod autoryzujacy: ",self.authcode.text)


class SecondWindow(Screen):#ekran z wyborem funkcji aplikacji, po przejsciu z ekranu main
    pass
#osobne ekrany dla poszczegolnych opcji
class swiatlo(Screen):
    pass

class drzwi(Screen):
    standrzwi=ObjectProperty(None)
    def press1(self):
        standrzwi="Otwarte"
        print(standrzwi)
    def press2(self):
        standrzwi="Zamknięte"
        print(standrzwi)        
        

class brama(Screen):
    pass

class tryskacze(Screen):
    pass

class temperatura(Screen):
    def slider(self,*args):#suwak do temperatury przesylajacy dane do konsoli w czasie rzeczywistym
        print (args)

class alarm(Screen):
    pass


kv = Builder.load_file("my.kv")


class MyMainApp(App):
    def build(self):
        Window.clearcolor = (134/255, 31/255, 27/255,1)
        return kv


if __name__ == "__main__":
    MyMainApp().run()