import cx_Freeze
executables = [
    cx_Freeze.Executable(script="main.py", icon="space.ico")
]
cx_Freeze.setup(
    name = "Space Maker",
    options = {
        "build_exe":{
            "packages": ["pygame"]
        }
    } , executables = executables
)