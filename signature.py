from PIL import Image,ImageFont,ImageDraw
import random
import os
import sys
import io
import datetime
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding = 'utf-8')

# Get the current date and time
current_time = datetime.datetime.now()

# Format the current time as a string
formatted_time = current_time.strftime("%Y-%m-%d_%H-%M-%S")

# Use the formatted time as the file name
file_name = "result_" + formatted_time + ".png"

content = sys.argv[1]
# content = '<p><span class="h-card"><a href="https://bgme.me/@ciao" class="u-url mention">@<span>ciao</span></a></span> 奇遇</p><p>第一句话<br />不出所料电信号'

# 拆出最后1行的文本，返回
def split_content(text):
    if text[-4:] != '</p>':
        text += '</p>'
    my_string = text[108:]
    my_string = my_string[:-4]
    # print(my_string)
    i = len(my_string)
    flag4 = 0
    while i != 0:
        i-=1
        if my_string[i] == '>':
            flag4 = i
            break
    if flag4 != 0:
        poem_line = my_string[flag4+1:]
        return(poem_line)
    else:
        return("[啊哦！数据传输出现问题]")

full_name = split_content(content)
# print(len(full_name))
 
class ImageChar():

	def __init__(self, color=(0,0,0),size=(100,30),
		fontlist=['./fonts/'+i for i in os.listdir('./fonts/') if not i =='.DS_Store'],
		fontsize=20,
		num_word=4):#生成多少个字的验证码（图片宽度会随之增加）
 
		self.num_word=len(full_name)
		self.color=color
 
		self.fontlist=fontlist
 
		if self.num_word==4:
			self.size=size
		else:
			self.size=((20+5)*self.num_word,40)
 
		#随机挑选一个字体 randint(0,2)会取0，1，2 所以减去 1
		self.fontpath=self.fontlist[random.randint(0,len(self.fontlist)-1)]
		self.fontsize=fontsize
 
		# self.chinese=open('3500.txt','r',encoding='utf-8').read()
 
		self.font=ImageFont.truetype(self.fontpath, self.fontsize)
	
	#随机生成杂线的坐标
	def rand_line_points(self,mode=0):
		width,height=self.size
		if mode==0:
			return (random.randint(0, width), random.randint(0, height))
		elif mode==1:
			return (random.randint(0,6),random.randint(0, height))
		elif mode==2:
			return (random.randint(width-6,width),random.randint(0, height))

	def draw_heart(self, draw_obj, position, size, color):
		x, y = position
		w, h = size
		draw_obj.polygon([(x, y + h//4), (x + w//2, y),
                          (x + w, y + h//4), (x + w, y + h),
                          (x, y + h), (x, y + h//4)], fill=color)

	def draw_circle(self, draw_obj, position, radius, color):
		x, y = position
		draw_obj.ellipse([(x - radius, y - radius), (x + radius, y + radius)], fill=color)

	def draw_triangle(self, draw_obj, position, size, color):
		x, y = position
		w, h = size
		draw_obj.polygon([(x, y), (x + w, y), (x + w//2, y + h)], fill=color)

	def draw_square(self, draw_obj, position, size, color):
		x, y = position
		w, h = size
		draw_obj.rectangle([(x, y), (x + w, y + h)], fill=color)

	#随机生成一张验证码，并且返回 四个汉字的字符串，测试用
	def rand_img_test(self,num_lines=4,num_shapes=4):
		width,height=self.size
		gap=5
		start=0
		num_lines = random.randint(0,4)
		num_shapes = random.randint(0,5)
 
		#第一张，带噪音的验证码
		self.img1 = Image.new('RGB',self.size,(255,255,255))
		self.draw1=ImageDraw.Draw(self.img1)
 
		#把线画上去
		for i in range(num_lines//2):
			self.draw1.line([self.rand_line_points(),self.rand_line_points()],(0,0,0))
		for i in range(num_lines//2):
			self.draw1.line([self.rand_line_points(1),self.rand_line_points(2)],(0,0,0))
		
		# 画图形
		for i in range(num_shapes):
			x = random.randint(0, width)
			y = random.randint(0, height)
			shape_type = random.choice(["heart", "circle", "triangle", "square"])
			size = random.randint(1, 20)
			# color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
			color = (128,128,128)

			if shape_type == "heart":
				self.draw_heart(self.draw1, (x, y), (size, size), color)
			elif shape_type == "circle":
				self.draw_circle(self.draw1, (x, y), size, color)
			elif shape_type == "triangle":
				self.draw_triangle(self.draw1, (x, y), (size, size), color)
			else:
				self.draw_square(self.draw1, (x, y), (size, size), color)
			
		words=full_name
		#将汉字画上去
		for i in range(len(words)):
			x=start+(self.fontsize+gap)*i+random.randint(0,gap)
			y=random.randint(0,height-self.fontsize-gap)
			# cr = random.randint(0,255)
			# cg = random.randint(0,255)
			# cb = random.randint(0,255)
			self.draw1.text((x,y),words[i],fill=(0,0,0),font=self.font)
		return self.img1,words

ic = ImageChar()
img, word = ic.rand_img_test(4)
filename="./signature/" + file_name
with open(filename,'wb') as f:
	img.save(f,format='png')
print(file_name)