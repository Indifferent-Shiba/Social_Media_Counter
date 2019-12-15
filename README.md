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
The diagram above illustrates the wiring needed to run two RGB LED panels with the Pi. If you plan to use more panels, more Ground and Voltage wiring may be needed. I would head to [Henner Zeller’s Wiring Layout](https://github.com/hzeller/rpi-rgb-led-matrix/blob/master/wiring.md) for more details on all of the pinouts. The Wires go from the pi to the ribbon cable, the other side of the ribbon cable attached to the first panel. The second ribbon cable chains the two RGB LED panels together, the back of the panels noted with arrows in terms of what direction the panels should flow in.  
