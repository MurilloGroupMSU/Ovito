import ovito
from ovito.vis import * #Allows us to manipulate camera
from ovito import dataset #Tells Ovito to use whatever dataset is currently open
from math import * #MUST include this to access pi, sin, and cos

#Viewport object is from ovito.vis - This is what we will use to directly manipulate camera
vp = Viewport()

#Camera setup info found in "Adjust View" dialogue box
vp.type = Viewport.Type.PERSPECTIVE
vp.camera_pos = (0, 0, -.25)
vp.camera_dir = (0,0,-1)
vp.fov = pi/16 #fov controls view angle (in radians) when in perspective view type



for frame in range(0, 100):
    dataset.anim.current_frame = frame #increment the animation

    #rotate from top veiw to side view
    if(frame < 13):
        theta = frame * pi/24 + pi/2
        vp.camera_dir = (cos(theta), 0, sin(theta))
        vp.zoom_all() #optimize camera position so it's centered

    #move camera forward (x-direction) into the middle of the ring
    elif(frame < 44):
        vp.camera_pos = (0.31- (frame-12)*.01, 0, 0)

    #calibrate camera position and direction
    elif(frame == 44):
        vp.camera_pos = (0, 0, 0)
        vp.camera_dir = (-1, 0, 0)

    #rotate camera so it's in line with the cylinder
    elif(frame < 58):
        theta = (frame-45)*pi/24 + pi
        vp.camera_dir = (cos(theta), 0, sin(theta))

    #move camera in z-direction, back out of the cylioinder
    elif(frame < 78):
        vp.camera_pos = (0, 0, (frame-57)*.01)


    #from frames 78 to 100, the camera position and direction won't change
    #it will just render the incremented animation from the same perspective

    #render every time
    rs = RenderSettings(size=(480,480), filename="C:/location/example"+str(frame)+".png", renderer = TachyonRenderer())
    vp.render(rs)
