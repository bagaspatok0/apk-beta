#import mudules

from logging import root
from kivymd.app import MDApp
from kivymd.uix.textfield import MDTextField
from kivymd.uix.button import MDRoundFlatButton, MDRectangleFlatButton, MDRoundFlatIconButton, MDFlatButton
from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.metrics import dp
from kivymd.uix.dialog import MDDialog
from kivymd.uix.list import OneLineAvatarListItem
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout



Window.size = 320,600
KV = '''
        
#:import get_color_from_hex kivy.utils.get_color_from_hex

ScreenManager:
    MenuScreen:
    ProfileScreen:
    PengaturanScreen:
    EdituserScreen:
    MessengerScreen:
    
<MenuScreen>:
    name: 'menu'
    MDToolbar:
        md_bg_color: get_color_from_hex("#b469e9")
        title: 'Patok'
        pos_hint: {'center_y':0.95}   
        left_action_items: [['notification-clear-all', lambda x: nav_drawer.set_state('open')]]
        MDIconButton:
            icon: 'facebook-messenger'
            pos_hint: {'center_x':0.5, 'center_y':0.5}
            on_press: root.manager.current = 'messenger'
                
    MDNavigationDrawer:
        id: nav_drawer
        BoxLayout:
            orientation: 'vertical'
            spacing: '8dp'
            padding: '8pd'
                
            Image:
                source: 'bagas.jpg' 
                    
            MDLabel:
                text: '     bagas_dyd'
                font_style: 'Subtitle1'
                size_hint_y: None
                height: self.texture_size[1]
                    
            MDLabel:
                text: '     cssbagas@gmail.com'
                font_style: 'Caption'
                size_hint_y: None
                height: self.texture_size[1]
                
            ScrollView:
                MDList:
                    OneLineIconListItem:
                        text: 'Profile'
                        on_press: root.manager.current = 'profile'
                        IconLeftWidget:
                            icon: 'account'
                            on_press: root.manager.current = 'profile'
                                                    
                    OneLineIconListItem:
                        text: 'Berlalih akun'
                        on_release: app.gantiakun()
                        IconLeftWidget:
                            icon: 'account-convert'
                            on_release: app.gantiakun()
                            
                    OneLineIconListItem:
                        text: 'Tambah akun'
                        on_press: app.tambahakun()
                        IconLeftWidget:
                            icon: 'account-plus'
                            
                    OneLineIconListItem:
                        text: 'Pengaturan'
                        on_press: root.manager.current = 'pengaturan'
                        IconLeftWidget:
                            icon: 'penguin' 
                            on_press: root.manager.current = 'pengaturan'
                        
                    OneLineIconListItem:
                        text: 'Keluar'
                        on_release: app.keluar()
                        IconLeftWidget:
                            icon: 'logout'
                            on_release: app.keluar()


<ProfileScreen>:
    name: 'profile'
    MDToolbar:
        md_bg_color: get_color_from_hex("#b469e9")
        title: 'Profile'
        pos_hint: {'center_y':0.95}
        left_action_items: [['account-settings-outline']]
        right_action_items: [['dots-vertical']]
    
    MDRoundFlatIconButton:
        text: 'Ganti username'
        pos_hint: {'center_x':0.3, 'center_y':0.78}
        icon: 'account-edit'
        on_press: root.manager.current = 'edituser'
        
    MDRoundFlatIconButton:
        text: 'Ganti email'
        pos_hint: {'center_x':0.25, 'center_y':0.68}
        icon: 'email'
    
    MDRoundFlatIconButton:
        text: 'Ganti password'
        pos_hint: {'center_x':0.3, 'center_y':0.58}
        icon: 'onepassword'
    
    MDRoundFlatIconButton:
        text: 'Ganti No'
        pos_hint: {'center_x':0.23, 'center_y':0.48}
        icon: 'phone-settings'
    
    MDRoundFlatIconButton:
        text: 'Ganti Pin Card'
        pos_hint: {'center_x':0.28, 'center_y':0.38}
        icon: 'credit-card-settings'
        
    MDRoundFlatIconButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.75, 'center_y':0.1}
        icon: 'arrow-left-circle-outline'
        on_press: root.manager.current = 'menu'        


<MessengerScreen>:
    name: 'messenger'
    MDToolbar:
        title: 'Pesan'
        left_action_items: [['android-messages']]
        md_bg_color: get_color_from_hex("#0c343d")
        pos_hint: {'center_y':0.95}
    MDIconButton:
        icon: 'magnify'
        pos_hint: {'center_x':0.1, 'center_y':0.8}

    MDTextField:
        id: search_field
        hint_text: 'Cari pesan'
        pos_hint: {'center_x':0.52, 'center_y':0.81}
        size_hint_x: None
        width: 230
        
    MDRoundFlatIconButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.75, 'center_y':0.1}
        on_press: root.manager.current = 'menu'
        icon: 'arrow-left-circle-outline'
        
        
        
<EdituserScreen>:
    name: 'edituser'
    MDToolbar:
        md_bg_color: get_color_from_hex("#b469e9")
        left_action_items: [['account-settings-outline']]
        right_action_items: [['dots-vertical']]
        title: 'Edit username'
        pos_hint: {'center_y':0.95}

    MDTextField:
        hint_text: "Username baru?"
        pos_hint: {'center_x':0.5, 'center_y':0.6}
        size_hint_x: None
        width: 270
        icon_right: 'account-circle'
    
    MDRoundFlatButton:
        text: 'Ganti'
        pos_hint: {'center_x':0.3, 'center_y':0.5}
    MDRoundFlatButton:
        text: 'Batal'
        pos_hint: {'center_x':0.7, 'center_y':0.5}
    
    MDRoundFlatIconButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.75, 'center_y':0.1}
        on_press: root.manager.current = 'profile'
        icon: 'arrow-left-circle-outline'
        

<PengaturanScreen>:
    name: 'pengaturan'
    MDToolbar:
        md_bg_color: get_color_from_hex("#0c343d")
        pecific_text_color: get_color_from_hex("#4a4939")
        title: 'Pengaturan'
        left_action_items: [['wrench']]
        right_action_items: [['dots-vertical']]
        pos_hint: {'center_y':0.95}
        
    MDRoundFlatIconButton:
        text: 'Gelap'
        on_release: app.gelap()
        pos_hint: {'center_x':0.2, 'center_y':0.8}
        icon: 'theme-light-dark'
        
    MDRoundFlatIconButton:
        text: 'Terang'
        on_release: app.terang()
        pos_hint: {'center_x':0.2, 'center_y':0.7}
        icon: 'theme-light-dark'
    
    MDRoundFlatIconButton:
        text: 'Kembali'
        pos_hint: {'center_x':0.75, 'center_y':0.1}
        on_press: root.manager.current = 'menu'
        icon: 'arrow-left-circle-outline'
        






<Content>
    orientation: "vertical"
    spacing: "12dp"
    size_hint_y: None
    height: "120dp"

    MDTextField:
        hint_text: "Username"

    MDTextField:
        hint_text: "Password"
        password: True        
        
'''


