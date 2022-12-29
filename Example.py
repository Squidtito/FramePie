import framepie as fp
#import random
import pygame
#import functools
#import ez_profile
block = [fp.load_image("blocks/grass.png", True),fp.load_image("blocks/stone.png", False)]
x:int=0
z:int=1
camera_x:int=0
camera_y:int=0
current:int
block_size=2
fp.FPS = 60
premath=[]
update = True
maths:int = 0
update_rendering =[1] #Array 0 means rendering for the terrain

world=[]
world_temp=[]
world_size=10 #How big is the world going to be?
world_chunk_size = 6 #How big are chunks?
#sine = [1,2,3,4,5,6,6,5,4,3,2,1] #Testing
z_axis=0
x_axis=0
for _ in range(world_size):
    #Begin creating chunk
    for _ in range(world_size):
        chunk = []
        for x in range(world_chunk_size): #Creating chunk
            for z in range(world_chunk_size):
                chunk.append((x,z,0,0)) #Add block into chunk
                world_temp.append(0)
        world.append([x_axis,z_axis,chunk]) #Add chunk to world. alongside where the chunk should be at.
        x_axis+=1
    z_axis+=1
    x_axis=0


print(len(world))
fp.set_window_background_color((31,31,51))
fp.set_window_resolution((1280/2,720/2))

def generate_premath(blocksize): #This prevents the game from doing a extra pointless amount of math for the block size/camera every frame
        premath.append(0.47*blocksize)
        premath.append(0.45*blocksize)
        premath.append(0.242*blocksize)
        premath.append(0.26*blocksize)

generate_premath(block_size)
while True:
    fp.update()
    maths = 0
    camera_x_old = camera_x
    camera_y_old = camera_y
    if fp.get_input(pygame.K_w):
        if not block_size == 2:
            block_size-=.5
            premath=[]
            maths+=4
            generate_premath(block_size)
    elif fp.get_input(pygame.K_s):
        block_size+=.5
        premath=[]
        maths+=4
        generate_premath(block_size)

    camera_old = (camera_x,camera_y)
    camera_speed=10
    if fp.get_input(pygame.K_RIGHT):
        camera_x-=camera_speed
    elif fp.get_input(pygame.K_LEFT):
        camera_x+=camera_speed
    if fp.get_input(pygame.K_UP):
        camera_y-=camera_speed
    elif fp.get_input(pygame.K_DOWN):
        camera_y+=camera_speed

    current=0
    drawn=0
    z=0

    #camera_view =(round(camera_x/block_size*world_chunk_size),round(camera_y/world_chunk_size))
    #print(camera_view)
    #loaded_chunks=[]
    #for zz in range(camera_view[1]):
    #    for xx in range(camera_view[0]):
    #        loaded_chunks.append(world[xx+zz][2])
    #print(loaded_chunks)

    chunk_count:int=0
    for chunk in world:
        chunk_count+=1
        blockX=chunk[0]*world_chunk_size
        blockZ=chunk[1]*world_chunk_size
        blockY=0

        meth = (
                blockX*premath[0]+camera_x-premath[1]*
                blockZ,
                blockX*premath[2]+premath[3]*
                blockZ-camera_y+
                blockY*premath[1]
                )
        maths+=18
        if meth[0]>=-200 and meth[0]<=800 and meth[1]>=-250 and meth[1]<=450: #Check if chunk is on screen. If so starts processing blocks
            chunk_surface = pygame.Surface((500, 300))
            for i in chunk[2]:
                    current+=1
                    blockX=i[0]+chunk[0]*world_chunk_size
                    blockZ=i[1]+chunk[1]*world_chunk_size
                    blockY=i[2]

                    meth = (
                    blockX*premath[0]+camera_x-premath[1]*
                    blockZ,
                    blockX*premath[2]+premath[3]*
                    blockZ-camera_y+
                    blockY*premath[1]
                    )


                    fp.draw_image(block[i[3]],meth,(block_size,block_size),surface=chunk_surface)
                    drawn+=1
                    maths+=13
            fp.draw_surface(chunk_surface,meth)
                

    fp.set_window_name(str(drawn)+" drawn blocks, " +str(maths)+" math calculations and operations total."+"   FPS: "+str(round(fp.clock.get_fps())))
