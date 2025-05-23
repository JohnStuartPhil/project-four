# BAND HOUSE

BAND HOUSE is a fictional venue where up and coming bands go to perform. When a band/solo artist plays there, the administrator of the website uploads a review on the band and invites registered users of the website to give their own opinions on the bands. The website runs in the mock terminal on Heroku. 

## Display on a mobile and a tablet :
![display on a mobile](/assets/imagesforreadme/mobile.png) ![display on a tablet](/assets/imagesforreadme/tablet.png)

## Dsiplay on a desktop:
![display on a desktop](/assets/imagesforreadme/desktop.png)


## Features of the website


## NAVIGATION BAR

**From left to right, the navigation bar clearly displays the following:**
- The BAND HOUSE name 
- Link to the Home page
- Link to the Bands page 
- Link to Sign Up page (only displays when the user is signed out) 
- Link to Sign In page (only disolays when the user is signed out) 
- Link to Sign Out (only displays when the user is signed in) 
- A slogan on the far right of the Nav bar

### What the user sees while signed out:
![display of nav bar while signed out](/assets/imagesforreadme/navbarsignedout.png)

### What the user sees while signed in:
![display of nav bar while signed in](/assets/imagesforreadme/navbarsignedin.png)

## Navigation bar tests

| Test  | Section  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| Remainig on the Home page  | Navigation Bar | Clicked on Home while on the Home page  |  The user remained on the Home page | Pass  |
| Navigating to the Bands page while on the Home page  |  Navigation Bar | Clicked on Bands while on the Home page   | Took the user to the Bands page  |  Pass |
| Navigating to the Register page while on the Home page  |  Navigation Bar  | Clicked on Register while on the Home page   | Took the user to the Sign Up page   | Pass  |
| Navigating to the Login page while on the Home page | Navigation Bar  | Clicked on Login while on the Home page  | Took the user to the Sign In page  | Pass  |
| Navigating to the Logout page while on the Home page |  Navigation Bar  | Clicked on Logout while on the Home page   | Took the user to the Sign Out page  |  Pass |
|  - |   |    |   |   |
| Navigating to the Bands page while on the Home page  |  Navigation Bar  | Clicked on Bands while on the Home page  | Took the user to the Bands page  | Pass  |
| Remainig on the Bands page  | Navigation Bar   | Clicked on Bands while on the Bands page  | The user remained on the Bands page  |  Pass |
| Navigating to the Sign Up page while on the Bands page  |  Navigation Bar  |  Clicked on Register while on the Bands page | Took the user to the Sign Up page |  Pass |
| Navigating to the Sign In page while on the Bands page  |  Navigation Bar  | Clicked on login while on the Bands page | Took the user to the Sign In page |  Pass |
| Navigating to the Sign Out page while on the Bands page  |  Navigation Bar  | Clicked on Logout while on the Bands page | Took the user to the Sign Out page |  Pass |
| - |   |  |  |  |  
|  Navigating to the Home page while on the Sign Up page |  Navigation Bar  |  Clicked on Home while on the Sign Up page  | Took the user to the Home page  | Pass  |
|  Navigating to the Bands page while on the Sign Up page |  Navigation Bar  |   Clicked on Bands while on the Sign Up page |  Took the user to the Bands page | Pass  |
|  Remainig on the Sign Up page |   Navigation Bar |  Clicked on Sign Up while on the Sign Up page  |  The user remained on the Sign Up page | Pass  |
|  Navigating to the Login page while on the Sign Up page |  Navigation Bar  | Clicked on Login while on the Sign Up page   |  Took the user to the Sign In page | Pass  |
|  Navigating to the Logout page while on the Sign Up page |  Navigation Bar  |  Clicked on Logout while on the Sign Up page  | Took the user to the Sign Out page  | Pass  |
| - |   |  |  |  |  
| Navigating to the Home page while on the Sign In page | Navigation Bar | Clicked on Home while on the Sign In page | Took the user to the Home page | Pass |
| Navigating to the Bands page while on the Sign In page | Navigation Bar | Clicked on Bands while on the Sign In page | Took the user to the Bands page | Pass |
| Navigating to the Register page while on the Sign In page | Navigation Bar | Clicked on Register while on the Sign In page | Took the user to the Sign Up page | Pass |
| Remainig on the Sign In page | Navigation Bar | Clicked on Sign In while on the Sign In page | The user remained on the Sign In page | Pass |
| Navigating to the Sign Out page while on the Sign In page | Navigation Bar | Clicked on Sign Out while on the Sign In page | Took the user to the Sign Out page | Pass |
| - |  |  |  |  |  
| Navigating to the Home page while on the Sign Out page | Navigation Bar | Clicked on Home while on the Logout page | Took the user to the Home page | Pass |
| Navigating to the Bands page while on the Sign Out page | Navigation Bar | Clicked on Bands while on the Logout page | Took the user to the Bands page | Pass |
| Remainig on the Sign Out page | Navigation Bar | Clicked on Sign Out while on the Sign Out page | The user remained on the Sign Out page | Pass |
| - | | | | |




