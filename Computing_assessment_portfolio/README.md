# Web application, Functionals and Non-functionals

## **Project Definition and Requirements**

**Notes for getting A:**
- Should have forms for review, login
- 3 webpages

### **Web Application Purpose:**
- To give accessibility for users to communicate to other users through group chats or personal chats in friend requests.
- To explore other group chats in the app and chat about common topics.
- (*Optional*) To be able to develop your own inventory and profile by buying badges or upgrading your inventory with cool items through gambling. **Each gambling comes from every 25th message**.

### **Functional:**
- To be able to invite friends onto group chats or start new chats with other people by clicking on invite friend and type up their username or id tag.
- To be able to communicate in chats through posting messages, images, (*optional*: videos and GIFs) in the messaging tab.
- To be able to join servers through pressing an invite button on an explore tab that summarises the purpose of the chat.
- (*Optional*) To be able to spin a wheel by pressing a button, so we can gamble for cool items that can be attached to your profile to make you look cooler.
- (*Optional*) To be able to change your own profile picture by clicking on it.
- To have a login page.
- To be able to customise the app, such as a different background colour.
- Notifications of new messages, or number next to groupchat. 
- **Most of these actions occur from pressing a button.**

### **Non-Functional:**
- Most functions can occur in less than a second.
- Buttons can make a cool clicking sound and move up and down.
- (*Optional*) Gambling wheel spins faster then slower, like roulette
- Messages come in quickly.
- Updates, such as notifications on messages are updated quickly. 

## Basic Design of UI, Hierachy and Interactive Elements

The image below is a screenshot of my first design for UI
![Basic UI: first design of webpage interface](image.png) 

### Colour
The colour here that I wanted to add was a basic, black, dark pink/purple colour, because it matches with the app's colour and is not prominent while messaging friends and getting disgusted or distracted by the colour, but settles the user into the calm, enjoyable setting of a nice chat with friends.

### Typography
The typography here is to be basic, or maybe fancy. I'm not too sure of what to do for it, since I'm not sure what 'vibe' I'm trying to express to in my app, but the size of each text would be reflective of its purpose. More significant text, such as headlines of significant webpages or parts of the webpage are in larger, bolder text, such as chats and vice versa.

### Image/Icon Choice
The images in my webpage are used for a purpose. For instance, the app's icon is the button used to return to the homepage of the app, or the image of the user's profile can be tapped on to see their description for their own customisability. These images should be small, as it is not the main functionals of the website. The functionals of messaging friends through any images used will be expressed in a large size to clearly display the the image to other users.

## Alternative Design - Playing with Possibilities

The image below is a screenshot of my alternate UI design. The group chat, chat, forum and profile customisability design is same as the basic UI design and the method to enter is the same.
![Alternate UI: second design of webpage interface](UI.png) 

### Colour
The colour is similar to the original UI, and is still inspired by the colour scheme of the logo, but now is slightly different shade.

### Typography
I plan to retain the same text type as it already seems appropriate and I like it. I might play around with other text types, depending on if I find any new ones I like.

### Image/Icon Choice
Image and icon choice have remained the same compared to the original UI, because it encompasses the original beauty and simplicity of the website, such as the logo or settings button.

## Designing algorithms - functional steps for user focused design

### Pseudocode
![Flowchart of how functional component works](Alternate_UI.png)

### Test Case
*Test Case ID*
- TC001

*Test Case Name*
- Verify login credentials to provide user access to app

*Preconditions*
- User must have registered account, or an email to access and add new username and password crednetials.

*Test Steps*
- Open application
- Enter username and password
- Press Login button
- Enter homepage

If no username, password:
- Enter user ID
- Type new username and password.
- Type again new username and password to confirm
- Press Enter
- Return to login page.

*Expected Result*
- To enter homepage

*Priority*
- High

**New Test Case**

*Test Case ID*
- TC002

*Test Case Name*
- Operating messaging function in messaging tab.

*Preconditions*
- User must have already logged into app and clicked on another user's icon to enter their messaging tab.

*Test Steps*
- Type in message bar of page.
- Add image in bar with text
- Press enter
- Display message
- Click app icon to return to homepage.

*Expected Result*
- To display typed message on message tab for other user and oneself to see, then return to homepage.

*Priority*
- High

## Adding Interactivity

### Chrome Lighthouse 
![Lighthouse Analysis - Chrome](Chrome_Lighthouse.png)

### Microsoft Lighthouse
![Lighthouse Analysis - Microsoft](Microsoft_Lighthouse.png)