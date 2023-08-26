import kivy
from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.widget import Widget
from kivy.core.window import Window

Window.size = (500,600)

Builder.load_file("culcutor.kv")


class Calculator(Widget):
    def number(self,values):
        result = self.ids.my_number.text
        if result == str(0):
            result= ''
            self.ids.my_number.text = f'{result}{str(values)}'
        else:
            self.ids.my_number.text = f'{result}{str(values)}'
    def maths(self,sign):
        result = self.ids.my_number.text
        self.ids.my_number.text = f'{result}{sign}'
    def clear(self):
        self.ids.my_number.text = '0'
    def remove(self):
        result = self.ids.my_number.text
        self.ids.my_number.text = f'{result[:-1]}'

    def change(self):
        result = self.ids.my_number.text
        if "-" in result:
            self.ids.my_number.text = f'{result.replace("-","")}'
        else:
            self.ids.my_number.text = f'-{result}'

    def dot(self):
        result = self.ids.my_number.text
        numbersplit = result.split("+")

        if "+" in result and "." not in numbersplit[-1]:
            self.ids.my_number.text = f'{result}.'
        elif "." in result:
            pass
        else:
            self.ids.my_number.text = f'{result}.'


    def evalnumber(self):
        result = self.ids.my_number.text
        self.ids.my_number.text = f'{eval(result)}'

    def sign(self):
        result = self.ids.my_number.text
        answer = result+'/100'
        self.ids.my_number.text = f'{eval(answer)}'



class  MyFisrtcalculator(App):
    def build(self):
        return Calculator()


MyFisrtcalculator().run()