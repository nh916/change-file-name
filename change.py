import os

os.chdir('C:\\Users\\username\\Ddirnmae\\dirname\\mydirname')

for f in os.listdir():

	file_name = os.path.splitext(f)[0]
	file_ext = os.path.splitext(f)[1]
	
	if file_name == 'change':
		print('pass')
		continue


	file_name = file_name.replace("150 - ", "")

	file_name = file_name.replace(" - course name", "").strip()
	new_name = f'{file_name}.mp4'

	print(new_name)

	os.rename(f, new_name)
