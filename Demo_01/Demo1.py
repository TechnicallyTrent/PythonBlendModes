
from PIL import Image               # py -m pip install pillow
from blend_modes import multiply    # py -m pip install blend-modes
import numpy                        # Installed via blend-modes

if __name__ == "__main__":
        
        # Open Images 
        im_bg = Image.open("Demo_01\BG.png")
        im_fg = Image.open("Demo_01\FG.png")

        # Convert to RGBA
        im_bg = im_bg.convert("RGBA")
        im_fg = im_fg.convert("RGBA")

        # Convert to Numpy arrays of floats
        im_bg_arr = numpy.array(im_bg).astype(float)
        im_fg_arr = numpy.array(im_fg).astype(float)

        # Blend Images with Multiply blend mode
        opacity = 1.0 # Opacity of the foreground layer
        img_blended = multiply(im_bg_arr, im_fg_arr, opacity)

        # Convert back to uint8 and an Image
        img_blended = numpy.uint8(img_blended)
        img_blended = Image.fromarray(img_blended)
        img_blended.show()