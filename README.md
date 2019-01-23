# Raspberry Pi Camera spectral response curves

I used sensor spec images to digitize the quantum efficiency of both sensors between 400 and 700 nm. A physical measurement will still be needed to quantify the remaining near infrared spectrum (> 700 nm).

Missing or uncertain edge values, at the beginning and end of each curve, were carried forward or backward when missing (2 values at most). Note that these values are scaled between 0-100%, and true quantum efficiency (QE) will be lower for each sensor.

A true response curve measured using a monochromator has been described in [Pagnutti et al. 2017](https://www.spiedigitallibrary.org/journals/journal-of-electronic-imaging/volume-26/issue-01/013014/Laying-the-foundation-to-use-Raspberry-Pi-3-V2-camera/10.1117/1.JEI.26.1.013014.full?SSO=1).

### Raspberry pi camera v1 - Omnivisoin OV5647

![](https://raw.githubusercontent.com/khufkens/pi-camera-response-curves/master/Omnivision_OV5647.jpg)

### Raspberry pi camera v2 - Sony IMX219

![](https://raw.githubusercontent.com/khufkens/pi-camera-response-curves/master/Sony_IMX219.png)
