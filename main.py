import os 
file_types = []
image = ['tif','tiff','bmp','jpg','jpeg','gif','png','eps','raw','cr2','nef','orf',
'sr2','apng','avif','gif','jfif','pjpeg','pjp','svg','webp']
aduio = ['3gp','aa','aac','aax','act','aiff','amr','ape','awb','dss','dvf','flac','gsm','iklax','ivs','m4a','m4b','m4p',
'mmf','mp3','mpc','msv','nmf','ogg','oga','mogg','opus','rm','ra','rf64','sln','tta','voc','vox','wav','wma','wv','webm','8svx','cda']
files = os.listdir(".")
print (files)
for file in files:
    file = file.split('.')
    file_types.append(file[len(file) -1 ])
