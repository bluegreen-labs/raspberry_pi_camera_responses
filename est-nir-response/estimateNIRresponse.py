import numpy as np
import matplotlib.pyplot as plt

# Data from a probably-similar-enough CMOS sensor that goes into the NIR to ~1050nm where CMOS all peter out
# Extracted from the file CMOS1280b1.png
simRlam, simRval = np.genfromtxt("R_similar.csv", delimiter=", ", unpack=True)
simGlam, simGval = np.genfromtxt("G_similar.csv", delimiter=", ", unpack=True)
simBlam, simBval = np.genfromtxt("B_similar.csv", delimiter=", ", unpack=True)

# Data from RasPiCam-v2(like) sensor (Sony IMX111), extracted from digitized plot data by khufkens
lam, Rval, Gval, Bval = np.genfromtxt("../Sony_IMX219_spectral_response.csv", delimiter=",", unpack=True, skip_header=1)

# Sensor QE data from another in the Sony Exmor R sensor line, to use as a
# guideline for the overall CMOS sensitivity envelope from 300-1100nm
#exmorQElam, exmorQE = np.genfromtxt("SonyIMX178qe_extracted.csv", delimiter=", ", unpack=True)
#
#plt.plot(exmorQElam, exmorQE*100, "--k")
# doesn't look like it describes the envelope of the IMX219 very well...forget it.

scale = np.max(Gval) / np.max(simGval)
squish = 1.0 #0.98
plt.plot(simRlam*squish, simRval*scale, ':k')
plt.plot(simGlam*squish, simGval*scale, ':k')
plt.plot(simBlam*squish, simBval*scale, ':k')
plt.plot(lam, Rval, '-r')
plt.plot(lam, Gval, '-g')
plt.plot(lam, Bval, '-b')

plt.xlabel("Wavelength [nm]")
plt.ylabel("Relative Response [%]")
plt.title("Sony-IMX219 (Vis) and Random CMOS sensor (to NIR)")
plt.show()
# Save file interactively, as "SonyIMX219_v_randomCMOS.png"

##########################################################################################
# Add Bezier curves of new estimates by eye in Inkscape 
#   (original curves in file RGB_NIRsketches.svg)
#*************************************************************************************************************
#****IF YOU THINK THE CURVES SHOULD BE TWEAKED, GO IN THERE, AND MODIFY THEM, THEN FOLLOW THE NEXT STEPS!!****
#*************************************************************************************************************
# Turn on mask layer and R, G, or B layer, then export to 3 PNGs named [x]filter_NIRsketch.png
# Import estimated curves to WebPlotDigitizer, extract data
# Generate new CSV files, and plot these here

# Data from a probably-similar-enough CMOS sensor that goes into the NIR
estRlam, estRval = np.genfromtxt("Rfilter_NIRsketch.csv", delimiter=", ", unpack=True)
estGlam, estGval = np.genfromtxt("Gfilter_NIRsketch.csv", delimiter=", ", unpack=True)
estBlam, estBval = np.genfromtxt("Bfilter_NIRsketch.csv", delimiter=", ", unpack=True)

plt.plot(simRlam*squish, simRval*scale, ':r')
plt.plot(simGlam*squish, simGval*scale, ':g')
plt.plot(simBlam*squish, simBval*scale, ':b')
plt.plot(lam, Rval, '-r', linewidth=2.0)
plt.plot(lam, Gval, '-g', linewidth=2.0)
plt.plot(lam, Bval, '-b', linewidth=2.0)
plt.plot(estRlam, estRval, "--r", linewidth=2.0)
plt.plot(estGlam, estGval, "--g", linewidth=2.0)
plt.plot(estBlam, estBval, "--b", linewidth=2.0)
plt.xlabel("Wavelength [nm]")
plt.ylabel("Relative Response [%]")
plt.title("Sony-IMX219 (Vis w/ NIR est'd) and Random CMOS sensor (Vis-NIR)")
plt.show()
# Save interactively as "SonyIMX219withNIRestimate_v_randomCMOS.png"

#########################################################################################

# Finally, do a simple linear interpolation at the regularly-spaced 1nm step values,
# and roll into a single file like khufkens did originally
reglam = np.arange(701,1051)

Rinterp = np.interp(reglam, estRlam, estRval)
Ginterp = np.interp(reglam, estGlam, estGval)
Binterp = np.interp(reglam, estBlam, estBval)

with open("Sony_IMX219_NIRESTIMATE_spectral_response.csv", 'w') as fout:
    fout.write("wavelength,red_est,green_est,blue_est\n")
    for i, rl in enumerate(reglam):
        fout.write("%d,%.3f,%.3f,%.3f\n" % (rl, Rinterp[i], Ginterp[i], Binterp[i]))

# Fin.



