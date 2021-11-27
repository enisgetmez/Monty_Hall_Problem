import random
import matplotlib.pyplot as plt

class monty_hall:
	def __init__(self):
		self.car_and_goats = ["goat","goat","car"]
		self.user_prize = 0
		self.shuffle()

	def shuffle(self):
		random.shuffle(self.car_and_goats)

	def choice(self,choice):
		self.user_choice = choice
		self.user_prize = self.car_and_goats[self.user_choice]
		del self.car_and_goats[self.user_choice]
	def monty_proposal(self):
		if(self.car_and_goats[0] == "goat"):
			del self.car_and_goats[0]
		else:
			del self.car_and_goats[1]
	def monty_accept(self,accept=False):
		if(accept == True):
			self.user_prize = self.car_and_goats[0]
	def prize(self):
		return self.user_prize

def bar(wins,winc,losss,lossc):
	plt.bar("win staying",wins,color="g",width=0.25)
	plt.bar("win changing",winc,color="g",width=0.25)
	plt.bar("loss staying",losss,color="r",width=0.25)
	plt.bar("loss changing",lossc,color="r",width=0.25)
	plt.show()

win_staying = 0
win_changing = 0
loss_staying = 0
loss_changing = 0
for i in range(30):
	m = monty_hall()
	m.choice(1) 
	#m.choice(random.randint(0,2)) #random choice
	m.monty_proposal()
	if(m.prize() == "car"):
		win_staying +=1
	else:
		loss_staying +=1
	m.monty_accept(True)
	if(m.prize() == "car"):
		win_changing +=1
	else:
		loss_changing +=1

bar(win_staying,win_changing,loss_staying,loss_changing)
