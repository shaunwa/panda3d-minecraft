from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        dirtBlock = loader.loadModel('dirt-block.glb')
        dirtBlock.reparentTo(render)
        dirtBlock.setHpr(0, 90, 0)

        stoneBlock = loader.loadModel('stone-block.glb')
        stoneBlock.reparentTo(render)
        stoneBlock.setPos(0, 2, 0)
        stoneBlock.setHpr(0, 90, 0)

        grassBlock = loader.loadModel('grass-block.glb')
        grassBlock.reparentTo(render)
        grassBlock.setPos(0, -2, 0)
        grassBlock.setHpr(0, 90, 0)

        dirtBlock = loader.loadModel('dirt-block.glb')
        dirtBlock.reparentTo(render)

        mainLight = DirectionalLight('main light')
        mainLightNodePath = render.attachNewNode(mainLight)
        mainLightNodePath.setHpr(30, -60, 0)
        render.setLight(mainLightNodePath)

        ambientLight = AmbientLight('ambient light')
        ambientLight.setColor((0.4, 0.4, 0.4, 1))
        ambientLightNodePath = render.attachNewNode(ambientLight)
        render.setLight(ambientLightNodePath)

        self.disableMouse()
        self.camera.setPos(10, -10, 10)
        self.camera.lookAt(0, 0, 0)

game = Game()
game.run()