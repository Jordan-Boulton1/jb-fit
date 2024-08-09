# [JB Fit](https://ci-jb-fit-73ac55dce174.herokuapp.com/)

[![GitHub commit activity](https://img.shields.io/github/commit-activity/t/Jordan-Boulton1/peak-performance)](https://github.com/Jordan-Boulton1/peak-performance/commits/main)
[![GitHub last commit](https://img.shields.io/github/last-commit/Jordan-Boulton1/peak-performance)](https://github.com/Jordan-Boulton1/peak-performance/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/Jordan-Boulton1/peak-performance)](https://github.com/Jordan-Boulton1/peak-performance)

Welcome to JB Fit, your ultimate online personal fitness coaching app. JB-Fit is designed to revolutionize the way you approach fitness by providing personalized coaching, comprehensive exercise plans, and a supportive community all in one platform. Whether you're a fitness novice or a seasoned athlete, JB-Fit is here to help you achieve your fitness goals and unlock your peak performance.

### What can you expect?

JB Fit aims to create a centralized and seamless fitness experience that combines expert coaching, tailored exercise & nutrition plans, and a vibrant community. My goal is to make high-quality fitness coaching accessible and affordable to everyone.

### Who do I target?

JB Fit is designed for:

- **Fitness enthusiasts**: Individuals who are passionate about fitness and are looking for structured exercise plans and professional guidance to enhance their workout routines.
- **Beginners**: Those who are new to fitness and need a supportive environment, clear guidance, and easy-to-follow plans to start their journey.
- **Busy Professionals**: People with a hectic schedule who require flexible, personalized coaching that fits into their lifestyle.
- **Fitness Coaches**: Professional coaches who want to reach a wider audience and provide their services through an innovative online platform.

### What benefits do you get?

- **Personalized Coaching**: Receive one-on-one coaching from a fitness expert, tailored to your specific goals and needs. 
- **Personal Check-Ins**: Benefit from regular personal check-ins to ensure you're on track with your fitness goals and receive the support you need to succeed.
- **Custom Exercise Plans**: Get exercise plans specifically designed for you  by a fitness professional. These personalized plans take into account your current fitness level, goals, and preferences, ensuring maximum effectiveness and safety.
- **Tailored Nutrition Plans**: Access personalized nutrition plans that complements your fitness goals. These plans are crafted to meet you dietary preferences and nutritional needs, helping you achieve optimal results.
- **Community Support**: Join a thriving community of like-minded individuals who share your passion for fitness. Engage in forums, share your progress, and support each other.
- **Convenient Payments**: With integrated Stripe payments, purchasing exercise plans and booking coaching sessions is secure and hassle-free.
- **Progress Tracking**: Keep track of your fitness journey with tools to monitor your progress, set new goals, and celebrate your achievements.

JB Fit is more than just a fitness application—it's your partner in achieving a healthier, stronger, and more empowered version of yourself. Take the step towards reaching your peak performance with JB Fit.

![screenshot](documentation/mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://jb-ci-boutique-ado-0fd50c244260.herokuapp.com)

## UX


When designing this webpage I wanted to achieve a simple, yet welcoming and professional feeling, creating a nice user experience.

### Colour Scheme

The colour scheme for the JB Fit website has been thoughtfully selected to create a visually appealing and effective user experience.

- `#FFFFFF` & `#000000` used interchangeably for primary text and headings.
- `#FF5100` used for primary highlights.
- `#f5f5f5` used as the  primary background colour.
- `#353431` used as the secondary background colour, primarily in the navbar and footer.

I used [coolors.co](https://coolors.co/ffffff-f5f5f5-ff5100-353431-000000) to generate my colour palette.

![screenshot](documentation/coolors.png)

I've used CSS `:root` variables to easily update the global colour scheme by changing only one value, instead of everywhere in the CSS file.

```css
:root {
--primary-color: #353431;
--primary-color-highlight: #FF5100;
/* Bootstrap overrides */
--bs-body-bg: #f5f5f5;
--bs-body-font-family: 'Cambay', sans-serif;
```

### Typography

- [Montserrat](https://fonts.google.com/specimen/Montserrat) was used for the primary headers and titles.

- [Mukta](https://fonts.google.com/specimen/Mukta) was used for the secondary headers and titles.

- [Cambay](https://fonts.google.com/specimen/Cambay) was used for all other secondary text.

- [Font Awesome](https://fontawesome.com) icons were used throughout the site, such as the social media icons in the footer.

## User Stories

### New Site Users

- As a **new user**, I want to **register and create an account**, so that I can **access personalized fitness and nutrition plans.**
- As a **new user**, I want to **read success stories and testimonials** so that **I can trust the effectiveness of the coaching services.**
- As a **new user**, I want to **be able to message the coach with any queries I have before purchasing a plan**, so that I **can make an informed decision.**

### Registered Site Users

- As a **registered user**, I want to **manage and update my profile information**, so that my **fitness and nutrition plans remain accurate and relevant.**
- As a **registered user**, I want to **securely pay for my selected training package using Stripe**, so that I can **access my plans and coaching services.**
- As a **registered user**, I want to **have regular check-ins and track my progress**, so that **I stay motivated and on track with my fitness goals.**
- As a **registered user**, I want to **access community forums** so that **I can engage with other users and share my experiences.**
- As a **registered user**, I want to **book video consultations with my coach** so that I can **receive personalized guidance and feedback.**
- As a **registered user** that has bought the elite plan, I want access to **exclusive fitness and nutrition workshops** so that I can **deepen my knowledge and skills.**
- As a **registered user**, I want to **understand the cancellation and refund policy** so that I **know what to expect if I need to stop my subscription.**
- As a **registered user**, I want to **contact my coach for support** so that I **can get help when I need it.**

### Site Admin

- As an **admin**, I want to **create, manage and update subscription plans** so that **users can see the up-to-date plans and services at the current time**
- As an **admin**, I want to **view and manage payments** so that **I can keep track of subscription fees and payment statuses.**
- As an **admin**, I want to **manage community content** so that **the forum remains a positive and supportive environment.**
- As an **admin**, I want to **integrate Stripe for handling payments** so that **users can subscribe to plans and make payments securely.**

## Mock-ups

To follow best practice, mockups were developed for this project.
I've used [Figma](https://www.figma.com) to design my site mockups.

### Home Page Mock-ups

<details>
<summary> Click here to see the Home Page Mock-ups</summary>

#### Home
  - ![screenshot](documentation/wireframes/home/home-mockup1.png)

  - ![screenshot](documentation/wireframes/home/home-mockup2.png)

  - ![screenshot](documentation/wireframes/home/home-mockup3.png)

  - ![screenshot](documentation/wireframes/home/home-mockup4.png)

  - ![screenshot](documentation/wireframes/home/home-mockup5.png)

  - ![screenshot](documentation/wireframes/home/home-mockup6.png)

</details>

### About Page Mock-ups

<details>
<summary> Click here to see the About Page Mock-ups</summary>

#### About
  - ![screenshot](documentation/wireframes/about/about-mockup1.png)
  
  - ![screenshot](documentation/wireframes/about/about-mockup2.png)

  - ![screenshot](documentation/wireframes/about/about-mockup3.png)

  - ![screenshot](documentation/wireframes/about/about-mockup4.png)

  - ![screenshot](documentation/wireframes/about/about-mockup5.png)

</details>

### Plans Page Mock-ups

<details>
<summary> Click here to see the Plans Page Mock-ups</summary>

#### Plans
  - ![screenshot](documentation/wireframes/plans/plan-mockup1.png)

  - ![screenshot](documentation/wireframes/plans/plan-mockup2.png)

  - ![screenshot](documentation/wireframes/plans/plan-mockup3.png)

</details>

### FAQ Page Mock-ups

<details>
<summary> Click here to see the FAQ Page Mock-ups</summary>

#### FAQ
  - ![screenshot](documentation/wireframes/faq/faq-mockup1.png)

  - ![screenshot](documentation/wireframes/faq/faq-mockup2.png)

</details>

### Testimonials Page Mock-ups

<details>
<summary> Click here to see the Testimonials Page Mock-ups</summary>

#### Testimonials
  - ![screenshot](documentation/wireframes/testimonials/testimonial-mockup1.png)

  - ![screenshot](documentation/wireframes/testimonials/testimonial-mockup2.png)

  - ![screenshot](documentation/wireframes/testimonials/testimonial-mockup3.png)

  - ![screenshot](documentation/wireframes/testimonials/testimonial-mockup4.png)

  - ![screenshot](documentation/wireframes/testimonials/testimonial-mockup5.png)

</details>

## Tools & Technologies Used

- [![Markdown Builder](https://img.shields.io/badge/Markdown_Builder-grey?logo=markdown&logoColor=000000)](https://tim.2bn.dev/markdown-builder) used to generate README and TESTING templates.
- [![Git](https://img.shields.io/badge/Git-grey?logo=git&logoColor=F05032)](https://git-scm.com) used for version control. (`git add`, `git commit`, `git push`)
- [![GitHub](https://img.shields.io/badge/GitHub-grey?logo=github&logoColor=181717)](https://github.com) used for secure online code storage.
- [![VSCode](https://img.shields.io/badge/VSCode-grey?logo=visualstudiocode&logoColor=007ACC)](https://code.visualstudio.com) used as my local IDE for development.
- [![HTML](https://img.shields.io/badge/HTML-grey?logo=html5&logoColor=E34F26)](https://en.wikipedia.org/wiki/HTML) used for the main site content.
- [![CSS](https://img.shields.io/badge/CSS-grey?logo=css3&logoColor=1572B6)](https://en.wikipedia.org/wiki/CSS) used for the main site design and layout.
- [![JavaScript](https://img.shields.io/badge/JavaScript-grey?logo=javascript&logoColor=F7DF1E)](https://www.javascript.com) used for user interaction on the site.
- [![jQuery](https://img.shields.io/badge/jQuery-grey?logo=jquery&logoColor=0769AD)](https://jquery.com) used for user interaction on the site.
- [![Python](https://img.shields.io/badge/Python-grey?logo=python&logoColor=3776AB)](https://www.python.org) used as the back-end programming language.
- [![Heroku](https://img.shields.io/badge/Heroku-grey?logo=heroku&logoColor=430098)](https://www.heroku.com) used for hosting the deployed back-end site.
- [![Bootstrap](https://img.shields.io/badge/Bootstrap-grey?logo=bootstrap&logoColor=7952B3)](https://getbootstrap.com) used as the front-end CSS framework for modern responsiveness and pre-built components.
- [![Jest](https://img.shields.io/badge/Jest-grey?logo=jest&logoColor=c21325)](https://jestjs.io) used for automated JavaScript testing.
- [![Django](https://img.shields.io/badge/Django-grey?logo=django&logoColor=092E20)](https://www.djangoproject.com) used as the Python framework for the site.
- [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-grey?logo=postgresql&logoColor=4169E1)](https://www.postgresql.org) used as the relational database management.
- [![PostgreSQL by Code Institute](https://img.shields.io/badge/PostgreSQL_by_Code_Institute-grey?logo=okta&logoColor=F05223)](https://dbs.ci-dbs.net) used as the Postgres database from Code Institute.
- [![ElephantSQL](https://img.shields.io/badge/ElephantSQL-grey?logo=postgresql&logoColor=36A6E2)](https://www.elephantsql.com) used as the Postgres database.
- [![WhiteNoise](https://img.shields.io/badge/WhiteNoise-grey?logo=python&logoColor=FFFFFF)](https://whitenoise.readthedocs.io) used for serving static files with Heroku.
- [![Stripe](https://img.shields.io/badge/Stripe-grey?logo=stripe&logoColor=008CDD)](https://stripe.com) used for online secure payments of ecommerce products/services.
- [![Gmail API](https://img.shields.io/badge/Gmail_API-grey?logo=gmail&logoColor=EA4335)](https://mail.google.com) used for sending emails in my application.
- [![AWS S3](https://img.shields.io/badge/AWS_S3-grey?logo=amazons3&logoColor=569A31)](https://aws.amazon.com/s3) used for online static file storage.
- [![Figma](https://img.shields.io/badge/Figma-grey?logo=figma&logoColor=F24E1E)](https://www.figma.com) used for creating wireframes.
- [![Font Awesome](https://img.shields.io/badge/Font_Awesome-grey?logo=fontawesome&logoColor=528DD7)](https://fontawesome.com) used for the icons.
- [![ChatGPT](https://img.shields.io/badge/ChatGPT-grey?logo=chromatic&logoColor=75A99C)](https://chat.openai.com) used to help debug, troubleshoot, and explain things.
- [![Mermaid](https://img.shields.io/badge/Mermaid-grey?logo=mermaid&logoColor=FF3670)](https://www.mermaidchart.com/) used for creating ERD diagrams.
- [![Djecrety](https://img.shields.io/badge/Djecrety-grey?logo=google-chrome&logoColor=e3e324)](https://djecrety.ir/) used for generating django secret keys.
- [![StackEdit](https://img.shields.io/badge/StackEdit-grey?logo=stackedit&logoColor=white)](https://www.stackedit.io) used as an in-browser markdown editor.
- [![Logo](https://img.shields.io/badge/Logo-grey?logo=google-chrome&logoColor=24aae3)](https://logo.com/) used to create the logo for the website.
- [![ImageResizer](https://img.shields.io/badge/ImageResizer-grey?logo=google-chrome&logoColor=24e341)](https://imageresizer.com/) used compress and resize images.

## Database Design

Entity Relationship Diagrams (ERD) help to visualize database architecture before creating models.
Understanding the relationships between different tables can save time later in the project.

```mermaid
erDiagram
User ||--o{ TrainingPlan : fk_User_TrainingPlan
User ||--|{ Checkout : fk_User_Checkout
User ||--o{ WeightLog : fk_User_WeightLog
User ||--o{ ProgressImage : fk_User_ProgressImage
TrainingPlan ||--|{ Checkout : fk_TrainingPlan_Checkout


User {
  int id  PK
  varchar(50) first_name
  varchar(50) last_name
  varchar(255) email
  varchar(100) password
  varchar(30) phone_number
  varchar(100) address
  varchar(255) image
  int gender
  datetime date_of_birth
  decimal current_weight
  decimal height
  decimal goal_weight
  int training_plan_id  FK  "NULL"
}

TrainingPlan {
  int id  PK
  varchar(150) title
  text description
  decimal price
}

WeightLog {
  int id  PK
  int user_id  FK
  decimal weight
  datetime entry_date
}

ProgressImage {
  int id  PK
  int user_id  FK
  varchar(255) image
  dateTime entry_date
}

Checkout {
  int id  PK
  int user_id  FK
  int training_plan_id  FK
  decimal total
}

Newsletter {
  varchar(255) email
}

Contact {
  varchar(50) first_name
  varchar(50) last_name
  varchar(255) email
  text message
}
```

I have used [mermaidchart](https://www.mermaidchart.com/) to generate an ERD.

## Agile Development Process

### GitHub Projects

[GitHub Projects](https://github.com/Jordan-Boulton1/jb-fit/projects?query=is%3Aopen) served as an Agile tool for this project.
It isn't a specialized tool, but with the right tags and project creation/issue assignments, it can be made to work.

Through it, user stories, issues, and milestone tasks were planned, then tracked on a weekly basis using the basic Kanban board.

![screenshot](documentation/projects-board.png)

### GitHub Issues

[GitHub Issues](https://github.com/Jordan-Boulton1/peak-performance/issues) served as an another Agile tool.
There, I used my own **User Story Template** to manage user stories.

It also helped with milestone iterations on a weekly basis.

- [Open Issues](https://github.com/Jordan-Boulton1/peak-performance/issues) [![GitHub issues](https://img.shields.io/github/issues/Jordan-Boulton1/peak-performance)](https://github.com/Jordan-Boulton1/peak-performance/issues)

    ![screenshot](documentation/gh-open-issues.png)

- [Closed Issues](https://github.com/Jordan-Boulton1/peak-performance/issues?q=is%3Aissue+is%3Aclosed) [![GitHub closed issues](https://img.shields.io/github/issues-closed/Jordan-Boulton1/peak-performance)](https://github.com/Jordan-Boulton1/peak-performance/issues?q=is%3Aissue+is%3Aclosed)

    ![screenshot](documentation/gh-closed-issues.png)

### MoSCoW Prioritization

I've decomposed my Epics into stories prior to prioritizing and implementing them.
Using this approach, I was able to apply the MoSCow prioritization and labels to my user stories within the Issues tab.

- **Must Have**: guaranteed to be delivered (*max 60% of stories*)
- **Should Have**: adds significant value, but not vital (*the rest ~20% of stories*)
- **Could Have**: has small impact if left out (*20% of stories*)
- **Won't Have**: not a priority for this iteration

### Milestones

To achieve success in the implementation of this project, I have setup milestones for the end of each week, which represented my "sprints". My approach to solving the business problem in the domain area was to do vertical slicing of the system, instead of horizontal - an approach that I have used so far in my projects. Vertical slicing focuses on ensuring that at the end of each sprint you are able to produce something in the system that is deployable, worthy of a "demo", and that is useable by the client.

![screenshot](documentation/gh-milestones.png)