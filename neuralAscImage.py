import PIL.Image
import requests

'''
	22222222222222222222222222222222222222222222222222
	22222222222222222222222222222532222222222222222222
	22222222222222222200000000000000032222222222222222
	22222222222222200000000000000000000222222222222222
	22222222220000000000000000000000000002222222222222
	22222222220000000000000000000000000000222222222222
	22222222200000000000000000000000000000222222222222
	22222222300000000000000000000000000000222222222222
	22222222000000070000000000000000000000022222222222
	22222222222222270002222000222200000000008222222222
	22222222222222200022222000222220000220000022222222
	22222222222222000222222200222222000222200022222222
	22222222222000002222220000222000000220000222222222
	22222222222222222222222262222240522222222222222222
	22222222222222222222222222222222222222222222222222

'''
def resize(image, new_width = 100):
        width, height = image.size
        new_height = new_width * height / width * 0.5
        # print(new_width, new_height)
        return image.resize((new_width, int(new_height)))

def to_greyscale(image):
    return image.convert("L")

def pixel_to_ascii(image):
    ASCII_CHARS = ["0", "9", "8", "7", "6", "5", "4", "3", "2"]
    pixels = image.getdata()    
    ascii_str = ""
    for pixel in pixels:
        # print(pixel)
        ascii_str += ASCII_CHARS[pixel//30]
    return ascii_str

def main():
    path = 's.png' # input("Enter the path to the image fiel : \n")
    try:
        image = PIL.Image.open(path)
    except:
        print(path, "Unable to find image ")    #resize image
    image = resize(image, 50);    #convert image to greyscale image
    greyscale_image = to_greyscale(image)    # convert greyscale image to ascii characters
    ascii_str = pixel_to_ascii(greyscale_image)
    img_width = greyscale_image.width
    ascii_str_len = len(ascii_str)
    ascii_img=""    #Split the string based on width  of the image
    for i in range(0, ascii_str_len, img_width):
        ascii_img += "\t" + ascii_str[i:i+img_width] + "\n"    #save the string to a file
    with open("ascii_image.txt", "w", encoding="utf-8") as f:
        f.write(ascii_img)

def ascImage(urlToCheck):
    imageNetAddress = str(urlToCheck)
    try:
        response = requests.get(imageNetAddress.strip())
        file = open("s.png", "wb")
        file.write(response.content)
        file.close()        
    except:
        return [None]   
    
    main()
    f = open('ascii_image.txt', 'r')
    openImage = f.readlines()
    f.close()
    return openImage
    # for x in openImage:
    #     print(x.strip())
    
