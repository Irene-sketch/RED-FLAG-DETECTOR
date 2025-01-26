# Red Flag Detector 🎯


## Basic Details
### Team Name: ByteSquad


### Team Members
- Member 1: Shadha Mohamed Shareef - TKM College of Engineering
- Member 2: Anju V B - TKM College of Engineering
- Member 3: Irene Treessa Raj - TKM College of Engineering

### Hosted Project Link
[mention your project hosted project link here]

### Project Description
The "Red Flag Detector" is designed to help users identify and recognize problematic behaviours, patterns, or warning signs across various life contexts such as relationships, business, mental health, and social situations. By utilizing a combination of user inputs and data aggregation, this empowers individuals to make informed decisions by flagging potential issues before they escalate into more significant problems

### The Problem statement
Today’s fast-paced world, individuals often encounter complex relationships, communication challenges, and uncertain decisions in their personal and professional lives. Identifying unhealthy behaviors, potential risks, or harmful patterns—commonly referred to as "red flags"—can be difficult. Many people struggle to recognize subtle signs of toxicity in relationships or communication, leading to prolonged emotional, mental, and even physical distress.There is a need for a tool that helps users spot these red flags early, whether in interpersonal relationships, professional environments, or other decision-making processes.

### The Solution
We Create a Red Flag Detector App that uses quizzes, behavioral analysis, AI-driven suggestions, and educational resources to help users identify potential red flags in various aspects of life, including personal relationships, professional settings, and other decision-making processes.
- User Categories:
Relationship Red Flags: Detect warning signs in personal relationships such as emotional manipulation, dishonesty, disrespect, or toxic behavior.
Professional Red Flags: Help users identify toxic workplace culture, unethical behavior, poor management, or potential job-related risks.
Financial Red Flags: Assist users in recognizing signs of financial fraud, risky investments, or unethical business practices.
Health and Wellness Red Flags: Educate users on early symptoms of potential health issues or unhealthy lifestyle habits.
Self-Reflection Red Flags: Allow users to assess their own behaviors for negative patterns like procrastination, poor decision-making, or emotional instability.
-Interactive Quizzes:
Each user category will feature customized quizzes that users can take to assess whether they are facing any red flags in their current situation.
Example questions could assess communication styles, behaviors observed in others, financial choices, or emotional well-being.
After completing a quiz, users will receive a score indicating the presence of potential red flags and an explanation of the results.

## Technical Details
### Technologies/Components Used
For Software::
Languages used
: Python,HTML,CSS,Javascript,Jinja 2
Frameworks used
: Flask,CSS,HTML,Javascript,Jinja 2
Libraries used
: Javascript,Jinja 2, Flask, JSON
Tools used
: ChatGPT

### Implementation
For Software:
# Installation
cd red-flag-detector
git init
git add .
git commit -m "Initial commit"
git tag -a v1.0-init -m "Project initialization with basic structure."
git tag -a v1.0-init -m "Project initialization with basic structure."
git add .
git commit -m "Frontend implementation completed."
git tag -a v1.1-frontend -m "Frontend implemented with HTML, CSS, and JavaScript."
git add .
git commit -m "Backend implementation completed."
git tag -a v1.2-backend -m "Backend implemented using Flask."
git add .
git commit -m "Full project with frontend, backend, and deployment ready."
git tag -a v1.3-full-project -m "Full project ready for deployment."


# Run
cd red-flag-detector
git init
git add .
git commit -m "Initial commit: Project setup and basic structure"
git tag -a v1.0-init -m "Project initialization with basic structure."
git add .
git commit -m "Frontend implementation completed."
git tag -a v1.1-frontend -m "Frontend implemented with HTML, CSS, and JavaScript."
git add .
git commit -m "Backend implementation completed."
git tag -a v1.2-backend -m "Backend implemented with Flask."
git add .
git commit -m "Full project ready, including frontend, backend, and deployment setup."
git tag -a v1.3-full-project -m "Full project ready for deployment."
git tag
git remote add origin <your-repo-url>
git push origin main --tags
git push --tags


### Project Documentation
For Software:

