from direct.showbase.ShowBase import ShowBase
from panda3d.core import DirectionalLight, AmbientLight

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        block = loader.loadModel('dirt-block.glb')
        block.reparentTo(render)

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