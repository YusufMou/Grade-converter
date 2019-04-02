from tkinter import *

root = Tk()
root.title("Grading System")
root.geometry("500x300")

user =  Label(root, text="Enter a level below. (Levels are R to 4+)").grid(row=1, column=1)
box = Entry(root)
box.grid(row=2, column= 1)

def grade():
	lv = str(box.get())
	if lv == '4+':
		la = Label(root, text="Your grade is 97%").grid(row=4, column=1)
	elif lv == '4':
		la = Label(root, text="Your grade is 91%").grid(row=4, column=1)
	elif lv == '4-':
		la = Label(root, text="Your grade is 83%").grid(row=4, column=1)	
	elif lv == '3+':
		la = Label(root, text="Your grade is 78%").grid(row=4, column=1)
	elif lv == '3':
		la = Label(root, text="Your grade is 74.5%").grid(row=4, column=1)
	elif lv == '3-':
		la = Label(root, text="Your grade is 71%").grid(row=4, column=1)				
	elif lv == '2+':
		la = Label(root, text="Your grade is 68%").grid(row=4, column=1)				
	elif lv == '2':
		la = Label(root, text="Your grade is 64.5%").grid(row=4, column=1)				
	elif lv == '2-':
		la = Label(root, text="Your grade is 61%").grid(row=4, column=1)				
	elif lv == '1+':
		la = Label(root, text="Your grade is 58%").grid(row=4, column=1)				
	elif lv == '1':
		la = Label(root, text="Your grade is 54.5%").grid(row=4, column=1)				
	elif lv == '1-':
		la = Label(root, text="Your grade is 51%").grid(row=4, column=1)				
	elif lv == 'R':
		la = Label(root, text="You grade is below 50%").grid(row=4, column=1)	
	else:
		la = Label(root, text="Error. Try again").grid(row=4, column=1)				


sub = Button()
sub ["text"] = "Submit"
sub ["command"] = grade
sub.grid(row=3, column=1)


root.mainloop()