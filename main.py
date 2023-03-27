from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.loadModels()
        self.setupLights()
        self.setupCamera()
        self.setupSkybox()
        self.generateWorld()

    def setupCamera(self):
        self.disableMouse()
        self.camera.setPos(50, -50, 50)
        self.camera.lookAt(0, 0, 0)

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