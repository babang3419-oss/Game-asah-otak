from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button

class AsahOtakApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', padding=30, spacing=20)
        
        self.label = Label(
            text='Game Asah Otak\nSiap menguji kemampuanmu?', 
            font_size=22, 
            halign='center', 
            valign='middle'
        )
        self.label.bind(size=self.label.setter('text_size'))
        
        btn = Button(
            text='Mulai Bermain', 
            font_size=18, 
            size_hint=(1, 0.25)
        )
        btn.bind(on_press=self.ubah_teks)
        
        layout.add_widget(self.label)
        layout.add_widget(btn)
        return layout

    def ubah_teks(self, instance):
        self.label.text = 'Pertanyaan:\nBerapa hasil dari 5 + 5 x 2?\n\nA. 20\nB. 15\nC. 25'

if __name__ == '__main__':
    AsahOtakApp().run()
