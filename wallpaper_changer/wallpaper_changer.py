import os, random, ctypes
folder = r"C:\Users\ADMIN\Desktop\Rohit\wallpapers"
wallpaper_path = random.choice(os.listdir(folder))
print(wallpaper_path)
ctypes.windll.user32.SystemParametersInfoW(20, 0, folder + "\\" + wallpaper_path , 0)