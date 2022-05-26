## Bite The Jaw (BTJ) - Solo Project

Deployed at: 

![btjlogo2](https://user-images.githubusercontent.com/75817925/168427314-5c471431-0d7d-404d-93dd-c6ef1d60bdcb.png)


## Project Requirements

This project was built for project three of General Assembly's Full-Stack Software Engineering course. The project aim was to build a website/application with our own API, utilise our growing knowledge of React and new-found knowledge of Pytho and Django. The project specs allowed us to take inspiration from complex websites/apps that use data such as AirBnb or Facebook, and essentially rebuild it in our own way if we desire, however, I decided to make a project about things I am passionate about and take inspiration from my own interests.

### Table of contents 

1. Project aims & inspiration 
2. Planning 
3. Build
4. Styling
5. Challenges and Wins
6. Future improvements

### Project aim 

BTJ is a fictional political space where people can express themselves on current affairs, history, philosophy and more. The articles are sorted by categories: Art, Film studies, Philosophy, History, Poltics and Current Affairs. (stretch goal). The articles are accessed and avaliable to view by anyone, however only registered user can submit a submission. 

The functionality of BTJ includes:

- Retrieve articles from the backend and display them to the user
- Register a user
- Login a user
- Submit an article when you are logged in

![image](https://user-images.githubusercontent.com/75817925/169652565-53f93d63-5369-4a1d-89f7-8b1119ced927.png)
![image](https://user-images.githubusercontent.com/75817925/169652576-a36d2e73-20e7-417b-b415-9cd14d90deec.png)
![image](https://user-images.githubusercontent.com/75817925/169652595-ffad7e89-cd44-4424-ad07-0b5815de435c.png)


### Planning 

![BTJ](https://user-images.githubusercontent.com/75817925/168427372-d741fbea-2520-439f-a41b-7db6279dad83.png)

Before the project: My planning started with creating a wireframe using Excalidraw, and speaking with my tutors on ideas that would be doable and sufficient for the project requirements.

During the project: I used Google Docs to keep a daily list of tasks I wanted to/needed to complete day by day, this helped me stay organised and know what to focus on as my next steps, whether that was asking a question from my tutors or implementing a function or styling etc. See example below:

![bjt screenshot readme](https://user-images.githubusercontent.com/75817925/168427352-1d77c206-4185-45de-bc05-0b11f03dafe1.png)

### Build

Frontend: The project utilises React, HTML and CSS. I didn't use any styling frameworks for this project as I enjoy doing my own styling, however for future, I would like to learn how to use some CSS libaries of frameworks. 
How does it work? The front-end fetches data from the local API that I built in the backend and displays the information on the page, thus the articles are dynamic and not hardcoded, users can also register and login which will send data to the API.

Backend: The backend of this project utilises Python, Django and Poetry package manager. I also used Insomnia to test my routes and understand my models/data. I utilised the use of Django Generics and the Django user model, however I adjusted the user model to fit the needs of my project. 

![helloooo](https://user-images.githubusercontent.com/75817925/168429865-92544cd9-edf7-41eb-b784-6e06ebd6b554.png)


### Styling

![btj design outline](https://user-images.githubusercontent.com/75817925/168427385-bea1c2e3-ef06-4c72-9eb5-464be4e4de9f.png)


### Challenges & wins

#### Wins

A big win for me was working on my own and pushing myself to be patient with myself and my abilities when it comes to front-end engineering. It was my first time figuiring things out on my own and I found that it was the first time I had pushed myself to overcome some of my imposter syndrome and working independently. 
Another win was realising how much I have a passion for design/styling and seeing my vision come to life, throughout my SEI course I have felt connected to styling and this final project really helped me see how much my skills have grown and how my passion for design has flourished and has inspired me to maybe take my design skills further.

#### Challenges 

The biggest techical challenge of this project was connecting the Username with the Submitted_by fields in my two models. It was possible to get the User ID however fetching the username was a challenge and I ended up not being able to implement this feature although I spent a lot of time researching and speaking to tutors about it. Another challenge was not knowing/having a gauge of how I was doing in the 2 weeks, and having to deal with the anxiety of the unknown and not having peers to discuss it with to ease the anxiety, however, in the end, this turned out to be okay as I was happy with where I was with my project and how far I got.

 
### Future improvements or changes

Features to implement: 

- Display author (logged in user who created the article) bio/picture/username
- Have a categories page, which will have links to the different categories, which will then show a list of articles with the relevant category (this was originally intended as a stretch goal)
- Add more data into the backend to display on the website
- Deployment
  

