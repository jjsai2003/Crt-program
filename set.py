#create a class f15
#ac displays the room tempreture and outside tempreture which are taken as input
#display-which displays  the differnce between room tempreture and outside tempreture and it also displaysfan speed
class F15:
    def __init__(self) -> None:
     print("The placements of Pragati Enginnering college during 2025 are:")
    def light(sai,color):
     print("The color of light:",color)
    def fans(sai,speed):
      print("The regulatory speed of fans:",speed)
      sai.speed = speed  
    def display(sai,in_temp,out_temp):
      print("The room and outside Temperature:",in_temp,out_temp) 

hari = F15()
hari.light("green")
hari.fans(5)
hari.display(16.0,42.8)
