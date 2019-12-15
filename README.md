![Liker](https://github.com/Indifferent-Shiba/Social_Media_Counter/blob/master/Images/liker.jpg)
# Social Media Counter Overview
The goal of this project is to create a display using RGB LED panels that shift through social media icons and their associated number of likes, subscribers, followers, and so forth. Inbetween social media counts will be animated transitions to add some variety and to fully untilize the potential of the LED panels artistically, the transitions randomized from the pool of available animations. Since the panels need a container, a case will be modeled and printed via a 3D printer, the case designed to be modular for more or less panels depending on the projects needs while also being both wall mountable and portable. Eventually, the counts for each social media displayed will ideally be automatically updated, the number of likes, subscribers, followers, and so forth pulled automatically every so often using API Keys.
### Current Progress:
- [x] Social media icons & manual counts run.
- [x] Randomized transitions between social media counts run.
- [x] Case for social media counter printed and stable. 
- [ ] Automated aquisition of social media counts via API Keys run.
# Getting Started
I used:
* 1 Raspberry Pi 2 Model B
* 2 64x32 RGB LED Matrix - 4mm Pitch
* 1 SanDisk Ultra 16GB Micro SD Card
* 1 Tobsun 50W DC-DC Converter 
* 2 Ribbon Cables & a pack of Male to Female Jumper Wires
* 6 mm Magnets and 4 mm Screws
## Wiring the Parts
![Wiring](https://github.com/Indifferent-Shiba/Social_Media_Counter/blob/master/Images/raspi_header_fritzer.png)
The diagram above illustrates the wiring needed to run two RGB LED panels with the Pi. If you plan to use more panels, more Ground and Voltage wiring may be needed. I would head to [Henner Zeller’s Wiring Layout](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md) for more details on all of the pinouts. The Wires go from the pi to the ribbon cable, the other side of the ribbon cable attached to the first panel. The second ribbon cable chains the two RGB LED panels together, the back of the panels noted with arrows in terms of what direction the panels should flow in.  
## Setting Up the Pi
To start, I installed the command line only version of Debian onto my Micro SD Card. Once the car is in the Pi and the basics are set up, install [Henner Zeller’s original project](https://github.com/hzeller/rpi-rgb-led-matrix).
```
$ mkdir display64x32
$ cd display64x32
$ git clone https://github.com/hzeller/rpi-rgb-led-matrix/
```
Next, we need to move the logs, scripts, icons, fonts, and animations to their proper locations:
### Social Media Logs:
These logs are currently used as the sources for our social media counts (In this case, Facebook, Instagram, Twitter, and Youtube.) Later, they will be replaced with a script to pull social media counts directly from the desired social media sites. 
* fb.txt			
* inst.txt			
* twi.txt			
* yt.txt 

##### &rarr; /home/user/
### Shuffle Log:
This log is used to keep track of shuffled transitions, the transitions printed into this file and kept tracked up via line count, the line count of the log determining when the next shuffle should occur.This file may have to be cleared and/or primed when changes occur.  
* Shuffle_log.txt
#### &rarr; /home/user/display32x64/rpi-rgb-led-matrix
### Social Media Icons:
These are the logos for a few social media sites. These icons are displayed next to their correlated counts. The icons were taken from the internet and pulled into [Gimp](https://www.gimp.org/) (discussed later under “Making Animations”), resized, and exported into ppm files. Their curved look was manually created in gimp by erasing/ adding pixels. 
* FB.ppm
* Instagram.ppm
* Twitter.ppm
* Twitter_blue.ppm
* yt.ppm
#### &rarr; /home/user/display32x64/rpi-rgb-led-matrix/graphics/ (may have to make graphics folder in rpi-rgb-led-matrix folder)
### Animations:
Animations are collections of ppm images that are played in a numbered sequence to produce an animation. Each collection of ppm files needs to be in its own folder, the files need to share a similar name and start with the number 1, such as “ectb1.ppm” and continue to increase until over, such as “ectb74.ppm”. 
* ectb (Folder)
#### &rarr; in /home/user/display32x64/rpi-rgb-led-matrix/graphics/Animations (may have to make Animations folder in graphics folder)
###Fonts:
These fonts were fonts that come with HZeller’s project, but were too small for my particular panels. I took one of the fonts from the project and pulled it into [FontForge](https://fontforge.org/en-US/) and resized them to better suit the panels and my use of them. 
* FixedMedium-15.bdf 
* FixedMedium-30.bdf
#### &rarr; /home/user/display32x64/rpi-rgb-led-matrix/fonts/
### Scripts:
These scripts are the meat of this project, using Python 2 and Bash scripts to run the Social Media Counter. They pull the count numbers, run the animations, and organize the display of social media site information and transitions. The scripts themselves have comments to help you personalize your social media counter. 
* arproject.sh
* fb_counter.sh 
* insta_counter.sh
* twi_counter.sh
* yt_counter.sh
#### &rarr; /home/user/display32x64/rpi-rgb-led-matrix/
* zz-animation.py
* zz-doubletext.py
* zz-image-n-text.py
#### &rarr; /home/user/display32x64/rpi-rgb-led-matrix/bindings/python/samples 
## Making Animations 
![Gimp](https://github.com/Indifferent-Shiba/Social_Media_Counter/blob/master/Images/gimp_homepage.PNG)
I have made many animations, but due to copyright rules, I am only able to post this original animation. However, all sorts of animations are possible, from Mario walking across the screen to the enterprise soaring by. I have found two ways to make animations, both that utilize [Gimp](https://www.gimp.org/). The first method takes a GIF and breaks the GIF into frames, which are then exported individually as ppm files. The other method takes an image and resizes it to fit the panels, the image exported as a ppm and animated by sliding it across the panels. 
### Making Animations based on GIFS
#### Step 1: Find a GIF you like
While searching for GIFs, keep in mind that the more complex a GIF is, the more likely that the animation will lose much of the GIFs details when resized to fit the panels and will have many more frames to export individually. I suggest keeping your GIF choices simple since it will require less work and less frame by frame editing in terms of fixing mixed up pixels. GIFs I worked with include Tron, Legend of Zelda, Super Mario Brothers, Raspberry Pi imagery, Mega Man, Disney logos, Shovel Knight, Cowboy Bebop, and some others, simplicity not necessarily taking away the variety of things you can do!
#### Step 2: Pull the GIF into Gimp
Opening Gimp and using **File &rarr; Open**, bring up the GIF. Upon bringing the GIF into Gimp, you will see on the right-hand side that your GIF has been broken up into layers for you. 
#### Step 3: Crop, Resize, and Touch Up
Crop your gif to the desired content using the rectangle selection tool in the left-hand corner of your screen, the first option in your list of icon tools. Next, go to **Image &rarr; Scale Image** and scale the image in pixels to your panel, in this case, scaling it to 32 pixels tall by 128 pixels long since in my example project I am using two panels. Quality at this point may vary, so pixels can be manually edited/ smoothed out to look nicer or you can try to crop the original GIF to a different size/focus and scale again to see if that helps.
#### Step 4: Export as ppm Files
This step is tedious. On the right-hand side with all of your frames, hide all of the frames by clicking the eye button until you reach frame 1. Export this frame by going up to **File &rarr; Export as…** and select the option to **show all file types**. Scroll down to **ppm** and save the file as “name1.ppm”. Click the following frame to be shown, the eye button reappearing, and do the same process for it, exporting it as “name2.ppm.” Continue this process until all frames are exported. I suggest exporting these frames into a folder to make it easier to hold all of them together.  
### Making Animations Based on Images
#### Step 1: Find an Image
Just as before with Animations, keep in mind that image quality will change when the image is resized to fit the panels. I have used both Star Trek and Star Wars ships as scrolling image on my Social Media Counter.
#### Step 2: Pull Image into Gimp and Resize
Opening Gimp and using **File &rarr; Open**, bring up the image. Crop your image to the desired content using the rectangle selection tool in the left-hand corner of your screen, the first option in your list of icon tools. Next, go to **Image &rarr; Scale Image** and scale the image in pixels to the height of your panel. Play with the width until the image look appropriate. 
#### Step 3: Export as ppm File
Export the image by going up to **File &rarr; Export** as… and select the option to **show all file types**. Scroll down to **ppm** and save the file as whatever name you desire. 
## Printing and Building the Case



