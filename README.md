# wallpaper_changer
This python application, randomly changes your wallpaper from a given folder

How to use this:
- edit the "wallpaper_changer.py" file in an editor
- edit the line foler = r"... => by typing your folder with wallpers in this variable:
- after edit, this line looks like: 
        folder = r"__filepath__"
- |--> where the __filepath__ is the folder's path
- save your file 
- assuming that you have python already installed in your pc: just when you double-click this python file, the wallpaper changes!




If you want change your wallpaper whenever windows starts up
- open your command prompt
- type "pip install pyinstaller" => install some required software
- now, open windows power shell
- type command: cd "__path_where_the_.py_file_is_downloaded__" => current working directory changes to the the file where the wallpaper_changer.py file is present
- type: pyinstaller --onefile -w 'filename.py'
- after hitting enter => some files will appear, our application file (.exe file) will be placed in in the folder called : "dist"
- create a shortcut for this .exe file
- press windowskey+R, type: shell:startup , and click 'OK'
- this opens up the 'Startup' folder
- now place the created shortcut here. and close the folder
=> this will make the wallpaper_changer.exe application run everytime windows startsup


- report any anamolies here in comment or @email = rohitathithya@gmail.com