#========================================================     
class MenuScreen(Screen):
    pass
class ProfileScreen(Screen):
    pass
class PengaturanScreen(Screen):
    pass
class EdituserScreen(Screen):
    pass
class MessengerScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ProfileScreen(name='profile'))
sm.add_widget(PengaturanScreen(name='pengaturan'))
sm.add_widget(EdituserScreen(name='edituser'))
sm.add_widget(MessengerScreen(name='messenger'))
#========================================================


class Item(OneLineAvatarListItem):
    divider = None
    source = StringProperty()
class Content(BoxLayout):
    pass

class Application(MDApp):
    def build(self):
        screen = Screen()
        
        lang = Builder.load_string(KV)
        screen.add_widget(lang)
        
        return screen
    
    #hasil menu / pengaturan
    
    def keluar(instance):
        exit()
    
    def gelap(self):
        self.theme_cls.theme_style = 'Dark'
    def terang(self):
        self.theme_cls.theme_style = 'Light'
    
    #========================================
    #gantiakun
    def gantiakun(self):
        
        btn1 = MDFlatButton(
            text = 'Batal',
            on_release = self.hasilbtn1
        )
        
        self.dialog = MDDialog(
            title = 'Ganti akun',
            type = 'simple',
            items=[
                Item(text='bagaspamadya37@gmail.com'),
                Item(text='bagaspython@gmail.com')
            ],
            buttons = [btn1]
        )
        self.dialog.open()
        
    def hasilbtn1(self, obj):
        self.dialog.dismiss()
    #========================================
    #tambah akun
    def tambahakun(self):
        btn1 = MDFlatButton(
        text = 'Batal',
        on_release = self.hasilbtn2)
        btn2 = MDFlatButton(
        text = 'Ok')
        
        self.dialog2 = MDDialog(
            title = 'Tambah akun',
            type="custom",
            content_cls=Content(),
            buttons = [btn1,btn2]
        )
        self.dialog2.open()
    def hasilbtn2(self, obj):
        self.dialog2.dismiss()
        
    #===========================================
    
if __name__ == '__main__':
    Application().run()
