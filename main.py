import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
from kivy.core.window import Window
import math
Builder. load_file("calc.kv")

#Window.size = (500,700)

class Interface(Widget):
          
     def clear(self):
          self.ids.calc_input.text = ""
          
     # Creating a button for each function
     def button_press(self, button):
          prior = self.ids.calc_input.text
          if "Invalid Syntax" in prior:
               prior = ""
          
             # creating an if statement
          if prior == "":
               self.ids.calc_input.text = ""
               self.ids.calc_input.text = f"{button}"
               
          else:
               self.ids.calc_input.text = f"{prior}{button}"
               
               #creating a sign function
     def math_sign(self, sign):
          prior = self.ids.calc_input.text
          # sign functions sign
          self.ids.calc_input.text = f"{prior}{sign}" 

                              
     def dot(self):
          prior = self.ids.calc_input.text
          #spliting the textinput by +
          num_list = prior.split("+")
          if "+" in prior and "." not  in num_list[-1]:
            prior = f'{prior}.'
            self.ids.calc_input.text = prior   
          #adding decimal to number
          elif "." in prior:
               pass
          else:
               prior = f'{prior}.'
               self.ids.calc_input.text = prior

         #creating an equals to function
         
     def equals(self):
          prior = self.ids.calc_input.text
          try:
               answer = eval(prior)
               self.ids.calc_input.text = str(answer)
          except:
                self.ids.calc_input.text = "Invalid Syntax"
          #Addition
#          if "+" in prior:
#                              num_list = prior.split("+")
#                              answer = 0.0
#                              #loop thru function
#                              for number in num_list:
#                                   answer = answer + float(number)
#                                   
                              
                                   
     
     def remove(self):
        prior = self.ids.calc_input.text
        prior = prior[: -1]       
        self.ids.calc_input.text = prior 


     def pos_neg(self):
        prior = self.ids.calc_input.text
        if "-" in prior:
                         self.ids.calc_input.text = f'{prior.replace("-", "")}'
        else:
                         self.ids.calc_input.text = f'-{prior}'                     
        
class CalculatorApp(App):
     def build(self):
          Window.clearcolor = (37/255,37/255,37/255,1)
          return Interface()

if __name__ == '__main__':
     CalculatorApp().run()
     
