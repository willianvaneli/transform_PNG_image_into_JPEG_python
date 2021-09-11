#!/usr/bin/env python
# -*- coding: utf-8 -*-
import progressbar
import os
from PIL.ExifTags import GPSTAGS
from PIL.ExifTags import TAGS
from PIL import Image


print("Starting PGN to JPEG Image Conversion\n")
bar = progressbar.ProgressBar()

pasta = './'
for diretorio, subpastas, arquivos in os.walk(pasta):
    bar.start(len(arquivos))
    i=0
    for arquivo in arquivos:
        if '.png' in arquivo:
            caminho = os.path.join(os.path.realpath(arquivo))            
            image = Image.open(caminho)

            if not image.mode == 'RGB':
                image = image.convert('RGB')

            image.save(arquivo[:-3] + 'jpg', quality=95)
            i+=1
            bar.update(i)