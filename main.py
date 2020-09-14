#Script pro vytváření poznáváček
#By: Tomáš Kebrle

#! Knihovna pro stahování
import urllib.request
from tkinter import *


#Proces pro stahování obrázku
def dl_jpg(url, file_path, file_name):
    full_path = file_path + file_name + '.jpg'
    urllib.request.urlretrieve(url, full_path)

#Vytvoření HTML souboru
def html_create(file_name, url, nazev, btn1, btn2):
    f = open(file_name + '.html', 'w')
    f.write('<!DOCTYPE html>'
            '<html lang="en">'
            '<head>'
            '<meta charset="UTF-8">'
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/materialize/1.0.0/css/materialize.min.css">'
            '<style>'
            'img{height:50% !important;width:50% !important;overflow: hidden;}'
            '</style>'
            '<title>' + nazev + '</title>'
            '</head>'
            '<body>'
            '<div class="container">'
            '<div class="row">'
            '<div class="img">'
            '<img class="col s12 l8 center" src="images/' + file_name + '.jpg">'
            '</div>'
            '<div class="center col s12 l4">'
            '<h1 class="center">' + nazev + '</h1> <br> <br> <br>'
            + '<p class="grey-text lighten-2 col s12 l12 center">' + url + '</p>'
            '<a href="' + btn1 + '.html" class="btn blue waves-effect waves-light">Previous</a>'
            '<a href="' + btn2 + '.html" class="btn blue waves-effect waves-light">Next</a>' 
            '</div>'
            '</div>'
            '</div>'
            '</body>'
            '</html>'
            )

file_name = 0
def click():
        global  file_name
        click_url =  url.get()
        click_nazev = nazev.get()
        file_name = int(file_name)
        file_name += 1
        tlacitko1 = file_name - 1
        tlacitko2 = file_name + 1
        file_name = str(file_name)
        tlacitko1 = str(tlacitko1)
        tlacitko2 = str(tlacitko2)
        #Download proces
        dl_jpg(click_url, 'images/', file_name)
        #vytvořit HTML file
        html_create(file_name, click_url, click_nazev, tlacitko1, tlacitko2)

####GUI
window = Tk()
window.title('Poznávačka Maker 3000')

# Label
Label(window, text='POZNÁVAČKA MAKER 3000', font='none 32 bold').grid(row=0, column=0, sticky=W, padx=20)

# Text Entry
Label(window, text='URL obrázku(musí končit na .jpg)', font='none 11').grid(row=3, column=0, sticky=W, padx=20)
url = Entry(window, width=80, )
url.grid(row=5, column=0, sticky=W, padx=20)

Label(window, text='Název kytky rostliny atd.', font='none 11').grid(row=7, column=0, sticky=W, padx=20)
nazev = Entry(window, width=80, )
nazev.grid(row=9, column=0, sticky=W, padx=20)

# Submit
Button(window, text='POTVRDIT', width='6', command=click).grid(row=11, column=0, sticky=W, padx=20)









#Loop pro stahování a pojmenování obrázku
#while 2 < 3:
#   url = input('Zadejte URL obrázku:')
#   nazev = input('Název:')
#   file_name = int(file_name)
#   file_name += 1
#   tlacitko1 = file_name - 1
#    tlacitko2 = file_name + 1
#    file_name = str(file_name)
#    tlacitko1 = str(tlacitko1)
#    tlacitko2 = str(tlacitko2)
#    #Download proces
#    dl_jpg(url, 'images/', file_name)
#    #vytvořit HTML file
#    html_create(file_name, url, nazev, tlacitko1, tlacitko2)

window.mainloop()