## HOME PAGE

The Home page to the left displays a portrait picture of a stage set for a band to play. To the right, is a description of BAND HOUSE. It invites up and coming bands/solo artists to come and perform for them and advises them of what they would be provided with if they were to perform there and the benefits of performing there.

### The Home Page
![display of top of Home page](/assets/imagesforreadme/homepagetop.png)

Below the description about BAND HOUSE is a form that invites interested bands in performing at BAND HOUSE to contact the venue. The interested party is required to provide the following information: 
- The name of their band 
- Their name (the person who is making contact) 
- Their email address 
- Information about their band 

The user must be signed in to receive a response

### The form for interested bands to complete
![display of the band form](/assets/imagesforreadme/bandformfilledin.png)

### Message received when the form is sucessfully sent
![display message received](/assets/imagesforreadme/messagereceived.png)

### Message received in the Django admin
![display message received in django admin](/assets/imagesforreadme/messagereceivedfromhomepageform.png)

### Django admin reading the message
![display message being read in django admin](/assets/imagesforreadme/adminreadingthemessage.png)

The administrator can then click Read when the message has been read



## Tests on the Home page

| Test  | Section  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| Clicking on the submit button with all fields empty | Form on Home page | Clicked on submit button with all fields empty | User is prompted to fill in the Your band name field | Pass |
| Clicking on the submit button with only the Name of your band field filled in | Form on Home page | Filled in Your band name field then clicked on submit | User is prompted to fill in the Your name field | Pass |  
| Clicking on the submit button with only the Name of your band and Your name fields filled in | Form on Home page | Filled in Your band name field and Your name field then clicked on submit | User is prompted to fill in the email field | Pass |
| Clicking on the submit button with only the Name of your band and Your name fields, and text only but no @ sign in the Email section filled in | Form on Home page | Filled in the Name of your band and Your name fields and text only but no @ sign in the Email section  then cliked on submit | User is prompted to include an @ sign in the email field | Pass |
| Clicking on the submit button with only the Name of your band and Your name fields, and an @ sign only in the email field filled in | Form on Home page | Filled in email field with @ sign only  then cliked on submit | User is prompted to fill in pre-text before the @ sign and post-text after the @ sign | Pass |
| Clicking on the submit button with only the Name of your band and Your name fields, and pre-text, an @ sign and post-text in the email field filled in | Form on Home page | Filled in email field with pretext then an @ sign then post-text  then cliked on submit | User is prompted to fill in the Tell us about your band field | Pass |
| Clicking on the submit button with only the Name of your band and Your name fields, pre-text, an @ sign and post-text in the email field and at least one characher in the Tell us about | Form on Home page | Filled in the Tell us about your band field with at least one character then cliked on submit when signed in | Message at top of screen reads: Request to play at BAND HOUSE received! We aim to respond within 2 working days. The message can be read in the admin section of Django | Pass |
| Clicking on the submit button with only the Name of your band and Your name fields, pre-text, an @ sign and post-text in the email field and at least one characher in the Tell us about your band field | Form on Home page | Filled in the Tell us about your band field with at least one character then cliked on submit when not signed in | The message is not sent to Admin and the page is directed to the top stating that the user is not logged in. | Pass |
| - | | | | |


## BANDS PAGE
The Band page clearly displays each band paginated into 6. 
The bands are displayed in date order with the most recent bands having been written about being displayed first. At the bottom of the display, there is a NEXT button which when clicked on, displays the next 6 bands. 
When the next 6 bands are displayed, there are two buttons at the bottom of the screen. The one on the left says PREV while the one on the right says NEXT. If the PREV button is clicked on, it takes the user back to the previous page while if the NEXT button is clicked on, it takes the user onto the next 6 oldest bands. When the last 1 – 6 bands are reached, only a PREV button appears which would take the user back to the previous 6 bands. 

