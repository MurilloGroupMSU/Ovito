import ovito
from ovito.vis import * #Allows us to manipulate camera
from ovito import dataset #Tells Ovito to use whatever dataset is currently open

#Viewport object is from ovito.vis
#This is what we will use to directly manipulate camera
vp = Viewport()

#Camera setup info found in "Adjust View" dialogue box
vp.type = Viewport.Type.PERSPECTIVE
vp.camera_pos = (0, 0, 0.06)
vp.camera_dir = (0,0,-1)
vp.fov = 20


for frame in range(0, 100):
	dataset.anim.current_frame = frame #increment the animation

    #Start with the original camera position (0, 0, 0.06)
    #Increment the coordinate you want to change (in this case, it's z)
    vp.camera_pos = (0, 0, .06 - .0003*frame)

    #render as usual (remember to change file location and name)
	rs = RenderSettings(size=(480,480), filename="location/zoom1"+str(frame)+".png", renderer = TachyonRenderer())
	vp.render(rs)
