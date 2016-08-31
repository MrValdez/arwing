import pygame
import OpenGL

from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

from array import array     # http://stackoverflow.com/questions/11125827/how-to-use-glbufferdata-in-pyopengl

def Cube():
    vertices= (
        (1, -1, -1),
        (1, 1, -1),
        (-1, 1, -1),
        (-1, -1, -1),
        (1, -1, 1),
        (1, 1, 1),
        (-1, -1, 1),
        (-1, 1, 1)
        )
    uv = (
        (1, 0),
        (1, 1),
        (0, 1),
        (0, 0),
        (0, 1),
        (0, 0),
        (0, 1),
        (1, 1),
        )
    edges = (
        (0,1),
        (0,3),
        (0,4),
        (2,1),
        (2,3),
        (2,7),
        (6,3),
        (6,4),
        (6,7),
        (5,1),
        (5,4),
        (5,7)
        )

    glBindTexture(GL_TEXTURE_2D, 0)
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glTexCoord2fv(uv[vertex])
            glVertex3fv(vertices[vertex])
    glEnd()

def load_model(modelname):
    vertices = []
    texture_vertices = []
    groups = []
    group_buffer = []

    with open(modelname) as f:
        for line in f:
            if line[0] == '#':
                continue
            line = line.strip('\n').split(' ')
            if line[0] == 'v':
                vertex = [float(v) for v in line[1:]]
                vertices.append(vertex)
            if line[0] == 'vt':
                vertex = [float(v) for v in line[1:]]
                texture_vertices.append(vertex)
            if line[0] == 'usemtl':
                material_name = line[1]
                groups = groups + [group_buffer]
                group_buffer = [material_name]
            if line[0] == 'f':
                group = []
                for faces in line[1:]:
                    faces = faces.split('/')
                    faces = [int(data) - 1 for data in faces]   # indexes in obj starts with 1
                    group += [faces]
                group_buffer.append(group)

    groups = groups + [group_buffer]
    groups = [group for group in groups if len(group)]  # remove empty lists

    return vertices, texture_vertices, groups

def load_image(image):
    # http://pygame.org/wiki/SimpleOpenGL2dClasses?parent=
    textureSurface = pygame.image.load(image)
 
    textureData = pygame.image.tostring(textureSurface, "RGBA", 1)
 
    width = textureSurface.get_width()
    height = textureSurface.get_height()
 
    texture = glGenTextures(1)
    glBindTexture(GL_TEXTURE_2D, texture)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexParameteri(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, GL_RGBA, width, height, 0, GL_RGBA,
        GL_UNSIGNED_BYTE, textureData)

    return texture, width, height

def load_textures(groups):
    textures = {}
    for group in groups:
        material_name = group[0]
        texture = load_image("model/{}.png".format(material_name))

        textures[material_name] = texture
    return textures

def draw_point(vertices):
    glBegin(GL_POINTS)
    for vertex in vertices:
        glVertex3fv(vertex)
    glEnd()

def draw_model(groups, vertices, texture_vertices, textures):
    for group in groups:
        material_name = group[0]
        texture = textures[material_name][0]
        glBindTexture(GL_TEXTURE_2D, texture)
        
        #glBufferData(GL_ARRAY_BUFFER, vertices.size() * sizeof(glm::vec3), &vertices[0], GL_STATIC_DRAW);
        ## http://stackoverflow.com/questions/11125827/how-to-use-glbufferdata-in-pyopengl
        #arr = array("f",vert)
        #glBufferData(GL_ARRAY_BUFFER, arr.tostring(), GL_STATIC_DRAW)
        #continue

        glBegin(GL_TRIANGLES)
        for face in group[1:]:
            for v, vt in face:
                glTexCoord2fv(texture_vertices[vt])
                glVertex3fv(vertices[v])
        glEnd()

def main():
    isRunning = True
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    aspect_ratio = display[0] / display[1]
    gluPerspective(120, aspect_ratio, 0.3, 10.0)

    glEnable(GL_TEXTURE_2D)
    glFrontFace(GL_CCW)

    camera_pos = [0, 0.1, 0]
    camera_rot = [0, 0, 0]

    modelname = "model/arwing.obj"
    modelname = "model/cube.obj"

    vertices, texture_vertices, groups = load_model(modelname)
    textures = load_textures(groups)

    while isRunning:
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        glTranslatef(*camera_pos)
        glRotatef(camera_rot[0], 1, 0, 0)
        glRotatef(camera_rot[1], 0, 1, 0)
        glRotatef(camera_rot[2], 0, 0, 1)

#        Cube()
        
        glPushMatrix()
        glTranslatef(0, 0, 0.3)
        glScalef(0.25, 0.25, 0.25)
        #draw_point(vertices)
        draw_model(groups, vertices, texture_vertices, textures)
        glPopMatrix()

        pygame.display.flip()

        keys = pygame.key.get_pressed()
        x, y, z = 0, 0, 0
        speed = 0.3
        if keys[pygame.K_ESCAPE]:
            isRunning = False
        if keys[pygame.K_LEFT]:
            y = -1
        if keys[pygame.K_RIGHT]:
            y = +1
        if keys[pygame.K_UP]:
            x = -1
        if keys[pygame.K_DOWN]:
            x = +1
        if keys[pygame.K_PAGEUP]:
            z = -1
        if keys[pygame.K_PAGEDOWN]:
            z = +1
        camera_rot[0] += speed * x
        camera_rot[1] += speed * y
        camera_rot[2] += speed * z
        
        x, y, z = 0, 0, 0
        if keys[pygame.K_a]:
            x = -1
        if keys[pygame.K_d]:
            x = +1
        if keys[pygame.K_w]:
            y = -1
        if keys[pygame.K_s]:
            y = +1
        if keys[pygame.K_q]:
            z = -1
        if keys[pygame.K_e]:
            z = +1
        x *= 0.1
        y *= 0.1
        z *= 0.1
        camera_pos = [camera_pos[0] + x,
                      camera_pos[1] + y,
                      camera_pos[2] + z,]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False

    pygame.quit()
    quit()
main()