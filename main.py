import os       #we use os functions for working with the files (make dir , rename and etc)


image = ['tif','tiff','bmp','jpg','jpeg','gif','png','eps','raw','cr2','nef','orf',
'sr2','apng','avif','jfif','pjpeg','pjp','svg','webp']  #all image formats we want to rearrange

audio = ['3gp','aa','aac','aax','act','aiff','amr','ape','awb','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p',
'mmf','mp3','mpc','msv','nmf','ogg','oga','mogg','opus','rm','ra','rf64','sln','tta','voc','vox','wav','wma','wv','webm','8svx','cda'] #all audio formats we want to rearrange

video = ['webm','mkv','flv','flv','vob','ogv','ogg','drc','gif','gifv','mng','avi','MTS','M2TS','mov','qt','wmv','yuv','rmvb','viv','asf',
'amv','mp4','m4p','m4v','mpg','mp2','mpeg','mpe','mpv','mpg','mpeg','m2v','m4v','svi','3gp','3g2','mxf','roq','Fflv'] #all video formats we want to rearrange

document = ['doc','fb2','md','docx','odt','sxw','pages','pdf','ps','rtf','wp7','wp','wpd','txt','text'] #all document formats we want to rearrange

script = ['py','sh'] # script formats we want to rearrange

print('Hi! welcome to automatic file orignaizer please use with caution')        # welcome messege 
print('the files will be organize in directorys based on their file types: audio,image,document,script,video')
print('all other file types will be moved to others directory')
print('this script does not affecting the current directories!')
while True:         # while for running input
    dir_path = input('please enter path of directory you want to organize : ')  #input path we want to organize  
    if os.path.isdir(dir_path):                  # checking if the path entered is exists
        if dir_path.endswith('/'):                # checing that the path entered without '/' at the end 
            print('please enter path that does not ends with -- / ') 
        else:
            break           # if the path is valid break the while 
    else:
        print('this is a wrong input or this dir is not exists')   # if the path does not exists try again
        print('please try again')

files = os.listdir(dir_path)        # saving a list of all files in the current directory
for file in files:             # for going over all items in the current directory
    file_ = file.split('.')     # splits and saves the filename in a list   
    old_file_path = (str(dir_path) + '/' + str(file))  # saving the current path
    if os.path.isfile(old_file_path):    # check if we are pointing on a file and not directory
        if file_[len(file_) -1 ] in image:     #  check if the file is image
            file_destination = (str(dir_path) + '/image/' + str(file))  # change the destenation to image dir
            if os.path.isdir(str(dir_path) + '/image') == False:  #check if the dir exits
                os.mkdir(str(dir_path) + '/image')                # if dir not exists create it 
                os.rename(old_file_path,file_destination)          # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)           # if the dir exists just move the file to the dir
        
        elif file_[len(file_) -1 ] in audio:       #  check if the file is audio
            file_destination = (str(dir_path) + '/audio/' + str(file))  # change the destenation to audio dir
            if os.path.isdir(str(dir_path) + '/audio') == False:   #check if the dir exists
                os.mkdir(str(dir_path) + '/audio')                 # if dir not exists create it 
                os.rename(old_file_path,file_destination)             # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)              # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in video:          #  check if the file is video
            file_destination = (str(dir_path) + '/video/' + str(file))  # change the destenation to video dir
            if os.path.isdir(str(dir_path) + '/video') == False:     #check if the dir exists
                os.mkdir(str(dir_path) + '/video')                   # if dir not exists create it 
                os.rename(old_file_path,file_destination)               # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)               # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in document:         #  check if the file is document
            file_destination = (str(dir_path) + '/document/' + str(file))  # change the destenation to document dir
            if os.path.isdir(str(dir_path) + '/document') == False:       #check if the dir exists
                os.mkdir(str(dir_path) + '/document')                     # if dir not exists create it 
                os.rename(old_file_path,file_destination)                   # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)                   # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in script:            #  check if the file is script
            file_destination = (str(dir_path) + '/script/' + str(file))  # change the destenation to script dir
            if os.path.isdir(str(dir_path) + '/script') == False:         #check if the dir exists
                os.mkdir(str(dir_path) + '/script')                      # if dir not exists create it 
                os.rename(old_file_path,file_destination)                   # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)                 # if the dir exists just move the file to the dir

        else:                                                           # all other filetypes
            file_destination = (str(dir_path) + '/others/' + str(file))  # change the destenation to others dir
            if os.path.isdir(str(dir_path) + '/others') == False:        #check if the dir exists
                os.mkdir(str(dir_path) + '/others')                    # if dir not exists create it 
                os.rename(old_file_path,file_destination)                # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)               # if the dir exists just move the file to the dir
        
    