import ovito
from ovito.vis import * #Allows us to manipulate camera
from ovito import dataset #Tells Ovito to use whatever dataset is currently open
from math import * #MUST include this to access pi, sin, and cos

vp = Viewport() #Viewport object is from ovito.vis - This is what we will use to directly manipulate camera

#Camera setup info found in "Adjust View" dialogue box
vp.type = Viewport.Type.ORTHO
vp.camera_pos = (0, 0, 0)
vp.camera_dir = (0,0,-.5)
vp.fov = .05


for frame in range(0, 50):
	dataset.anim.current_frame = frame #increment the animation

    #create theta based on "frame" so that as frame increments, the camera will rotate around
    #the smaller your theta, the less it will rotate in each frame
	theta = frame *pi / 12

    #choose one coordinate to be constant
        #that's the axis you'll rotate around
        #and the magnitude of the constant determines the angle of the camera
    #set the other two to cos(theta) and sin(theta)
	vp.camera_dir = (cos(theta), sin(theta), -.5)

    #render as usual (remember to change file location and name)
	rs = RenderSettings(size=(480,480), filename="location/zoom1"+str(frame)+".png", renderer = TachyonRenderer())
	vp.render(rs)
