# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 14:10:06 2020

@author: renatons
"""

from PIL import Image 
import pytesseract 
from pdf2image import convert_from_path 
import os 
  
pdf_entrada = r'C:\Users\RenatoNS\Desktop\teste_ocr\imgs\teste_pdf.pdf'

dir_saida = r'C:\Users\RenatoNS\Desktop\teste_ocr'

dir_atual = os.getcwd()
os.chdir(dir_saida)
  
  
paginas = convert_from_path(pdf_entrada, 500) 
  
image_counter = 1
  
for pagina in paginas: 
    filename = "pagina_"+str(image_counter)+".jpg"
    pagina.save(filename, 'JPEG') 
    image_counter = image_counter + 1
  

limite = image_counter-1
  
arq_saida = "saida_texto.txt"
  
f = open(arq_saida, "a") 
  
for i in range(1, limite + 1): 
    filename = "pagina_"+str(i)+".jpg"

    texto = str(((pytesseract.image_to_string(Image.open(filename))))) 

    texto = texto.replace('-\n', '')     
  
    f.write(texto) 
  
f.close() 
os.chdir(dir_atual)
