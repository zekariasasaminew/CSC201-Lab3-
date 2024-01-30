from graphics2 import *
def createWindow():
    window = GraphWin(f'Click to get triangles', 500, 600)
    window.setBackground('white')
    return window
def threeClick(window):
    for num in range(3):
        click = window.getMouse()
    return click
def drawTriangle(window, click):
    for num in range(3):
        x = click.getX()
        y = click.getY()
        triangle = Polygon(x, y)
        triangle.setFill('cyan')
        triangle.draw(window)
    return triangle
def main():
    w = input('Would you like a triangle? ')
        
    window = createWindow()
    click = threeClick(window)
    drawTriangle(window, click)
main()
        
        