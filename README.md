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
| A   | Music player                   |     5      |         4 |
| B   | Sheet music PDF sharing        |     5      |         4 |
| C   | Image upload                   |     3      |         5 |
| D   | Reviewing                      |     5      |         3 |
| E   | Profile page and updatable info|     3      |         5 |
|     | Total                          |     21     |        21 |

### Responsive

[Am I Responsive?](http://ami.responsivedesign.is/#) was used to test how responsive the website is on different devices.

<img src="static/images/responsive.png">

### Frameworks Used

- [Bootstrap](https://getbootstrap.com/)
- Bootstrap is an open source library with access to reusable bits of code for html, css and javascript. 

- [jQuery](https://jquery.com/)
- jQuery is an open source library that makes using javascript easier and quicker. It simplifies a variety of multiple lines of javascript code by putting it into a single line of jquery code. 

- [Flask]

- []

### Typography

The font Arvo was used as it is a serif font. Serif fonts are known for their roman types. 
As music is associated with latin (as shown with terminology for dynamics), a serif font was appropriate for this project. (https://www.fonts.com/content/learning/fontology/level-1/type-anatomy/type-classifications)

1 [Google Font](https://fonts.google.com/) was used throughout this website:
- ["Arvo", serif;](https://fonts.google.com/specimen/Arvo)

### Colors



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

 - This project uses Javascript to create functions, rules and effects in order to make the certain features work. Features include being able to use a music player. Updating and showing dropdown menus for genre/instruments. 
 Shrink the number of words on a review card until read more is clicked if over a certain amount.
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

\*The [Pokematch repository](https://github.com/adam181189/Pokematch) was developed using GitHub Workspaces, and all commits were pushed to GitHub using Git.

\*Commits were pushed every time important sections were completed in order to create useful ongoing checkpoints.

### Local Deployment

- *In order to locally deploy the website, the following was actioned (using Windows 10): 
1. Navigate to GitHub repository:
    - [adam181189 repository](https://github.com/adam181189?tab=repositories)
2. Open the Pokematch repository:
    - [Pokematch repository](https://github.com/adam181189/Pokematch)
3. Click on the code dropdown option and select download zip
4. Create a new folder called Pokematch and unzip the files in that new folder
5. Now iis is required, this can be done by going to run and typing in appwiz.cpl
6. Now click on turn windows features on or off
7. scroll down to internet information services
8. Open folder and open Web Management tools and tick IIS Management Console
9. Go to This PC and click on the local disk that houses the operating system.
10. Open folder called inetpub
11. inside here find wwwroot
12. Move your pokematch folder into this folder. 
13. Go to the following link http://localhost/pokematch/index.html

### Remote Deployment

- Deployed Site:

  - https://adam181189.github.io/Pokematch/

*In order to deploy the website, the following was actioned:
1. Navigate to GitHub repository:
    - [adam181189 repository](https://github.com/adam181189?tab=repositories)
2. Open the Pokematch repository:
    - [Pokematch repository](https://github.com/adam181189/Pokematch) 
3. Click on the **Settings** tab at the top:
    - [Settings](https://github.com/adam181189/Pokematch/settings)
3. Scroll down to the **GitHub Pages** section.
4. The first drop-down field should be **Source** with *None* pre-selected.
5. Select **master branch** from the list.
6. The page should refresh.
7. Scroll down to the **GitHub Pages** section.
8. There will now be a deployed link:
    - The site is published at [https://adam181189.github.io/Pokematch/](https://adam181189.github.io/Pokematch/)

##### Back to [top](#table-of-contents)
---

## Credits

---

### Content

- Most written content was my own.
- "Welcome to the world of Pokemon, I am the Pokemon professor" is a phrase used at the start of the pokemon games by Professor Oak so was included to introduce him as part of the "how to play" section.

### Media

- [Pixabay](https://pixabay.com/photos/grass-lawn-backdrop-background-84622/) - Grass background image
- [Bulbapedia](https://bulbapedia.bulbagarden.net/wiki/Main_Page) All other images came from this website. All images are copyrighted property of Nintendo.
- [Sounds](https://www.sounds-resource.com/game_boy_gbc/pokemonredblueyellow/sound/17241/) All used sounds were found and downlaoded from this page.
- [Hourglass image](https://www.clipartmax.com/middle/m2i8d3K9i8m2A0Z5_hourglass-clipart-image-hour-glass-clip-art/) Used as part of the timer.

### Acknowledgements

Inspiration for this project was drawn from a video game series I have enjoyed since I was a child, and the need for a simple ICT programme that the 
children can use in my job. We can use this to assess how well the children in our group can complete a program from start to finish, and also help 
to build up memory function skills. 

I also want to thank some of the members on slack May-2020 group as they looked at my project and suggested some changes, and bugs that were in my project. 
I also want to the thank the children at the pre school i work at for playing the game and telling me what they enjoyed about it. 

##### Back to [top](#table-of-contents)
