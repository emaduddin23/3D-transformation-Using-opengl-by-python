#3D_Transformation_Group_6

# Sarder Iftekhar Ahmed
# 2018-1-60-181
# Md. Emad Uddin Aksir
# 2018-1-60-170
# Md. Nadim
# 2018-1-60-161



import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
verticies = ((-1, 1, -1),(1, 1, -1),(1, -1, -1),(-1, -1, -1),(-1, -1, 1),(-1, 1, 1),(1, 1, 1),(1, -1, 1))
edges=((0,1),(0,5),(1,2),(1,6),(2,3),(2,7),(0,3),(3,4),(4,7),(6,7),(5,6),(4,5))
surfaces = ((0,1,2,3),(0,1,6,5),(0,3,4,5),(3,2,7,4),(1,2,7,6),(4,5,6,7),) #quads

def color_in_face(color, face_index):
    for vertex in surfaces[face_index]:
        glColor3fv(color) ##color function
        glVertex3fv(verticies[vertex])

def Cube():
    glBegin(GL_QUADS)
    color_in_face((1,0,0), 0)
    color_in_face((0,1,0), 1)
    color_in_face((0,0,1), 2)
    color_in_face((1,1,0), 3)
    color_in_face((0,1,1), 4)
    color_in_face((1,0,1), 5)
    glEnd()

    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(verticies[vertex])
    glEnd()

def main():
    print("Button tranformation:\n For Rotation use up,down,right,left buttons of your keyboard")
    print("Button tranformation:\n For translate use W,S,A,D buttons of your keyboard")
    print("Button tranformation:\n For sacling use Y,H,G,J buttons of your keyboard")
    print("Button tranformation:\n Use Q to stop the operation")
    to_transform = False
    pygame.init()
    display = (800,600)
    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    gluPerspective(45,  (display[0]/display[1]), 0.1, 70.0)
    glTranslatef(0.0,0.0, -5)
    glRotatef(0,1,0,0)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    to_transform = "left"
                elif event.key == pygame.K_RIGHT:
                    to_transform = "right"
                elif event.key == pygame.K_UP:
                    to_transform = "up"
                elif event.key == pygame.K_DOWN:
                    to_transform = "down"
                elif event.key == pygame.K_a:
                    to_transform = "t-l"
                elif event.key == pygame.K_d:
                    to_transform = "t-r"
                elif event.key == pygame.K_w:
                    to_transform = "t-u"
                elif event.key == pygame.K_s:
                    to_transform = "t-d"
                elif event.key == pygame.K_g:
                    to_transform = "x-"
                elif event.key == pygame.K_j:
                    to_transform = "x+"
                elif event.key == pygame.K_y:
                    to_transform = "y+"
                elif event.key == pygame.K_h:
                    to_transform = "y-"
                elif event.key == pygame.K_q:
                    to_transform = "stop"
                
        if to_transform!=None:
            if to_transform==False:
                glRotatef(0, 0, 0, 0) ##position
            elif to_transform=="left":
                glRotatef(0.5, 0, 1, 0)
            elif to_transform=="right":
                glRotatef(0.5, 0, -1, 0)
            elif to_transform=="up":
                glRotatef(0.5, 1, 0, 0)
            elif to_transform=="down":
                glRotatef(0.5, -1, 0, 0)
            elif to_transform=="t-l":
                glTranslatef(-0.1, 0, 0)
            elif to_transform=="t-r":
                glTranslatef(0.1, 0, 0)
            elif to_transform=="t-u":
                glTranslatef(0, 0.1, 0)
            elif to_transform=="t-d":
                glTranslatef(0, -0.1, 0)
            elif to_transform=="x-":
                glScalef(0.99, 1, 1)
            elif to_transform=="y-":
                glScalef(1, 0.99, 1)
            elif to_transform=="x+":
                glScalef(1.01, 1, 1)
            elif to_transform=="y+":
                glScalef(1, 1.01, 1)
            elif to_transform=="stop":
                glTranslatef(0.0, 0.0, 0)
                glRotatef(0, 0, 0, 0)
        glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT) #to clear previous operation and add new operaiton
        Cube()
        pygame.display.flip() # new display flip 
        pygame.time.wait(10) # display delay 10 nanosec
if __name__=="__main__":
    main()