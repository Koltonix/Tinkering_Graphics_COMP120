# Comp120 Tinkering Graphics Assignment
## Python Code for Re-purposing Graphics Algorithms

[This Repository](https://github.com/Koltonix/comp120-tinkering-graphics)

| Name                                                | Contract |
|-----------------------------------------------------|----------|
|[James Heath](https://github.com/Heathage)           | #1       |
|[Callum Metcalfe](https://github.com/Tragicdragoon)  | #2       |
|[Christopher Robertson](https://github.com/Koltonix) | #3       |
|[Alex Williamson](https://github.com/Alphon1)        | #4       |
|[Thomas O'Leary](https://github.com/thomasoleary)    | #5       |

## Contracts Information
**Python Version 3 is necessary for all projects** 

**You will also need the Pygame module too**

### Contract #1 - Platformer Tile Generator
*A tool that will generate textures for various different types of tile that couldbe conceivable to have in a platformer.  There needs to be an allowanceto specify variations through a set of attiributes (e.g., soil-dry, wet,charred;foliage-spring,autumn,summer,winter; etc.)*

### Contract #2 - Platformer Level Generator
*A tool that will take a level size and other attributues and generate a tile mapto represent a 2d side-scrolling platformer.  A tile set will be fed into this tooland it is imagined that any or all of these tiles could be used to generate themap. There should be clearly identifiable features of the level such as pitfalls,shrines, wells, water, pools, and so on; befitting of a historical-fantasy setting.*

#### Requirements

* Generate a tilemap
* include a water tile
* Include death tiles
* Have the map be randomly generated

### Contract #3 - Platformer Entity Generator
*Various creatures will occupy the world, and so the ability to create manydifferent types of items and enemies using various components is desired.These units should be saved to a new png file for use in the game.*

#### Requirements

* Must be able to create a variety of objects
* Using a component system if possible
* Save to a new .PNG specifically

#### Instructions
**Before Running:**

* To run this script you need to ensure that in the root folder there is another folder named '\Images' to ensure that the program is able to save the image create. 

* The program also automatically crops the photo using the colour of the background.

* From there you are able to run the script normally and can use the software as intended.

* Create objects using the buttons and move around with WASD. 

* You can colour them by clicking on the RGB values on the right hand side. To enter a value you must 3 digits exactly, so the value of 3 would have to be 003

* You are also able to delete the most recent shape that was created too. 

* After you can then save the image which can be found in the '\Images' folder in the root of the program.

### Contract #4 - Platformer Entity Reskinning
*To enable better re-use of assets,  a tool which reskins in-game items andmonsters devised by the dugeon entity.  You will have to remove a colourand then add a new colours.  There are four types (representing qualities)represented by a set of colours.  For example:  red, green, blue and yellow.Each unit of these teams will have to be saved in a new png file.*

### Contract #5  - Colour Blindness User InterfaceTool
*1-in-12 men and 1-in-200 women in the world suffer some form of colour blind-ness. Your studio lead has asked you to create a tool which takes in a screen-shot of your game and then displays the image as if viewed by someone with a form of colour blindness. They would like you to save an image to file for everytype of colour blindess so that the UI designer can adjust the colours of the ingame UI.*

#### Requirements

* Grab an image to be processed and reformatted
* Display the processed image to the screen
* Must be able to save multiple processed images

#### Instructions
**Before Running:**

* To run the script, ensure that within the root folder a folder named '\Colour Blind Images' is there. This will be the folder where all newly processed images will be saved to.

# MIT Licensing

We have decided to go with the MIT License since we are more than pleased for people to use our code in a commercial sense for their own software. We also acknowledge and allow the distribution and modification of our code to be used elsewhere whether it be public, or private. The conditions to this is that this piece of code provides no warranty, nor limitation of liability. The largest condition is that if our code is used then the MIT License provided must be included in said project and state our authorship into it. The reason we quite like this is because it could potentially help the open source community for free while still allowing us to retain our authorship of the code which could be to our benefit in gaining some advertisement in the software development industry.
