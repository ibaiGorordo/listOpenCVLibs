import glob
import os

library_path = "C:/OpenCV/Build/x64/vc16"
opencvLibs = glob.glob(library_path + '/*.lib')

for lib in opencvLibs:
	print(os.path.basename(lib))