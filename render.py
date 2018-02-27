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
    dataset.anim.current_frame = frame #This progresses the animation to the next frame

    #settings for rendering - make sure to change the location and file name!
    rs = RenderSettings(size=(480,480), filename="location/fileName"+str(frame)+".png", renderer = TachyonRenderer())

    vp.render(rs) #render the image using the specified settings
