from tkinter import Tk, Canvas

WIDTH = 800
HEIGHT = 600

lines = []

def main():
    #print(len(lines))
    root.bind("<Button-1>", create_line)
    if len(lines) != 0:
        root.bind('<Motion>', motion)
    root.after(20, main)
    
def motion(event):
    if 'line' in globals():
        lines[len(lines) -1].delete_line()
    lines[len(lines) -1].draw_line(event.x, event.y)
    
    
def create_line(event):
    #if line != None:
    #    lines.append(line)
    lines.append(Line(event.x, event.y))


class Line(object):
    line = None
    x1 = None
    y2 = None
    def __init__(self, x1, y1):
        self.x1 = x1
        self.y1 = y1
    
    def draw_line(self, x2, y2):
        if self.x1 != None and self.y1 != None:
            self.line = c.create_line (self.x1, self.y1, x2, y2)
        
    def delete_line(self):
        if self.line != None:
            c.delete(self.line)

# Setting up window
root = Tk()
c = Canvas(root, width=WIDTH, height=HEIGHT)
c.grid() 
c.focus_set()

main()
#start_game()
root.mainloop()

