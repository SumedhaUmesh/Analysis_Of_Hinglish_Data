import wget
import os
import re


def saveImage(media_links):
    for i in range(50):
        if os.path.isfile('downloaded_image_' + str(i) + '.jpg'):
            os.remove('downloaded_image_' + str(i) + '.jpg')
        else:
            break

    for i, link in enumerate(media_links):
        filename = wget.download(link)
        if os.path.isfile('downloaded_image_' + str(i) + '.jpg'):
            os.remove('downloaded_image_' + str(i) + '.jpg')
        os.rename(filename, 'downloaded_image_' + str(i) + '.jpg')
