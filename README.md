# Melody Nest

---

## Table of Contents

---

1. [UX](#ux)
   - [User Stories](#user-stories)
   - [Viability](#project-viability)
   - [Responsive](#responsive)
   - [Frameworks](#frameworks-used)
   - [Typography](#typography)
   - [Colors](#colors)
   - [icons](#icons)
   - [Wireframes](#wireframes)
   - [Logo](#logo)
2. [Features](#features)
   - [Existing Features](#existing-features)
   - [Features left to implement](#features-left-to-implement)
3. [Technologies Used](#technologies-used)
   - [Front End Technologies](#front-end-technology)
4. [Testing](#testing)
   - [Validators](#validators)
   - [Testing Methods](#testing-methods)
5. [Deployment](#deploy)
   - [Local Deployment](#local-deployment)
   - [Remote Deployment](#remote-deployment)
6. [Credits](#credits)
   - [Content](#content)
   - [Media](#media)
   - [Acknowledgements](#acknowledgements)

---

## UX

---

### User Stories

This gis created so users can share music they have arranged or composed, sharing the audio and the sheet music.

- As a user, I want to be able to share the sheet music I arrange or I compose

- As a user, I want to be able to share an audio file of the music I performed on my chosen instrument

- As a user, I want to have a profile page where I can share information about myself in terms of music. 

- As a user, I want to write reviews about the music shared by other users

- As a user, I want to see what others think of the music I have shared

- As a user, I want to see an attractive website that makes me want to use it. 

- As a user, I want to see other users profile pages, and see what they have shared

- As a user, I want to listen to other users performances

- As a user, I want to be able to download some new music that others have shared.

### Project Viability

|     | Feature                        | Importance | Viability |
| --- | ------------------------------ | :--------: | --------: |
| A   | Music player                   |     5      |         5 |
| B   | Sheet music PDF sharing        |     5      |         5 |
| C   | Image upload                   |     5      |         5 |
| D   | Reviewing                      |     3      |         4 |
| E   | Profile page and updatable info|     4      |         4 |
|     | Total                          |     22     |        23 |

### Responsive

[Am I Responsive?](http://ami.responsivedesign.is/#) was used to test how responsive the website is on different devices.

<img src="static/images/responsive.png">

### Frameworks Used

- [Bootstrap](https://getbootstrap.com/)
- Bootstrap is an open source library with access to reusable bits of code for html, css and javascript. 

- [jQuery](https://jquery.com/)
- jQuery is an open source library that makes using javascript easier and quicker. It simplifies a variety of multiple lines of javascript code by putting it into a single line of jquery code. 

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- Flask is a micro web framework written in Python
- Uses Workzeug which is a utility library for the Python programming language
- Uses Jinja which is a template engine for the Python programming language

- [NodeJs](https://en.wikipedia.org/wiki/Node.js)
- npm was installed so bootstrap was modifiable. 

- [Sass](https://en.wikipedia.org/wiki/Sass_(stylesheet_language))
- Sass is used to tweak the stylesheets so bootstrap is editable. It allows the custom code to be added to the bootstrap. Installed [Ruby](https://en.wikipedia.org/wiki/Ruby_(programming_language)) in order to use Sass

### Typography

The font Arvo was used as it is a serif font. Serif fonts are known for their roman types. 
[As music is associated with latin](https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/type-classifications) (as shown with terminology for dynamics), a serif font was appropriate for this project.

1 [Google Font](https://fonts.google.com/) was used throughout this website:
- ["Arvo", serif;](https://fonts.google.com/specimen/Arvo)

### Colors

The following colours have been selected for this project

#### Foundation colours
These were used as the main colours. A more monochromic approach 

- "white": "white"
- "black": "black"
- "gray": #707070,
- "gray-dark": #3f3f3f,

#### Accent colours 
The red was chosen from a colour picker on the rose itself on the home page image.
The other colours were chosen to compliment the selected red colour. According to this [website](https://www.canva.com/colors/color-wheel/), they are either tetradic or analogous.

 Main accent colour
- "red": #421319,

Analogous - Chosen for its versatility. 

- "purple": #421331,
- "brown": #422513,

Tetradic - Chosen for boldness but to compliment the red as the primary colour. Red is used for anything larger, with the smaller buttons having the tetradic colours.
- "green": #194213,
- "mint green": #13423c,
- "dark blue": #131942,


### Icons

[Font Awesome 5.13.1](https://fontawesome.com/)
  

### Wireframes

- Click here to see the project [Wireframes](wireframes.md)

### Image modifications

- [GIMP](https://www.gimp.org/) was used to tweak the main page image so the top was plain black so title could be added without conflicting with the words on the piano. 
Permissions for editing image ok.   

##### Back to [top](#table-of-contents)
---

## Features

---

### Existing Features

- View shared music

  - Able to see cards of different pieces of music. 
  - Shares Name of piece, artists name, genre of the music, instrument performed with, username, button to the sheet music pdf on a new tab, play and stop button with performance playing

- Write a review 

  - Able to write a review on the piece of music shared. The button pops up on any pieces of music not created by the current user. This opens up a page for user to type what they think of the music. 

- Share pieces of music

   - Page called share which allows a user to type in a title and  artist of the piece of music. 
   - Choose a genre and instrument from the dropdown. If genre or instrument isnt there, a new one can be added
   - Upload an audio file which will be playable on the piece of music card
   - Upload an image/piece of artwork which will show up as the main image for that piece of musics card
   - Upload sheet music which can be accessed by users clicking on the sheet music on the card. This links the uploaded music to a new page.  

- Edit and delete pieces

  - If the piece of music belongs to the user, they can either delete it by clicking on the delete button.
  - The users can edit the pieces by clicking on the edit button and going to a page which fills in previously filled info into the shared form page

- Sound  

  - Music plays through the play bottom at the bottom of the cards. If play is clicked, it stops all music on the page and just starts that one. Stop Stops all music on the page. 
  
- Profile Pages 

  - Page full of profiles where every profile can be accessible. Shows the user names and profile images of every user
  - Profile page shows the users chosen profile image. Information about themselves from inputted data on register, and an about me page that can be edited any time. 
  - Edit profile button which opens up a similar looking page if the profile belongs to the current user
  - All pieces of music shared by that user is viewable at the bottom of this page

- Edit profile Page

  -  Change profile picture 
  -  Change about me information
  -  Change registration information (email, password, name, preferred instrument)
  -  Update changes button updates all information changed in the form
  -  Go back returns to the users profile page

-  

### Features to Implement

- 5 star system where users can give a rating to the piece they review. 

##### Back to [top](#table-of-contents)

---

## Technologies Used

---

- HTML

  - This project uses HTML to create the main functions of the website.
  - [HTML](https://en.wikipedia.org/wiki/HTML)

- CSS

  - This project uses CSS to add styling to features. It is also used to tweak some of the bootstrap. (Sass is also used to achieve this.)
  - [CSS](https://en.wikipedia.org/wiki/CSS)

- Python

  - This project uses Python for the main database related features. It ensures that all information shared between MongoDB and the project are accessible and respond to one another.
  - [Python](https://en.wikipedia.org/wiki/Python_(programming_language))


- Javascript

  - This project uses Javascript to create functions, rules and effects in order to make the certain features work. Features include being able to use a music player. Updating and showing dropdown menus for genre/instruments. Shrink the number of words on a review card until read more is clicked if over a certain amount.
  - [Javascript](https://en.wikipedia.org/wiki/JavaScript)


##### Back to [top](#table-of-contents)

---

## Testing

---

### Validators

- HTML

  - [W3C HTML Validator](https://validator.w3.org/) "Document checking completed. No errors or warnings to show."

- CSS

  - [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) "Congratulations! No Error Found. This document validates as CSS level 3 + SVG !"

- JSHint

  - [JSHint javascript Validator](https://jshint.com/) 


### Testing Methods

For information on the testing, follow the link to the document [here](testing.md)

##### Back to [top](#table-of-contents)
---

## Deployment

---



### Local Deployment



### Remote Deployment



##### Back to [top](#table-of-contents)
---

## Credits

---

### Content

- All written content was my own.


### Media

- [Pixabay](https://pixabay.com/photos/grass-lawn-backdrop-background-84622/) - Main home image
- Uploaded piano pieces were performed by myself
- Alton towers theme was downloaded from [here]()
- All images used for uploading are found on [google images](www.google.com) by using images/tools/usage rights/commercial and other licenses.
- For the purpose of this project I have used sheet music that is already made.  


### Acknowledgements



##### Back to [top](#table-of-contents)
