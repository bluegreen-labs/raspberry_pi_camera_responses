# Raspberry Pi Camera spectral response curves

I used sensor spec images to digitize the quantum efficiency of both sensors between 400 and 700 nm. A physical measurement will still be needed to quantify the remaining near infrared spectrum (> 700 nm).

Missing or uncertain edge values, at the beginning and end of each curve, were carried forward or backward when missing (2 values at most). Note that these values are scaled between 0-100%, and true quantum efficiency (QE) will be lower for each sensor.

### Raspberry pi camera v1 - Omnivisoin OV5647

![](https://raw.githubusercontent.com/khufkens/pi-camera-response-curves/master/Omnivision_OV5647.jpg)

### Raspberry pi camera v2 - Sony IMX219

![](https://raw.githubusercontent.com/khufkens/pi-camera-response-curves/master/Sony_IMX219.png)