Each band displays the following information: 
The name of the band, the genre of music that the band plays, number of members in the band, an excert containing a brief description of the band: 
The band can be clicked on anywhere on the name of the band/genre/number of members/excert which takes the user to a separate page featuring more details about the band. 


### First batch of Bands displayed with NEXT button:
![display of bandpost when signed out no opinions](/assets/imagesforreadme/bandsnext.png)

### Middle batch of Bands displayed with NEXT and PREV buttons:
![display of bandpost when signed out no opinions](/assets/imagesforreadme/bandsnextprev.png)

### Last batch of Bands displayed with PREV button:
![display of bandpost when signed out no opinions](/assets/imagesforreadme/bandsprev.png)

The bands listed in this project were initially put onto a json file then uploaded into the Django admin page. 

### Tests on bands

| Test  | Section  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| Clicking on the bands | Bands | Used the mouse to over on any of the bands over the name, genre, number of members or except | Details of the band (name/genre/number of members/except) turns red | Pass |
| Clicking on the bands | Bands | Clicked on any of the bands over the name, genre, number of members or except | User taken into each individual bandpost | Pass |
| Clicking on the NEXT button | Bands | Clicked the NEXT button | Took the user to the next batch of bands | Pass |
| Clicking on the PREV button | Bands | Clicked the PREV button | Took the user to the previous batch of bands | Pass |
| - | | | | |

## BANDPOST PAGES

When the bandpost is clicked on, a new page is brought up in the display. This shows the following information. 
At the top left of the bandpost, is the name of the band in capital letters and underneath, the date that the bandpost was written. On the top right of the post is a generic picture of musicians playing on a stage. 
Directly below the top left and top right is a more detailed description about the band which fills out across the screen. 
Below the description is a speech bubble showing a number next to it. This number is the number of published opinions.
Underneath what has been described above, the remainder of the page is in two parts
On the left are a list of published opinions (if there are any).

### An example of a bandpost when the user is not signed in and there are no published opinions to display:
![display of bandpost when signed out no opinions](/assets/imagesforreadme/bandpostsignedoutnoopinions.png)

### An example of a bandpost when the user is signed in and there are no published opinions to display:
![display of bandpost when signed in](/assets/imagesforreadme/bandpostwhensignedin.png)

On the right is the option to leave an opinion of the band on which the user has clicked on. The user must be signed in, in order to be leave an opinion. Underneath where the user inputs their opinion are two dropdown menus. The first dropdown asks the user to rate the band by selecting very bad, bad, average, good or very good. The other dropdown menu asks the user if they would see the band again. The options on this one are yes, no or maybe. 

### Where the user gives their opinion:
![display of where the opinion is given](/assets/imagesforreadme/opinioniswritteninhere.png)

Underneath where the user provides their opinions is a submit button. When the user clicks on that, it submits the entered information and displays it on the left of the page. This information shows but is initially shown as faded. Underneath the opinion is a message advising that it is awaiting authorisation to be published. A message also appears at the top of the screen thanking them for their opinion and that it is awaiting authorisation to be published. 

### Message at top of screen when opinion submitted:
![display message at top of screen when opinion submitted](/assets/imagesforreadme/topmessageopinionsubmitted.png)

### Opinion shown faded on left of screen:
![display opinion submitted prior to being authorised](/assets/imagesforreadme/submittedopinionpriortoauthorisation.png)

The information that has been submitted is shown as faded out on the left of the screen. It also states 'This opinion is awaiting approval'. Below that are two buttons, Edit and Delete. 
When the Edit button is clicked on, it re-enters the previous text given in the opinion filled into the opinion box. The user can the re-enter their information. They must also re-enter the two dropdown menus (even if they wish to select the same options as previously). Also, when the Edit button is clicked on, the ‘Submit’ button becomes the ‘Update’ button. 

### Edited opinion prior to being authorised:
![display opinion submitted prior to being authorised](/assets/imagesforreadme/editedopiniontoupdate.png)


When the Update button is clicked on a message at the top appears thanking the user for updating their opinion and that it is awaiting authorisation to be published. 

