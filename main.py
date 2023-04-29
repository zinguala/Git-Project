import os       #we use os functions for working with the files (make dir , rename and etc)


image = ['tif','tiff','bmp','jpg','jpeg','gif','png','eps','raw','cr2','nef','orf',
'sr2','apng','avif','jfif','pjpeg','pjp','svg','webp']  #all image formats we want to rearrange

audio = ['3gp','aa','aac','aax','act','aiff','amr','ape','awb','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p',
'mmf','mp3','mpc','msv','nmf','ogg','oga','mogg','opus','rm','ra','rf64','sln','tta','voc','vox','wav','wma','wv','webm','8svx','cda'] #all audio formats we want to rearrange

video = ['webm','mkv','flv','flv','vob','ogv','ogg','drc','gif','gifv','mng','avi','MTS','M2TS','mov','qt','wmv','yuv','rmvb','viv','asf',
'amv','mp4','m4p','m4v','mpg','mp2','mpeg','mpe','mpv','mpg','mpeg','m2v','m4v','svi','3gp','3g2','mxf','roq','Fflv'] #all video formats we want to rearrange

document = ['doc','fb2','md','docx','odt','sxw','pages','pdf','ps','rtf','wp7','wp','wpd','txt','text'] #all document formats we want to rearrange

current_wd = os.getcwd()      # saving our current working directory
files = os.listdir(".")
print (files)
for file in files:
    file_ = file.split('.')
    old_file_path = (str(current_wd) + '/' + str(file))
    if os.path.isfile(old_file_path):
        if file_[len(file_) -1 ] in image:
            file_destination = (str(current_wd) + '/image/' + str(file))
            if os.path.isdir(str(current_wd) + '/image') == False:
                os.mkdir(str(current_wd) + '/image')
                os.rename(old_file_path,file_destination)
            else: 
                os.rename(old_file_path,file_destination)
        
        elif file_[len(file_) -1 ] in audio:
            file_destination = (str(current_wd) + '/audio/' + str(file))
            if os.path.isdir(str(current_wd) + '/audio') == False:
                os.mkdir(str(current_wd) + '/audio')
                os.rename(old_file_path,file_destination)
            else: 
                os.rename(old_file_path,file_destination)

        elif file_[len(file_) -1 ] in video:
            file_destination = (str(current_wd) + '/video/' + str(file))
            if os.path.isdir(str(current_wd) + '/video') == False:
                os.mkdir(str(current_wd) + '/video')
                os.rename(old_file_path,file_destination)
            else: 
                os.rename(old_file_path,file_destination)

        elif file_[len(file_) -1 ] in document:
            file_destination = (str(current_wd) + '/document/' + str(file))
            if os.path.isdir(str(current_wd) + '/document') == False:
                os.mkdir(str(current_wd) + '/document')
                os.rename(old_file_path,file_destination)
            else: 
                os.rename(old_file_path,file_destination)

        else:
            file_destination = (str(current_wd) + '/others/' + str(file))
            if os.path.isdir(str(current_wd) + '/others') == False:
                os.mkdir(str(current_wd) + '/others')
                os.rename(old_file_path,file_destination)
            else: 
                os.rename(old_file_path,file_destination)
        
    