import ovito
from ovito.vis import * #Allows us to manipulate camera
from ovito import dataset #Tells Ovito to use whatever dataset is currently open

#Viewport object is from ovito.vis
#This is what we will use to directly manipulate camera
vp = Viewport()

#Camera setup info found in "Adjust View" dialogue box
vp.type = Viewport.Type.TOP
vp.camera_pos = (0, 0, 0)
vp.camera_dir = (0,0,-1)
vp.fov = 0.05

for frame in range(0, 50):
	if frame < 30: #for the first 30 frames, do this:
		vp.fov = vp.fov - .001 #zoom in by .001
        #decreasing the fov (field of view) is equivalent to zooming in

	else: #for frames 30 to end, do this:
		dataset.anim.current_frame = frame #progress the animation

    #render as usual (remember to change file location and name)
	rs = RenderSettings(size=(480,480), filename="location/zoom1"+str(frame)+".png", renderer = TachyonRenderer())
	vp.render(rs)
