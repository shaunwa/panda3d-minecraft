from setuptools import setup

setup(
    name = "My Minecraft Clone",
    options = {
        "build_apps" : {
            "include_patterns" : [
                "**/*.png",
                "**/*.glb",
                "**/*.egg",
                "**/*.txt",
            ],
            "gui_apps" : {
                "My Minecraft Clone" : "main.py"
            },
            "plugins" : [
                "pandagl",
            ],
            "platforms" : [
                # "manylinux1_x86_64",
                "macosx_10_6_x86_64",
                # "win_amd64"
            ],
            "log_filename" : "/Users/swassell/panda3d/minecraft-key/output.log",
            "log_append" : False
        }
    }
)