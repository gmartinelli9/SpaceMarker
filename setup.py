import cx_Freeze

executables = [cx_Freeze.Executable('main.py')]

cx_Freeze.setup(
    name="Space Maker",
    options={'build_exe': {'packages':['pygame'],
                           'include_files':['bg.jpg', 'Space_Machine_Power.mp3', 'space.ico', 'space.png']}},

    executables = executables
)
    