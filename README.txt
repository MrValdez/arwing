*Keys*

Use the arrow keys to rotate the model. WASD to move it around. Q and E to make the model disappear. Page Up and Page Down to do a **Barrel Roll**.

ESCape to quit.

----

*Videos*

Demo
- https://youtu.be/wkfOfQf_ERM

Spongebob test
- https://youtu.be/a2IJSjR_Fnw

----

*Why*

So, I woke up with a weird itch. For some very odd reason, I want to make a Python program of a 3D model. ...and I kept hearing the phrase "DO A BARREL ROLL" in my head. So, that's what I did.

I've done OpenGL years ago in C. And I've been looking for an excuse to do OpenGL on Python. My excuse all these times was that I wanted to wait for a Vulkan-Python bindings, since its the next evolution of OpenGL. But that coding itch have finally became loud enough (DO A BARREL ROLL) that after having my morning coffee, I sat down and code.

I've found an Arwing model on the Internet and it was perfect. It was even in OBJ format, the one format that I worked on when I started OpenGL! 

Fun fact: it was Blender that exposed me to Python all those years ago when I needed to export to OBJ. So I had a cute nostalgia trip while searching for a model.

While making the program, I couldn't figure out some rendering bugs. I suspected that I was loading the OBJ file wrong, so I downloaded a simplier cube model to test. I looked for a Spongebob image for the cube sides because, why not.

When I finally got it working, the UV wasn't perfect, resulting in a perspective trick, which I decided to keep and make a video of.

Finally, I originally wanted to push spacebar or push a button on a joystick to **DO A BARREL ROLL**. But instead, I went to the lazy approach of just rotating the model with the origin far from the model.

-----

*Weird behavior*

This is just meant to be a one-off code. I know the bugs and what to do to fix them. 

** Q and E keys **

Use the arrow keys to rotate the model. WASD to move it around. Q and E to make the model disappear.

Now it might be odd that the E and Q keys doesn't change the Z axis. This is because we are in Orthographic mode instead of Perspective mode. I was planning to go into Perspective mode but I like the effect of the Arwin disappearing section-by-section. I know that the reason for that is that I'm moving the camera and that the model reaches the far plane and becomes unrenderable. But the effect is very pretty, so I kept it.

** Rotation **

If you look at the code, the keys for axis mapping is wrong. That's the camera has an initial rotation. The proper way to do this is to have a camera class and rotate that instead of doing it directly. But I don't want to do implement any Quaternion technology, so this is fine as is. If I have more time, I would have made a proper camera system.

** Background **

Because I neglected the camera code AND I didn't use a proper Perspective matrix, I basically can't put up a skybox. Oh well.

....I had that itch again and I've added simple stars (more like dusts, actually) to the background. Yay.

-----

Arwing model downloaded from: http://www.models-resource.com/gamecube/starfoxassault/model/8646. The readme claim that its a ripped model.
Cube model downloaded from: http://www.opengl-tutorial.org/beginners-tutorials/tutorial-7-model-loading/
SpongeBob model downloaded from: https://pbs.twimg.com/profile_images/420241225283674113/xoCDeFzV_400x400.jpeg

-----
*Resource*

For tutorial, I used this: https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial

But if you are a beginner on OpenGL, I don't suggest this tutorial. Personally, I learned OpenGL on nehe.gamedev.net and with an OpenGL book (OpenGL Game Programming by Kevin Hawkins). I'm unsure if the NeHe Python translation (http://pyopengl.sourceforge.net/context/tutorials/index.html) is a good translation on the original C code that I grew up with.

-----

# Resources links:
#  - http://aosabook.org/en/500L/a-3d-modeller.html
#  - http://pyopengl.sourceforge.net/context/tutorials/index.html
#  - http://pyopengl.sourceforge.net/documentation/opengl_diffs.html
#  - https://pythonprogramming.net/opengl-rotating-cube-example-pyopengl-tutorial/
#  - https://en.wikipedia.org/wiki/Wavefront_.obj_file
#  - http://stackoverflow.com/questions/22185654/rendering-obj-files-with-opengl
#  - http://stackoverflow.com/questions/11125827/how-to-use-glbufferdata-in-pyopengl
#  - http://pygame.org/wiki/SimpleOpenGL2dClasses?parent=
#  - http://www.opengl-tutorial.org/beginners-tutorials/tutorial-7-model-loading/
#  - http://www.pygame.org/wiki/OBJFileLoader
