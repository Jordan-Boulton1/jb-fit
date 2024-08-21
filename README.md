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

![screenshot](documentation/responsive-mockup.png)

source: [amiresponsive](https://ui.dev/amiresponsive?url=https://ci-jb-fit-73ac55dce174.herokuapp.com/)

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

## Features

### Existing Features

#### Navigation Bar

- **Responsive Navigation Bar**

    - The site includes a fully responsive navigation bar that adapts to different screen sizes. On mobile devices, the navigation bar collapses into a toggleable menu, enhancing usability for users on the go. The navigation bar provides easy access to essential pages such as Home, About, Plans, FAQ, and Community, ensuring users can quickly navigate the site. For logged-in users, additional options like 'My Profile' and 'Logout' are available, making it easy to manage their account.

![screenshot](documentation/features/feat-responsive-nav1.png)
![screenshot](documentation/features/feat-responsive-nav2.png)

- **Custom Logo**

    - The website features a custom logo prominently displayed in the navigation bar, reinforcing brand identity. This visual element helps establish trust and recognition, as users can immediately identify the JB Fit brand. The logo is linked to the homepage, allowing users to return to the main page with a single click.

![screenshot](documentation/features/feat-logo.png)

- **Authentication Links**

    - Depending on the user's authentication status, the navigation bar dynamically displays relevant options. For unauthenticated users, 'Login' and 'Register' links are provided, encouraging new sign-ups and making it easy for returning users to log in. Authenticated users are presented with 'My Profile' and 'Logout' options, enabling seamless account management.

![screenshot](documentation/features/feat-unauthenticated-user.png)
![screenshot](documentation/features/feat-authenticated-user.png)

### Footer

- **Social Media Links**

    - The footer includes prominent social media links, allowing users to connect with JB Fit across multiple platforms like Facebook, Instagram, Twitter, LinkedIn, and YouTube. This integration helps build a community around the brand and keeps users engaged with the latest updates and content from JB Fit.

![screenshot](documentation/features/feat-social-links.png)

- **Newsletter Subscription Form**

	- The footer also includes a newsletter subscription form, which is a valuable tool for maintaining communication with users. By subscribing, users receive monthly updates on fitness trends, promotions, and news. This feature is crucial for user retention and driving ongoing engagement.

![screenshot](documentation/features/feat-newsletter.png)

- **Quick Links Section**

	- A quick links section in the footer provides easy access to the most important pages on the site. This section is especially useful for users who may need to quickly navigate to another part of the site without returning to the top of the page.

![screenshot](documentation/features/feat-quick-links.png)

- **Custom Footer Branding**

	- The footer is customized to include JB Fit’s branding, including a copyright notice and branding colors. This consistent branding across the site enhances the professional appearance and reinforces the site’s identity.

![screenshot](documentation/features/feat-footer.png)

### Home Page

- **Hero**

    - The hero section is the first thing users see when they visit the website. It features a strong, compelling headline and a call-to-action button that encourages users to start their fitness journey. This section is visually impactful, with a background image that sets the tone for the site, and a clear value proposition that appeals to users looking for personal online fitness coaching.

![screenshot](documentation/features/home/feat-home-hero.png)

- **About**

    - The About section introduces the site's founder, Jordan, providing credibility and a personal connection with visitors. It explains Jordan's experience and qualifications, which helps to build trust with potential clients. The section is accompanied by a professional image, further enhancing the personal connection with visitors.

![screenshot](documentation/features/home/feat-home-about.png)

- **Online Personal Training**

    - This section explains what online personal training is and outlines its benefits, such as flexibility, personalization, accessibility, and affordability. It also includes visually appealing icons that represent each benefit, making it easy for users to understand the advantages of online training at a glance. This section is crucial for educating visitors about the unique value proposition of online training.

![screenshot](documentation/features/home/feat-home-online-pt.png)

- **How It Works**

    - The "How It Works" section breaks down the process of getting started with JB Fit into four easy steps: Initial Consultation, Personalized Plan, Ongoing Support, and Community Interaction. Each step is visually represented with an icon and a brief description, helping users understand what to expect when they sign up. This transparency is key to converting visitors into clients.

![screenshot](documentation/features/home/feat-home-how-it-works.png)

- **Client Reviews**

    - The Client Reviews section features testimonials from satisfied clients, which are essential for building social proof. Each review is accompanied by a star rating and a photo of the client, making the testimonials more relatable and trustworthy. This section helps reassure potential clients of the quality and effectiveness of JB Fit’s services.

![screenshot](documentation/features/home/feat-home-client-review.png)

- **Training Plans**

    - The Training Plans section presents the different packages available, each with a clear breakdown of what’s included and the associated cost. This section is designed to help users easily compare the options and choose the one that best fits their needs. The use of distinct cards for each plan, along with prominent pricing, makes this information easy to digest.

![screenshot](documentation/features/home/feat-home-training-plans.png)

- **Contact Form**

    - The Contact Form section invites users to get in touch for more information or inquiries, with a prompt to check the FAQ for common questions. This section is designed to facilitate easy communication between potential clients and JB Fit, enhancing the user experience by providing a straightforward way to ask questions or start the sign-up process.

![screenshot](documentation/features/home/feat-home-contact-form.png)

### About Page

- **Inspirational quote - Hero**

    - The About page opens with a powerful and inspirational quote, which sets a motivational tone for visitors. This section uses a full-width, centred layout with a bold, white font against a hero image, making the quote stand out. The quote encapsulates the philosophy of perseverance and determination, resonating with the core values of the JB Fit coaching program.

![screenshot](documentation/features/about/feat-about-hero.png)

- **Biography**

    - The Coach Biography section provides a detailed overview of the coach's background, including academic qualifications, certifications, and professional experience. This section builds credibility and trust by highlighting the coach’s expertise and the personalized approach they bring to their training. The biography is divided into text and bullet points, making it easy for users to digest the information and understand the coach’s qualifications and commitment to continuous learning.

![screenshot](documentation/features/about/feat-about-biography.png)

- **Mission and Vision**

    - The Mission and Vision section clearly outlines the purpose and goals of JB Fit. The mission statement emphasizes the commitment to empowering individuals through personalized coaching and supportive community engagement. The vision statement reflects the long-term goals of making professional fitness coaching accessible to all and fostering a culture of health and wellness. This section is essential for communicating the core values and long-term aspirations of the brand to potential clients.

![screenshot](documentation/features/about/feat-about-mission-vision.png)

- **Personal Fitness Philosophy**

    - The Personal Fitness Philosophy section is a key feature that showcases the coach's unique approach to fitness. It emphasizes a holistic and sustainable approach to health and wellness, focusing not only on physical strength but also on mental resilience and overall well-being. The section is visually divided into individual cards, each highlighting a different aspect of the coach’s philosophy, such as Individualized Approach, Sustainable Practices, Holistic Health, Continuous Learning, and Community Support. This layout makes the philosophy accessible and relatable to users, encouraging them to connect with the values of JB Fit.

![screenshot](documentation/features/about/feat-about-philosophy.png)

### Plans Page

- **Training Plans**

    - The Training Plans section offers users a detailed overview of the different fitness packages available at JB Fit. Each plan is presented in a clean, card-based layout, making it easy for users to compare options and select the one that best suits their needs. The plans include various levels of support and customization, from a one-time plan to the comprehensive Elite Coaching package. This section is essential for helping users make informed decisions about their fitness journey and provides clear pricing for each option.

![screenshot](documentation/features/plans/feat-plans-training.png)

- **Why Choose My Plans?**

    - This section highlights the key advantages of choosing JB Fit’s training plans, such as Expertise, Customization, Support, and Results. Each benefit is visually represented with an icon and a brief description, reinforcing the value of the services offered. This section is designed to build trust and confidence in potential clients by emphasizing the quality and effectiveness of the plans.

![screenshot](documentation/features/plans/feat-plans-why-choose.png)

### FAQ Page

- **FAQ Section**

    - The FAQ section is designed with an accordion layout, which organizes frequently asked questions into expandable panels. This structure makes it easy for users to find answers to their specific questions without having to scroll through long blocks of text. The accordion is divided into multiple categories such as General Questions, Services & Packages, Pricing & Payments, Personalized Plans, Support & Community, and Getting Started. Each category addresses key areas of interest for potential and current clients, providing detailed and helpful information to guide them through their fitness journey with JB Fit.

![screenshot](documentation/features/faq/feat-faq-accordian-open.png)
![screenshot](documentation/features/faq/feat-faq-accordian-closed.png)

- **General Questions**

    - This section addresses broad, introductory questions about JB Fit, such as what the platform is and how online personal training works. It helps new visitors quickly understand the core services offered and the benefits of choosing JB Fit for their fitness needs.

![screenshot](documentation/features/faq/feat-faq-accordian-open.png)

- **Services & Packages**

    - The Services & Packages section provides detailed information about the various services available and helps users decide which package is right for them. This section is crucial for helping potential clients understand the offerings and make an informed decision about which plan best suits their fitness goals.

![screenshot](documentation/features/faq/feat-faq-services.png)

- **Pricing & Payments**

    - This section covers important information about payment methods, discounts, and cancellation policies. It ensures that users are fully informed about the financial aspects of signing up for JB Fit services, providing transparency and building trust with potential clients.

![screenshot](documentation/features/faq/feat-faq-pricing.png)

- **Personalized Plans**

    - The Personalized Plans section explains how JB Fit customizes workout and nutrition plans based on each client's unique needs and preferences. It highlights the flexibility and personalized attention clients receive, which are key selling points for JB Fit's services.

![screenshot](documentation/features/faq/feat-faq-personalized-plans.png)

- **Support & Community**

    - This section outlines the various levels of support available to clients, including check-ins, email and chat support, video consultations, and access to a supportive community. It emphasizes the ongoing support that clients receive, which is essential for maintaining motivation and achieving long-term success.

![screenshot](documentation/features/faq/feat-faq-support-community.png)

- **Getting Started**

    - The Getting Started section provides a step-by-step guide for new clients on how to begin their journey with JB Fit. It covers the initial consultation process and the information required to create a personalized plan. This section is designed to make onboarding new clients as smooth and straightforward as possible.

![screenshot](documentation/features/faq/feat-faq-getting-started.png)

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

## Ecommerce Business Model


This site sells goods directly to individual customers, following a **Business to Customer (B2C)** model. In addition to individual transactions, it also offers subscription options, allowing customers to receive products or services on a regular basis, such as monthly or annually.

The business is still in its early development stages but already features a newsletter and social media marketing links. Social media, particularly on larger platforms like Facebook, can play a crucial role in building a community around the business, increasing site traffic, and fostering customer loyalty.

The newsletter list is a valuable tool for the business to engage with its customers. It can be used to send regular updates about special offers, new products, changes in business hours, event notifications, and more, ensuring that subscribers stay informed and connected.

### Sitemap

I've used [XML-Sitemaps](https://www.xml-sitemaps.com) to generate a sitemap.xml file.
This was generated using my deployed site URL: https://ci-jb-fit-73ac55dce174.herokuapp.com/

After it finished crawling the entire site, it created a
[sitemap.xml](sitemap.xml) which I've downloaded and included in the repository.

### Robots

I've created the [robots.txt](robots.txt) file at the root-level.
Inside, I've included the default settings:

```
User-agent: *
Disallow:
Sitemap: https://jb-ci-boutique-ado-0fd50c244260.herokuapp.com/sitemap.xml
```

Further links for future implementation:
- [Google search console](https://search.google.com/search-console)
- [Creating and submitting a sitemap](https://developers.google.com/search/docs/advanced/sitemaps/build-sitemap)
- [Managing your sitemaps and using sitemaps reports](https://support.google.com/webmasters/answer/7451001)
- [Testing the robots.txt file](https://support.google.com/webmasters/answer/6062598)

### Social Media Marketing

Creating a strong social base (with participation) and linking that to the business site can help drive sales.
Using more popular providers with a wider user base, such as Facebook, typically maximizes site views.

I've created a mockup Facebook business account.

![screenshot](documentation/mockup-facebook1.png)
![screenshot](documentation/mockup-facebook2.png)

### Newsletter Marketing

I have incorporate a newsletter sign-up form on my application, to allow users to supply their
email address if they are interested in learning more.

![screenshot](documentation/newsletter.png)

## Testing

> [!NOTE]  
> For all testing, please refer to the [TESTING.md](TESTING.md) file.

## Deployment

The live deployed application can be found deployed on [Heroku](https://ci-jb-fit-73ac55dce174.herokuapp.com/).

### PostgreSQL Database

This project uses a [Code Institute PostgreSQL Database](https://dbs.ci-dbs.net).

To obtain my own Postgres Database from Code Institute, I followed these steps:

- Signed-in to the CI LMS using my email address.
- An email was sent to me with my new Postgres Database.

> [!CAUTION]  
> - PostgreSQL databases by Code Institute are only available to CI Students.
> - You must acquire your own PostgreSQL database through some other method
> if you plan to clone/fork this repository.
> - Code Institute students are allowed a maximum of 8 databases.
> - Databases are subject to deletion after 18 months.

### Amazon AWS

This project uses [AWS](https://aws.amazon.com) to store media and static files online, due to the fact that Heroku doesn't persist this type of data.

Once you've created an AWS account and logged-in, follow these series of steps to get your project connected.
Make sure you're on the **AWS Management Console** page.

#### S3 Bucket

- Search for **S3**.
- Create a new bucket, give it a name (matching your Heroku app name), and choose the region closest to you.
- Uncheck **Block all public access**, and acknowledge that the bucket will be public (required for it to work on Heroku).
- From **Object Ownership**, make sure to have **ACLs enabled**, and **Bucket owner preferred** selected.
- From the **Properties** tab, turn on static website hosting, and type `index.html` and `error.html` in their respective fields, then click **Save**.
- From the **Permissions** tab, paste in the following CORS configuration:

	```shell
	[
		{
			"AllowedHeaders": [
				"Authorization"
			],
			"AllowedMethods": [
				"GET"
			],
			"AllowedOrigins": [
				"*"
			],
			"ExposeHeaders": []
		}
	]
	```

- Copy your **ARN** string.
- From the **Bucket Policy** tab, select the **Policy Generator** link, and use the following steps:
	- Policy Type: **S3 Bucket Policy**
	- Effect: **Allow**
	- Principal: `*`
	- Actions: **GetObject**
	- Amazon Resource Name (ARN): **paste-your-ARN-here**
	- Click **Add Statement**
	- Click **Generate Policy**
	- Copy the entire Policy, and paste it into the **Bucket Policy Editor**

		```shell
		{
			"Id": "Policy1234567890",
			"Version": "2012-10-17",
			"Statement": [
				{
					"Sid": "Stmt1234567890",
					"Action": [
						"s3:GetObject"
					],
					"Effect": "Allow",
					"Resource": "arn:aws:s3:::your-bucket-name/*"
					"Principal": "*",
				}
			]
		}
		```

	- Before you click "Save", add `/*` to the end of the Resource key in the Bucket Policy Editor (like above).
	- Click **Save**.
- From the **Access Control List (ACL)** section, click "Edit" and enable **List** for **Everyone (public access)**, and accept the warning box.
	- If the edit button is disabled, you need to change the **Object Ownership** section above to **ACLs enabled** (mentioned above).

#### IAM

Back on the AWS Services Menu, search for and open **IAM** (Identity and Access Management).
Once on the IAM page, follow these steps:

- From **User Groups**, click **Create New Group**.
	- Suggested Name: `group-peak-performance` (group + the project name)
- Tags are optional, but you must click it to get to the **review policy** page.
- From **User Groups**, select your newly created group, and go to the **Permissions** tab.
- Open the **Add Permissions** dropdown, and click **Attach Policies**.
- Select the policy, then click **Add Permissions** at the bottom when finished.
- From the **JSON** tab, select the **Import Managed Policy** link.
	- Search for **S3**, select the `AmazonS3FullAccess` policy, and then **Import**.
	- You'll need your ARN from the S3 Bucket copied again, which is pasted into "Resources" key on the Policy.

		```shell
		{
			"Version": "2012-10-17",
			"Statement": [
				{
					"Effect": "Allow",
					"Action": "s3:*",
					"Resource": [
						"arn:aws:s3:::your-bucket-name",
						"arn:aws:s3:::your-bucket-name/*"
					]
				}
			]
		}
		```
	
	- Click **Review Policy**.
	- Suggested Name: `policy-peak-performance` (policy + the project name)
	- Provide a description:
		- "Access to S3 Bucket for peak-performance static files."
	- Click **Create Policy**.
- From **User Groups**, click your "group-peak-performance".
- Click **Attach Policy**.
- Search for the policy you've just created ("policy-peak-performance") and select it, then **Attach Policy**.
- From **User Groups**, click **Add User**.
	- Suggested Name: `user-peak-performance` (user + the project name)
- For "Select AWS Access Type", select **Programmatic Access**.
- Select the group to add your new user to: `group-peak-performance`
- Tags are optional, but you must click it to get to the **review user** page.
- Click **Create User** once done.
- You should see a button to **Download .csv**, so click it to save a copy on your system.
	- **IMPORTANT**: once you pass this page, you cannot come back to download it again, so do it immediately!
	- This contains the user's **Access key ID** and **Secret access key**.
	- `AWS_ACCESS_KEY_ID` = **Access key ID**
	- `AWS_SECRET_ACCESS_KEY` = **Secret access key**

#### Final AWS Setup

- If Heroku Config Vars has `DISABLE_COLLECTSTATIC` still, this can be removed now, so that AWS will handle the static files.
- Back within **S3**, create a new folder called: `media`.
- Select any existing media images for your project to prepare them for being uploaded into the new folder.
- Under **Manage Public Permissions**, select **Grant public read access to this object(s)**.
- No further settings are required, so click **Upload**.

### Stripe API

This project uses [Stripe](https://stripe.com) to handle the ecommerce payments.

Once you've created a Stripe account and logged-in, follow these series of steps to get your project connected.

- From your Stripe dashboard, click to expand the "Get your test API keys".
- You'll have two keys here:
	- `STRIPE_PUBLIC_KEY` = Publishable Key (starts with **pk**)
	- `STRIPE_SECRET_KEY` = Secret Key (starts with **sk**)

As a backup, in case users prematurely close the purchase-order page during payment, we can include Stripe Webhooks.

- From your Stripe dashboard, click **Developers**, and select **Webhooks**.
- From there, click **Add Endpoint**.
	- `https://jb-ci-boutique-ado-0fd50c244260.herokuapp.com/checkout/wh/`
- Click **receive all events**.
- Click **Add Endpoint** to complete the process.
- You'll have a new key here:
	- `STRIPE_WH_SECRET` = Signing Secret (Wehbook) Key (starts with **wh**)

### Gmail API

This project uses [Gmail](https://mail.google.com) to handle sending emails to users for account verification and purchase order confirmations.

Once you've created a Gmail (Google) account and logged-in, follow these series of steps to get your project connected.

- Click on the **Account Settings** (cog icon) in the top-right corner of Gmail.
- Click on the **Accounts and Import** tab.
- Within the section called "Change account settings", click on the link for **Other Google Account settings**.
- From this new page, select **Security** on the left.
- Select **2-Step Verification** to turn it on. (verify your password and account)
- Once verified, select **Turn On** for 2FA.
- Navigate back to the **Security** page, and you'll see a new option called **App passwords**.
- This might prompt you once again to confirm your password and account.
- Select **Mail** for the app type.
- Select **Other (Custom name)** for the device type.
	- Any custom name, such as "Django" or peak-performance
- You'll be provided with a 16-character password (API key).
	- Save this somewhere locally, as you cannot access this key again later!
	- `EMAIL_HOST_PASS` = user's 16-character API key
	- `EMAIL_HOST_USER` = user's own personal Gmail email address