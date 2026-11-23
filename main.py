import cv2
import numpy as np

#match input intensity to output intensity
def intensity_level(pix_val, inp1, out1, inp2, out2):
    if(0<=pix_val and pix_val <= inp1):
        return (out1/inp1)*pix_val
    elif(inp1<pix_val and pix_val<=out2):
        return ((out2 - out1)/(inp2 - inp1)) * (pix_val-inp1)+out1
    else:
        return ((255-out2)/(255-inp2)) * (pix_val - inp2)+out2

#turn image grayscale 
gray_image = cv2.imread("froggt.jpg", 0)

#invert the image
neg_image = 255 - gray_image

gamma = 1.2
gamma_corrected = np.array(255*(neg_image/255) ** gamma, dtype = 'uint8')
# cv2.imwrite('gamma transformed(' + str(gamma) + ').jpg', gamma_corrected)

lut = np.array([intensity_level(i, 80, 0, 180, 255) for i in range(256)])
lut = np.clip(lut, 0, 255).astype(np.uint8)

intensity_corrected = lut[gamma_corrected]

#cv2.imshow('Grayscale', gray_image)
#cv2.imshow('Negative', neg_image)
cv2.imwrite('final_sketch.jpg', intensity_corrected)
cv2.imshow('intensity corrected', intensity_corrected)

cv2.waitKey(0)
cv2.destroyAllWindows()
