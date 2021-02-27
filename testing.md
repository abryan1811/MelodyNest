# Memory Nest Testing

---

## User stories


### As a user, I want to be able to share the sheet music I arrange or I compose
- A user can share an their sheet music. 

<img src="static/images/sheetmusicupload.png">

### As a user, I want to be able to share an audio file of the music I performed on my chosen instrument
- A user can share an audio file. 

<img src="static/images/audioupload.png">

### As a user, I want to have a profile page where I can share information about myself in terms of music. 

### As a user, I want to write reviews about the music shared by other users

### As a user, I want to see what others think of the music I have shared

### As a user, I want to see an attractive website that makes me want to use it. 

### As a user, I want to see other users profile pages, and see what they have shared

### As a user, I want to listen to other users performances

### As a user, I want to be able to download some new music that others have shared.



## Bugs

### 

- New users cannot access profiles 

    - This bug was solved by adding a simple if else statement on the user_profile.html. If the length of the useruploads array has 1 or more items inside it, then it loads up the users uploaded music. , else it says user hasnt uploaded any music. 

- MongoDB filling up with unused data

    - 

- When a user updates a new piece, it changes all the other details on genre and instrument to say the same for every piece.(in profile view only).

    - This bug was due to an error in the code written, and was a simple and obvious fix. At the bottom of the user profile, the append to array code (useruploadstitle.append(piece)) needed to go below all the information in the for loop, where as I had it written before. 

## User opinions



##### Back to [readme](README.md)