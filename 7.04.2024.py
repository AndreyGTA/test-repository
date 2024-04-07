from PIL import Image
 
image = Image.open('Chat.jpg')
image2 = Image.open('gim.jpg')
image3 = Image.open('logo.jpg')
#new_image = image.crop((10, 50, 100, 200))
#можно так
#cord = (10, 50, 100, 200)
#new_image = image.crop(cord)
new_image = image.resize((300 , image.height),Image.LANCZOS)
new_image2 = image2.resize((300 , image2.height),Image.LANCZOS)
new_image3 = image3.resize((300 , image3.height),Image.LANCZOS)
new_image.save("Chat1.jpg")
new_image2.save("gim1.jpg")
new_image3.save("logo1.jpg")
# print("Ширина:", image.width)
# print("Высота:", image.height)
# print("Название:", image.filename)
# print("Ширина:", image2.width)
# print("Высота:", image2.height)
# print("Название:", image2.filename)
# print("Ширина:", image3.width)
# print("Высота:", image3.height)
# print("Название:", image3.filename)
image.close()
new_image.close()
image2.close()
new_image2.close()
image3.close()
new_image3.close()