### Message at top of screen advising opinion updated:
![display opinion submitted prior to being authorised](/assets/imagesforreadme/topmessageupdateopinion.png)

### Faded updated opinion shown at on left:
![display opinion submitted prior to being authorised](/assets/imagesforreadme/updatedopinionpriortoauthorisationonleft.png)


Publishing the opinion:
Inside the admin page, the superuser must click on Opinions. The users is then presented with the opinions that have been provided. There is an option to approve the opinion by clicking the small tick box. If the superuser chooses to do this, they then must click the save button. The superuser is also free to edit the opinion themselves if they so choose to. The superuser also has the option to press the delete button which would delete the opinion altogether. This would not notify the user that submitted the opinion but the user would no longer be able to view the opinion. 
If the superuser decides to authorise the opinion, the text that the user has submitted, the rating and the question of whether they would see the band again appear unfaded. Anyone, signed into the website or not signed into the website alike can view the opinion. 

### Authorising the publishing of the opinion in Django admin
![display authorising the opinion indjango admin](/assets/imagesforreadme/approvebandpostinadmin.png)

### Published opinion shown at on left:
![display published opinion on left](/assets/imagesforreadme/opinionpublishedonleft.png)

If the user chooses to Edit their now published opinion, as previously mentioned, they can then re-enter their information and click on the ‘Update’ button. This shall then show a message at the top of the screen thanking them for updating their opinion and that it is currently awaiting authorisation to be published. The information re-entered returns to the faded display and also advises them that the opinion is awaiting authorisation to be published. 

### Editing the opinion after it has been published:
![display editing opinion after it has been published](/assets/imagesforreadme/editingopinionafterithasbeenpublished.png)

### Message at top after editing:
![display message at the top after editing](/assets/imagesforreadme/messageattopafterupdatingopinion.png)

### Opinion faded again as awaiting for update to be published:
![display opinion faded again as awaiting for update to be published](/assets/imagesforreadme/opinionfadedagainafterediting.png)

The user can choose to delete their own opinions at any time, published or awaiting authorisation to be published alike. When they click on the delete button they are initially presented with a modal. The modal asks the user if they are sure that they want to delete the opinion because if they choose do so, it shall not be retrievable. If the user does not wish to delete at that stage, they can click the close button. If they are certain that they wish to delete the opinion, they can click the Delete button in the modal and a message shall appear at the top of the screen advising them that their opinion has been deleted. 

### Asking the user if they are sure they wish to delete:
![display asking user if they are sure they wish to delete](/assets/imagesforreadme/areyousureyouwishtodelete.png)

### After the opinion has been deleted:
![display showing that the opinion has been deleted](/assets/imagesforreadme/afterdeletion.png)


### Tests on entering an opinion

| Test  | Section  | Action  | Result  | Pass/Fail  |
|---|---|---|---|---|
| Clicking on the submit button with all fields empty | Leave your opinion on this band | Clicked on submit button with all fields empty | User prompted to fill in the Your opinion field | Pass |
| Clicking on the submit button with only the Your opinion field filled in | Leave your opinion on this band | Clicked on submit button with only the Your opinion field filled in | User prompted to fill in the Please rate the band field | Pass |
| Clicking on the submit button with only the Your opinion and the Please rate the band fields filled in |Leave your opinion on this band  | Clicked on submit button with only the Your opinion and Please rate the band fields filled in | User prompted to fill in the Would you see this band again field | Pass |
| Clicking on the submit button with all the fields filled in | Leave your opinion on this band | Clicked on submit button with all fields filled in | A message at the top of the screen appears advising that the opinion is awaiting authorisation and the opinions provided appear on the left of the screen faded out also with a message advising that the opinions are awaiting to be published. Edit and Delete buttons also appear under the opinion provided | Pass |
| Viewing the submitted opinion awaiting authorisation while signed out | Leave your opinion on this band | Signed out and searched for submitted opionion | Could not view this as only published opinions can be viewed when signed out | Pass |
| Viewing the submitted opinion awaiting authorisation while signed in as another user | Leave your opinion on this band | Signed in as another user and searched for submitted opionion | Could not view this as only the user that has submitted the unauthorised opioion can see their own opinions | Pass |
| - | | | | |


### Tests on Editing unpublished opinions

| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Edit button | Leave your opinion on this band | Clicking on the Edit button of the unpublished opinion | The text in the Your opnion reappeared in the Your opinion field, the Please rate this band field and the Would you see this band again field showed as empty, the Submit button swicthed to the Update button | Pass |
| Clicking on the Update button without altering anything in the Leave Your Opinion on this band section | Leave your opinion on this band | Clicked on the Update button having not altered anything in the Leave your opinion on this band field | User is prompted to fill in the Please rate this band section | Pass |
| Clicking on the Update button only filling in the Please rate the band field | Leave your opinion on this band | Clicked on the Update button only having filled in the please rate the band field | User prompted to fill in the Would you see this band again field | Pass |
| - | | | | |
| Clicking on the Update button only filling in the Please rate the band and Would you see this band again fields | Leave your opinion on this band | Clicked on the Update button  | A message appears at the top of the screen confirm that the updated opinion has been receieved and is awaiting authorisation and the same text as before appears on t he left of the screen and the updated Please rate the band and Would you see this band again fields updated. A message also advising that the opinion is awaiting authorisation also appears. The Information on the left of the screen is faded | Pass |
| Clicking on the Update button altering the Your opinion field | Leave your opinion on this band | Changed the text in the Your opinion filed | User is prompted to fill in the Please rate this band section | Pass |
| Clicking on the Update button having chaged the text in the Your opinion field and filled in the Please rate the band field | Leave your opinion on this band | Clicked on the Update button only having chaged the text in the Your opinion field and filled in the Please rate the band field | User prompted to fill in the Would you see this band again field | Pass |
| Clicking on the Update button chaged the text in the Your opinion field and filled in the Please rate the band and Would you see this band again fields | Leave your opinion on this band | Clicked on the Update button  | A message appears at the top of the screen confirm that the updated opinion has been receieved and is awaiting authorisation and the same text as before appears on t he left of the screen and the updated Please rate the band and Would you see this band again fields updated. A message also advising that the opinion is awaiting authorisation also appears. The Information on the left of the screen is faded | Pass |
| - | | | | |


### Tests on Editing published opinions

| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Edit button | Leave your opinion on this band | Clicked on the Edit button of the published opinion | The submit Button became the Update button and the published text appears in the Your opinion field | Pass |
| Clicking on the Update button without altering anything in the Leave Your Opinion on this band section | Leave your opinion on this band | Clicked on the Update button having not altered anything in the Leave your opinion on this band field | User is prompted to fill in the Please rate this band section | Pass |
| Clicking on the Update button only filling in the Please rate the band field | Leave your opinion on this band | Clicked on the Update button only having filled in the please rate the band field | User prompted to fill in the Would you see this band again field | Pass |
| Clicking on the Update button only filling in the Please rate the band and Would you see this band again fields | Leave your opinion on this band | Clicked on the Update button  | A message appears at the top of the screen confirm that the updated opinion has been receieved and is awaiting authorisation and the same text as before appears on the left of the screen and the updated Please rate the band and Would you see this band again fields updated. A message also advising that the opinion is awaiting authorisation also appears. The Information on the left of the screen returns to faded | Pass |
| - | | | | |
| Clicking on the Update button altering the Your opinion field | Leave your opinion on this band | Changed the text in the Your opinion filed | User is prompted to fill in the Please rate this band section | Pass |
| Clicking on the Update button having chaged the text in the Your opinion field and filled in the Please rate the band field | Leave your opinion on this band | Clicked on the Update button only having chaged the text in the Your opinion field and filled in the Please rate the band field | User prompted to fill in the Would you see this band again field | Pass |
| Clicking on the Update button chaged the text in the Your opinion field and filled in the Please rate the band and Would you see this band again fields | Leave your opinion on this band | Clicked on the Update button  | A message appears at the top of the screen confirm that the updated opinion has been receieved and is awaiting authorisation and the same text as before appears on t he left of the screen and the updated Please rate the band and Would you see this band again fields updated. A message also advising that the opinion is awaiting authorisation also appears. The Information on the left of the screen returns to faded | Pass |
| - | | | | |


### Tests on Deleting unpublished and published opinions alike 

| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Delete button underneath the opinion | Leave your opinion on this band | Clicked on the Delete button underneath the opinion | A modal appears asking if user if they are sure that they wish to delete the opinion as the action cannot be undone should they choose to delete. The modal contains two buttons, Close and Delete | Pass |
| Clicking on the Close button in the Modal | Leave your opinion on this band | Clicked on the Close button in the modal | The modal disappears and the opinion published in bold or unpublished faded can still be seen | Pass |
| Clicking on the Delete button in the Modal | Leave your opinion on this band | Clicked on the Delete button in the modal | The published or unpublished opinion dissapears along with the Edit and Delete buttons that were underneath it | Pass |
| - | | | | |



## SIGN UP PAGE

When the user clicks on the Sign Up section of the Nav Bar, they are taken to the Sign Up page. 
The first line asks if the user already has an account and a link to the Sign In page if they do have one 

Beneath are the details of what is required. These are the following: 
- Username 
- Email address (this is optional) 
- Password 
Below the password, there are terms and conditions of creating a password 
- Password (again) 
Below that is the Sign-up button
If the user has entered all the correct details, it shall then take them to the Home page.
A message shall appear at the top of the screen advising that they have sucessfully signed in as their new user name but the user can make this disappear by clicking the x.
A permanent display at the top right of the screen also advises them that they are signed in as that user name for as long as they are signed in under that name.  

## The Sign Up page:
![display of Sign Up page](/assets/imagesforreadme/signuppage.png)

The user is asked to provide a Username. The user is requied to make up a Username at this point and enter it. Entering an email address is optional. The user is then asked to make up a password which must meet the following requiremnets:
- The password can’t be too similar to other personal information.
- The password must contain at least 8 characters.
- The password can’t be a commonly used password.
- The password can’t be entirely numeric.

## Unsucessfully signing up:
![display unsucessfully signing up](/assets/imagesforreadme/signupincorrectpassword.png)

## Sucessfully signing up:
![display sucessfully signing up](/assets/imagesforreadme/signupcorrectpassword.png)

### Tests on the Sign Up page:

| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Sign Up button without filling in any fields | Sign Up page | Clicking on the Sign Up button without filling in any fields | User is prompted to fill in the Username field | Pass |
| Clicking on the Sign Up button only having filled in the Username field | Sign Up page | Clicking on the Sign Up only having filled in the User name field | User is prompted to fill in first Password field | Pass |
| Clicking on the Sign Up button only having filled in the Username field and only one password field | Sign Up page | Clicked on the Sign Up button only having filled in the Username field and only one password field | User is prompted to fill in the other Password field | Pass |
| Clicking on the Sign Up button having filled in the Username field and both password fields with both passwords having not met the password requirements | Sign Up page | Clicked on the Sign Up button having filled in the Username field and both password fields having not met the password requirements | Appropriate messages appear between the optional email field and the first password field advising why the password entered cannot be used | Pass |
| Clicking on the Sign Up button having filled in the Username field and both password fields with both passwords meeting the password requirements | Sign Up page | Clicked on the Sign Up button having filled in the Username field and both password fields with both passwords meeting the password requirements | User is taken to the Home page and a message appears at the top of the screen advising they have sucessfully signed in as their new user name | Pass |
| Clicking on the Sign In link on the Sign Up page | Sign Up page | Clicked on the Sign In link on the Sign Up page | User is taken to the Sign In page | Pass |
| - | | | | |



## SIGN IN PAGE

When the user clicks on the Sign In section of the Nav Bar, they are taken to the Sign In page. 
The first line welcomes the user back to the website and advises that to leave opinions on the bands, they must sign in. It also advises that if they do not have an account, they must sign in first. 

Beneath requests the following details 
•	Username 
•	Password 
There is also the Remember Me box which the user can tick which keeps the users details username and dotted out password on their device for future sign ins. 
Below that is the Sign-in button

When the sign in button is clicked, if the correct details have been entered, it takes the user to the Home/Band page

## The Sign In page:
![display of the sign in page](/assets/imagesforreadme/signinpage.png)

## Unsucessfully signing in:
![display unsucessfully signing in](/assets/imagesforreadme/unsucessfullysigningin.png)

## Sucessfully signing in:
![display sucessfully signing in](/assets/imagesforreadme/sucessfullysigningin.png)


