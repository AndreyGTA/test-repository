# from PIL import Image
#  
# image = Image.open('img.jpg')
# image.show()
# from PIL import Image
#  
# image = Image.open('img.jpg')
# print("Ширина:", image.width)
# print("Высота:", image.height)
# print("Название:", image.filename)
# image.close()
# from PIL import Image
#  
# image = Image.open('img.jpg')
# new_image = image.resize((1000, 1000), Image.LANCZOS)
# new_image.save("resized_img.jpg")
# image.close()
# new_image.close()
# from PIL import Image
#  
# image = Image.open('img.jpg')
# new_image = image.crop((10, 50, 100, 200))
# #можно так
# #cord = (10, 50, 100, 200)
# #new_image = image.crop(cord)
# new_image.save("cropped_img.jpg")
# image.close()
# new_image.close()
# from PIL import Image
#  
# image = Image.open('img.jpg')
# new_image = image.rotate(180)
# new_image.save("rotated_img.jpg")
# image.close()
# new_image.close()
# from PIL import Image
#  
# image = Image.open('img.jpg')
# print(image.format)
# image.save('img.png', 'png')
# image.close()
# new_image.close()
# # # from PIL import Image
# # #  
# # # image = Image.open('img.jpg')
# # # new_image = image.resize((150, 150), Image.LANCZOS)
# # # new_image.save("resized_img.jpg")
# # # image.close()
# # # new_image.close()
# # # image = Image.open('img.png')
# # # new_image = image.resize((150, 150), Image.LANCZOS)
# # # new_image.save("resized_img.png")
# # # image.close()
# # # new_image.close()



# from PIL import Image
#  
# image = Image.open('img.jpg')
# new_image = image.crop((150, 0, 300, 300))
# #можно так
# #cord = (10, 50, 100, 200)
# #new_image = image.crop(cord)
# new_image.save("cropped_img.jpg")
# image.close()
# new_image.close()
# 
# image = Image.open('img.png')
# new_image = image.crop((0, 0, 150, 300))
# #можно так
# #cord = (10, 50, 100, 200)
# #new_image = image.crop(cord)
# new_image.save("cropped_img.png")
# image.close()
# new_image.close() 
x = int(input("1-3 "))
for i in range(1 ,x):
    image = Image.open('x.jpg')
    print("Ширина:", image.width)
    print("Высота:", image.height)
    print("Название:", image.filename)
    image.close()