# Screenshots (Add at least 3)
![Screenshot1]
![image](https://github.com/user-attachments/assets/7ae1fee6-196d-4ebe-bf0c-e6b9c8fe3c6f)

:This HTML code creates a simple web page for a "Red Flag Detector" with a welcoming interface and two action buttons. Here's a brief breakdown of what happens in the code: HTML Structure:
The document uses a basic HTML structure with <!DOCTYPE html> and <html lang="en">, specifying the document type and language.
The <head> section includes metadata such as character encoding (UTF-8), viewport settings for responsive design, and the title of the webpage (Red Flag Detector).
A link to an external CSS file (style.css) is added using Flask's url_for function to apply additional styling.
Page Layout and Content:
The <body> has an inline style to set the background color to a soft red shade (rgb(226, 178, 178)).
Inside the <body>, there's a <div class="container"> that holds the main content:
A large, centered element with the text "Welcome to Red Flag Detector" in red color.
A paragraph (<p>) briefly explaining the purpose of the page, encouraging users to analyze situations for red flags.
A div class .options holds two buttons that link to other parts of the website:
The first button labeled "Go to Detector" takes the user to the /detector page when clicked.
The second button labeled "Take a Quiz" redirects the user to the /categories page for quizzes.
Footer:
At the bottom, a <footer> section includes a copyright message (© 2025 ByteSquad. All Rights Reserved.).
Navigation:
The buttons use the onclick attribute to trigger navigation to different URLs when clicked (/detector and /categories).
In summary, this code builds a simple homepage for the Red Flag Detector, offering users two options to either access the detector tool or take a quiz, with basic styling and layout.

![Screenshot2]
![image](https://github.com/user-attachments/assets/f09df42a-9fc5-45d5-8eb5-e93194228562)
:This code creates a simple webpage called "Red Flag Detector" where users can enter text to check for red flag keywords. Here's a breakdown of what's happening:
1. HTML Structure:
The page uses basic HTML and CSS for structure and styling, along with a simple JavaScript function for interactivity.
The <head> section includes metadata like character encoding, viewport settings for responsive design, and a link to the Google Fonts service to import the Poppins font.
2. Styling (CSS):
Gradient background animation: The body has a gradient background animation that shifts colors in a smooth cycle using the @keyframes gradient rule.
Container styling: A centered white box with a shadow (.container) holds the page's content.
Animations:
Elements like the text, container, and buttons use the fadeIn and slideIn animations to smoothly appear on the page.
Text area and button styling: The text area and button are styled with padding, borders, and background colors. The button changes color when hovered.
Footer: A fixed footer at the bottom of the page displays a copyright message.
3. Main Content:
Header and Introduction:
The title "Red Flag Detector" is displayed in red, and there's a paragraph explaining the tool's purpose—helping users identify red flags in communication or situations.
Text Input Area:
Users can type their text in a textarea element to be analyzed for potential red flags.
Submit Button:
The button labeled "Check for Red Flags" triggers a JavaScript function to analyze the entered text.
4. JavaScript Function:
The detectRedFlags() function runs when the button is clicked:
It retrieves the text entered by the user from the textarea.
It checks the text for specific red flag keywords (such as "scam", "fraud", "abuse", etc.) stored in the redFlags array.
If the text contains any of these keywords, it displays them in the results box.
If no red flags are detected, it shows a message saying, "No red flags detected."
The result is displayed inside a previously hidden div with the class result, which becomes visible once the function runs.
5. Footer:
A simple copyright message (© 2025 Team ByteSquad. All rights reserved.) is displayed at the bottom of the page.
6. Animations:
The gradient background transitions smoothly through various colors using a @keyframes gradient animation.
Elements fade in and slide in as they load using fadeIn and slideIn keyframe animations.
In summary, this webpage allows users to input text, check it for red flags using predefined keywords, and view the results in a clean, animated interface. The main interactive feature is the JavaScript function that detects red flag terms.

![Screenshot3]
![image](https://github.com/user-attachments/assets/b1d4f187-cb1d-46c0-9f27-3e49d73f35e0)

:This code generates a visually engaging webpage where users can pick a quiz category. Here's a breakdown of the functionality:
1. HTML Structure:
The page consists of a quiz container with a heading "Pick a Quiz Category" and a list of category links that users can choose from.
The quiz container is styled as a centered box with a red flag image above it and animated buttons that link to specific quizzes. The categories are dynamically generated using templating ({% for category in categories %}), indicating server-side rendering, likely from a backend framework like Flask.
2. CSS Styling and Animations:
Body:
The body has a gradient background that shifts colors diagonally using the @keyframes gradientShift animation. The body content is centered vertically and horizontally on the page.
Floating Red Flags:
Four red flags float around the screen in different positions. The floating effect is achieved using @keyframes floatFlag (which moves the flags up and down) and @keyframes rotateFlag (which slightly rotates them for a waving effect).
Quiz Container:
The quiz container is styled with a white semi-transparent background and a red border, positioned centrally on the page. It includes a red flag image positioned above the container, which also waves back and forth (@keyframes wave).
Category Links:
The categories are displayed as red flag buttons. These buttons have a bounce effect created using the @keyframes bounceButton animation, making them subtly move up and down.
On hover, the buttons change color, grow slightly, and have an added shadow for a 3D effect, making them more interactive and attractive to click.
Particles:
Small particles (confetti-like) float down the screen, created by the particleMove animation, adding a subtle decorative effect. The particles gradually move down and fade out as they fall.
3. Dynamic Content:
Templating:
The list of quiz categories is populated dynamically using a server-side templating system ({% for category in categories %}). Each category is displayed as a clickable button, linking to the quiz URL based on the category name (/quiz/{{ category }}).
4. JavaScript (Potential Backend Integration):
Though not visible in this snippet, the backend likely provides the list of categories for the template. When a category is selected, it redirects the user to a specific quiz page for that category (/quiz/{{ category }}).
Summary:
This code creates an interactive and animated webpage where users can select a quiz category. The design features floating red flags, animated buttons, and particle effects, making the page visually appealing. The category list is dynamically generated from the backend, and the quiz container invites users to choose a quiz through engaging animations.
![Screenshot4]
![image](https://github.com/user-attachments/assets/d3a4886a-2da0-4de4-a855-889b56451c21)

![Screenshot5]
![image](https://github.com/user-attachments/assets/2d017bd3-42bd-441a-8751-4b712fdaf144)
:This code creates an interactive quiz on a webpage, called "Find the Real Red Flags 🚩", where users can answer questions and identify potential "red flags" (indicators of problematic behavior or situations). Here's a breakdown of what's happening:
1. HTML Structure:
The page has a simple structure, including floating red flags, a quiz container with questions, and a submission button. The quiz is populated dynamically with questions and options using templating syntax ({% for question in questions %}), indicating that this code is part of a server-side application (like Flask in Python).
2. CSS Styling:
General Styles:
The body uses a Poppins font, and the content is centered on the page.
The overflow: hidden ensures that content does not scroll off the page, while the height: 100vh makes the content fill the entire viewport.
Animated Gradient Background:
The body background has a gradient animation that smoothly transitions through colors using the @keyframes gradient rule.
Floating Red Flags:
Multiple .floating-flag div elements are created, representing small red flags that float around the page. Their positions and animations differ slightly to create a lively effect.
Each flag moves up and down with a slight rotation using the @keyframes float animation.
Quiz Container:
The quiz form is placed inside a container (.quiz-container) with a white background, padding, rounded corners, and a drop shadow.
The container slides in from the bottom when the page loads using the slideIn animation.
Animated Header:
The quiz title "🚩 Red Flag Quiz 🚩" has a glow effect, which pulsates continuously using the fadeInGlow animation.
Question Shake Animation:
The question text shakes slightly to draw attention using the shake animation.
Button Animation:
The submit button (.submit-btn) changes background color and rotates slightly when hovered over, giving it a dynamic feel.
Result Fade-in:
The result text fades in smoothly once displayed using the fadeInResult animation.
3. Dynamic Quiz Content:
Templating:
The questions and options are dynamically inserted into the form using templating syntax ({% for question in questions %}). This suggests the quiz content is rendered on the server-side and sent to the client.
Each question is associated with multiple answer options (using radio buttons), and users can select only one answer per question.
4. Form Submission (JavaScript):
When the form is submitted, the JavaScript function intercepts the form submission with event.preventDefault(), preventing the page from reloading.
Form Data Handling:
The form data is collected using FormData and stored in an answers object, where the key is the question ID (derived from the input name) and the value is the user's selected answer.
AJAX Request:
An asynchronous POST request is sent to the server (at the /result endpoint) with the category and the user's answers as a JSON payload.
Displaying Results:
Once the server responds with the quiz results (the number of red flags identified and the total number of questions), the results are displayed in the result div.
The result message either warns the user about red flags ("🚩 Watch out for those red flags!") or reassures them that they're safe ("👍 You're in the clear!").
5. Back-end Integration:
The form's action is handled server-side (likely Flask), where the server processes the quiz responses and returns the result via JSON.
In summary, this code creates a visually engaging and interactive quiz where users answer questions to spot red flags. It uses animations to enhance the user experience, and JavaScript is used to handle form submission without page reloads, sending data to the server and displaying the results dynamically.
![Screenshot6]
![image](https://github.com/user-attachments/assets/41a33cef-ac69-4550-b089-63230597a4fc)

# Diagrams
[Homepage]
   |
   |--- [Option 1: Go to Detector] ---> [Input Description] ---> [POST /detector]
   |                                          |
   |                                          V
   |                                  [Analyze Description]
   |                                          |
   |                                       [Result]
   |
   |--- [Option 2: Take a Quiz] ---> [Pick Category] ---> [GET /quiz/{{category}}]
                                                 |
                                                 V
                                         [Display Questions]
                                                 |
                                         [Submit Answers] ---> [POST /result]
                                                 |
                                                 V
                                              [Result]


### Project Demo
# Video
https://drive.google.com/file/d/1ja2HOBftyEi3YadI5wNG_-TrCiKntGjj/view?usp=sharing


## Team Contributions
- Shadha Mohamed Shareef: care.html index.html and app.py
- Anju V B: quiz.html, detector.html Documentation
- Irene Treessa Raj: relation.html and  behaviour.html

---
Made with ❤️ at TinkerHub