### Tests on the Sign In page:
| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Sign In button without filling in any fields | Sign In page | Clicked on the Sign In button without filling in any fields | User is prompted to fill in the Username field | Pass |
| Clicking on the Sign In button filling in the Username but not the password | Sign In page | Clicked on the Sign In button filling in the Username but not the password | User is prompted to fill in the Password field | Pass |
| Clicking on the Sign In button filling in the Username and the incorrect password | Sign In page | Clicked on the Sign In button filling in the Username and an incorrect password | A message above the Usernamefield appears adviug that the username and/or password are not correct | Pass |
| Clicking on the Sign In button filling in the Username and the correct password | Sign In page | Clicked on the Sign In button filling in the Username and the correct password | The user is taken to the home page and a message appears at the top of the screen advising that they have sucessfully signed in | Pass |
| Clicking on the Sign In link on the Sign Up page | Sign Up page | Clicked on the Sign In link on the Sign Up page | User is taken to the Sign In page | Pass |
| - | | | | |


## SIGN OUT PAGE

When the user clicks on he sign out page, they are asked if they are sure that they wish to sign out.

### Asking the user if they are sure they wish to sign out:
![display of the sign out page](/assets/imagesforreadme/areyousuresignout.png)

If they are sure they wish to sign out, they can click the sign out button and a message confirms that they have signed out.

### Confirmation the user has signed out:
![display confimration signed out](/assets/imagesforreadme/confirmationsignedout.png)


### Tests on the Sign Out page:
| Test  | Section  | Action  | Result  | Pass/Fail |
|---|---|---|---|---|
| Clicking on the Sign Out button  | Sign Out page | Clicked on the Sign Out button | User is retunred to the Home page and a message at the top of the screen confirms they have signed out | Pass |
| - | | | | |

## FOOTER

At the bottom of the site is the footer featuring copyright information and links to social media platforms. 

![display of the footer](/assets/imagesforreadme/footer.png)



## Deployment 
- The site was deployed to GitHub pages. The steps to deploy are as follows:

  - Go to the Settings tab of the GitHub repository.
  - In the code and automation section, select Pages.
  - In the build and Deployment section, under the Source section select Deploy from a Branch.
  - In the build and Deployment section, under the Branch section Main branch and Root file.
  - Within a few minutes the live site shall then be refreshed.

## Forking the Repository
- To Folk a repository, the steps are as follows:
  
  - Go to the Code tab of the GitHub repository.
  - Click on the down arrow of the Folk section.
  - This should create a copy of the repository in your own repository.
  - This copy could be used for testing purposes only without affecting the main repository.

## Cloning the Repository
- To make a clone of a repository, the steps are as follows:

  - Go to the Code tab of the GitHub repository.
  - Select a URL provided and copy it to the clipboard.
  - Enter the URL into your browser.
  - Type 'git clone' and the URL into VS Code.
  - This shall bring up the selected repository at the time it was cloned ready to be edited.


# Validators

## PEP8 Python for band_house/settings.py
![display PEP8 for band_house/settings.py](/assets/imagesforreadme/settingspy.png)

## PEP8 Python for band_house/urls.py
![display PEP8 for band_house/urls.py](/assets/imagesforreadme/bandhouseurlspy.png)

## PEP8 Python for bands/admin.py
![display PEP8 for bands/admin.py](/assets/imagesforreadme/bandsadminpy.png)

## PEP8 Python for bands/apps.py
![display PEP8 for bands/apps.py](/assets/imagesforreadme/bandsappspy.png)

## PEP8 Python for bands/forms.py
![display PEP8 for bands/forms.py](/assets/imagesforreadme/bandsformspy.png)

## PEP8 Python for bands/models.py
![display PEP8 for bands/models.py](/assets/imagesforreadme/bandsmodelspy.png)

## PEP8 Python for bands/urls.py
![display PEP8 for bands/urls.py](/assets/imagesforreadme/bandsurlspy.png)

## PEP8 Python for bands/views.py
![display PEP8 for bands/views.py](/assets/imagesforreadme/bandsviewspy.png)

## PEP8 Python for intro/admin.py
![display PEP8 for intro/admin.py](/assets/imagesforreadme/introadminpy.png)

## PEP8 Python for intro/apps.py
![display PEP8 for intro/apps.py](/assets/imagesforreadme/introappspy.png)

## PEP8 Python for intro/admin.py
![display PEP8 for intro/admin.py](/assets/imagesforreadme/introadminpy.png)

## PEP8 Python for intro/forms.py
![display PEP8 for intro/forms.py](/assets/imagesforreadme/introformspy.png)

## PEP8 Python for intro/models.py
![display PEP8 for intro/models.py](/assets/imagesforreadme/intromodelspy.png)

