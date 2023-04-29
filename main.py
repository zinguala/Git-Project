import os       #we use os functions for working with the files (make dir , rename and etc)


image = ['tif','tiff','bmp','jpg','jpeg','gif','png','eps','raw','cr2','nef','orf',
'sr2','apng','avif','jfif','pjpeg','pjp','svg','webp']  #all image formats we want to rearrange

audio = ['3gp','aa','aac','aax','act','aiff','amr','ape','awb','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p',
'mmf','mp3','mpc','msv','nmf','ogg','oga','mogg','opus','rm','ra','rf64','sln','tta','voc','vox','wav','wma','wv','webm','8svx','cda'] #all audio formats we want to rearrange

video = ['webm','mkv','flv','flv','vob','ogv','ogg','drc','gif','gifv','mng','avi','MTS','M2TS','mov','qt','wmv','yuv','rmvb','viv','asf',
'amv','mp4','m4p','m4v','mpg','mp2','mpeg','mpe','mpv','mpg','mpeg','m2v','m4v','svi','3gp','3g2','mxf','roq','Fflv'] #all video formats we want to rearrange

document = ['doc','fb2','md','docx','odt','sxw','pages','pdf','ps','rtf','wp7','wp','wpd','txt','text'] #all document formats we want to rearrange

script = ['py','sh',] # script formats we want to rearrange

current_wd = os.getcwd()      # saving our current working directory
files = os.listdir(".")        # saving a list of all files in the current directory
for file in files:             # for going over all items in the current directory
    file_ = file.split('.')     # splits and saves the filename in a list   
    old_file_path = (str(current_wd) + '/' + str(file))  # saving the current path
    if os.path.isfile(old_file_path):    # check if we are pointing on a file and not directory
        if file_[len(file_) -1 ] in image:     #  check if the file is image
            file_destination = (str(current_wd) + '/image/' + str(file))  # change the destenation to image dir
            if os.path.isdir(str(current_wd) + '/image') == False:  #check if the dir exits
                os.mkdir(str(current_wd) + '/image')                # if dir not exists create it 
                os.rename(old_file_path,file_destination)          # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)           # if the dir exists just move the file to the dir
        
        elif file_[len(file_) -1 ] in audio:       #  check if the file is audio
            file_destination = (str(current_wd) + '/audio/' + str(file))  # change the destenation to audio dir
            if os.path.isdir(str(current_wd) + '/audio') == False:   #check if the dir exists
                os.mkdir(str(current_wd) + '/audio')                 # if dir not exists create it 
                os.rename(old_file_path,file_destination)             # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)              # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in video:          #  check if the file is video
            file_destination = (str(current_wd) + '/video/' + str(file))  # change the destenation to video dir
            if os.path.isdir(str(current_wd) + '/video') == False:     #check if the dir exists
                os.mkdir(str(current_wd) + '/video')                   # if dir not exists create it 
                os.rename(old_file_path,file_destination)               # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)               # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in document:         #  check if the file is document
            file_destination = (str(current_wd) + '/document/' + str(file))  # change the destenation to document dir
            if os.path.isdir(str(current_wd) + '/document') == False:       #check if the dir exists
                os.mkdir(str(current_wd) + '/document')                     # if dir not exists create it 
                os.rename(old_file_path,file_destination)                   # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)                   # if the dir exists just move the file to the dir

        elif file_[len(file_) -1 ] in script:            #  check if the file is script
            file_destination = (str(current_wd) + '/script/' + str(file))  # change the destenation to script dir
            if os.path.isdir(str(current_wd) + '/script') == False:         #check if the dir exists
                os.mkdir(str(current_wd) + '/script')                      # if dir not exists create it 
                os.rename(old_file_path,file_destination)                   # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)                 # if the dir exists just move the file to the dir

        else:                                                           # all other filetypes
            file_destination = (str(current_wd) + '/others/' + str(file))  # change the destenation to others dir
            if os.path.isdir(str(current_wd) + '/others') == False:        #check if the dir exists
                os.mkdir(str(current_wd) + '/others')                    # if dir not exists create it 
                os.rename(old_file_path,file_destination)                # move the file to the dir
            else: 
                os.rename(old_file_path,file_destination)               # if the dir exists just move the file to the dir
        
    