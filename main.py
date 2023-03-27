from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight
from panda3d.core import WindowProperties
from panda3d.core import TransparencyAttrib
from direct.gui.DirectGui import *
from direct.gui.OnscreenImage import OnscreenImage 

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.loadModels()
        self.setupLights()
        self.setupCamera()
        self.setupPauseScreen()
        self.setupSkybox()
        self.generateWorld()
        self.setupControls()
        self.captureMouse()
        self.setupTasks()

    def update(self, task):
        dt = globalClock.getDt()

        if self.cameraSwingActivated:
            self.moveCameraWithMouse(dt)

        return task.cont

    def moveCameraWithMouse(self, dt):
        md = self.win.getPointer(0)
        mouseX = md.getX()
        mouseY = md.getY()
        mouseChangeX = mouseX - self.lastMouseX
        mouseChangeY = mouseY - self.lastMouseY

        currentH = self.camera.getH()
        currentP = self.camera.getP()

        self.camera.setHpr(
            currentH - mouseChangeX * dt * self.cameraSwingFactor,
            min(90, max(-90, currentP - mouseChangeY * dt * self.cameraSwingFactor)),
            0
        )

        self.lastMouseX = mouseX
        self.lastMouseY = mouseY

    def setupTasks(self):
        taskMgr.add(self.update, 'update')

    def setupCamera(self):
        self.disableMouse()

        self.cameraSwingFactor = 10

        self.camera.setPos(0, 0, 3)
        self.camLens.setFov(80)

        icon = OnscreenImage(image = "crosshairs.png",
                        pos = (0, 0, 0),
                        scale = 0.05)
        icon.setTransparency(TransparencyAttrib.MAlpha)
    
    def setupControls(self):
        self.accept('escape', self.releaseMouse)
    
    def captureMouse(self):
        md = self.win.getPointer( 0 )
        self.lastMouseX = md.getX()
        self.lastMouseY = md.getY()

        self.cameraSwingActivated = True
        properties = WindowProperties()
        properties.setCursorHidden(True)
        properties.setMouseMode(WindowProperties.M_relative)
        self.win.requestProperties(properties)
        self.pauseScreen.hide()

    def releaseMouse(self):
        self.cameraSwingActivated = False
        properties = WindowProperties()
        properties.setCursorHidden(False)
        properties.setMouseMode(WindowProperties.M_absolute)
        self.win.requestProperties(properties)
        self.pauseScreen.show()
    
    def setupPauseScreen(self):
        self.pauseScreen = DirectDialog(text = 'Paused...',
                                frameSize = (-0.7, 0.7, -0.7, 0.7),
                                fadeScreen = 0.4,
                                relief = DGG.FLAT)
                            
        btn = DirectButton(text = "Resume",
            command = self.captureMouse,
            pos = (0, 0, -0.2),
            parent = self.pauseScreen,
            scale = 0.05)

        self.pauseScreen.hide()

    def loadModels(self):
        self.dirtBlock = loader.loadModel('dirt-block.glb')
        self.dirtBlock.setHpr(0, 90, 0)

        self.stoneBlock = loader.loadModel('stone-block.glb')
        self.stoneBlock.setHpr(0, 90, 0)

        self.grassBlock = loader.loadModel('grass-block.glb')
        self.grassBlock.setHpr(0, 90, 0)

    def setupSkybox(self):
        self.skybox = loader.loadModel('skybox')
        self.skybox.setScale(512)
        self.skybox.setBin('background', 1)
        self.skybox.setDepthWrite(0)
        self.skybox.setLightOff()
        self.skybox.reparentTo(render)

    def generateWorld(self):
        for z in range(10):
            for x in range(20):
                for y in range(20):
                    newBlockNode = render.attachNewNode("new-box-placeholder")

                    newBlockNode.setPos(
                        x * 2 - 20,
                        y * 2 - 20,
                        -z * 2,
                    )

                    if z == 0:
                        self.grassBlock.instanceTo(newBlockNode)
                    else:
                        self.dirtBlock.instanceTo(newBlockNode)


    def setupLights(self):
        mainLight = DirectionalLight('main light')
        mainLightNodePath = render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        render.setLight(mainLightNodePath)

        ambientLight = AmbientLight('ambient light')
        ambientLight.setColor((0.4, 0.4, 0.4, 1))
        ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNodePath)


game = Game()
game.run()