## PEP8 Python for intro/urls.py
![display PEP8 for intro/urls.py](/assets/imagesforreadme/introurlspy.png)

## PEP8 Python for intro/views.py
![display PEP8 for intro/views.py](/assets/imagesforreadme/introviewspy.png)

## PEP8 Python for intro/views.py
![display PEP8 for intro/views.py](/assets/imagesforreadme/introviewspy.png)


## JS Hint for static/js/opinions.js and staticfiles/js/opinions.js 
### (New Javascript features (ES6) assumed)
![display JS Hint for static/js/opinions.js and staticfiles/js/opinions.js](/assets/imagesforreadme/jshint.png)


## W3C CSS Jigsaw for the home page 
### The link to the results can be found below: 
[display Jigsaw CSS Validation results for the home page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
![display W3C valdiator screenshot for the home page](/assets/imagesforreadme/w3ccssforhomepage.png)

## W3C CSS Jigsaw for bands page
### The link to the results can be found below: 
[display Jigsaw CSS Validation results for the bands page](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2Fbands&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
![display W3C valdiator screenshot for the bands page](/assets/imagesforreadme/w3ccssforbandspage.png)

## W3C CSS Jigsaw for bandposts page (using the band Sisoa as the example)
### The link to the results can be found below: 
[display Jigsaw CSS Validation results for the bandpost page using Sisoa as the example](https://jigsaw.w3.org/css-validator/validator?uri=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2Fbands%2Fsisao%2F&profile=css3svg&usermedium=all&warning=1&vextwarning=&lang=en)
![display W3C valdiator screenshot for the bandpost page using Sisoa as the example](/assets/imagesforreadme/w3ccssforbandpostpage.png)


## W3C HTML for the home page 
### The link to the results can be found below:
[display HTML Validation results for the home page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2F)
![display W3C valdiator screenshot for the home page](/assets/imagesforreadme/w3chtmlforhomepage.png)

## W3C HTML for bands page
### The link to the results can be found below:
[display HTML Validation results for the bands page](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2Fbands%2F)
![display W3C valdiator screenshot for the bands page](/assets/imagesforreadme/w3chtmlforbandspage.png)

## W3C HTML for bandposts page (using the band Sisoa as the example)
### The link to the results can be found below:
[display HTML Validation results for the bandpost page using Sisoa as the example](https://validator.w3.org/nu/?doc=https%3A%2F%2Fjsp-project-four-3b23961c0676.herokuapp.com%2Fbands%2Fsisao%2F)
![display W3C valdiator screenshot for the bandpost page using Sisoa as the example](/assets/imagesforreadme/w3chtmlforbandpostpage.png)




# Bugs 

When validating the HMTL code on the Home Page (intro app), multiple errors were occuring in the W3C HTML validator.
This was due to the text being in the intro/models, About model, in a section of the model called about_us using Summernote styling. 
Due to time restrictions and with much regret, the quickest way to resolve this was to remove the about_us section of the model and the use of Summernote and input the text directly into the HMTL in intro\templates\intro\intro.html.

## Multiple errors in HTML validation caused by Summernote
![display errors in HMTL validator](assets/imagesforreadme/multipleerrors.png)

## Admin before about_us part of the model removed
![display admin before about us part of the model removed](assets/imagesforreadme/adminbeforesummernoteremoval.png)

## Admin after about_us part of the model removed
![display jadmin after about us part of the model removed](assets/imagesforreadme/adminaftersummernoteremoval.png)

Two dropdown menus from intro/models, CollaborateRequest model, in sections of the model genre and number_of_members_in_your_band also had to be removed from the contact form on the Home page (intro app) for similar reasons. 


# User Stories 

These are listed in Projects in Github.


# References:

Much of the code is taken from the Code Institute, Code Star Walkthrough project and amended to fit the requirements of the BAND HOUSE website.

Authentication code dowloaded from All Auth.

Stagepic: https://unsplash.com/photos/a-band-playing-on-a-stage-at-a-concert-z93bOEeaRPM

Bandpic: https://www.bigstockphoto.com/image-307835170/stock-photo-live-music-background-and-music-band-on-stage-live-music-and-rock-band-on-stage


# Thanks to: 

- Mentor: Matthew Bodden 
- Tutors: Oisin, Rebecca, Roman 
- Student Care: Eva, Kieron
