# cs216-project-proposal

## Introduction

  In the 2010s, counter-culture groups, those who distinguish themselves from dominant discourse, continued to thrive on the Chinese Internet. Counter-culture groups ,as one type of cultural group, is defined as “a set of publicly shared codes or repertoires, building blocks that structure people's ability to think and to share ideas” (Eliasoph and Lichterman), in other words, a group of shared norms. In sociology studies, any counter-cultural group would have “group boundaries” as the group’s relationships, imagined and real, to other counter-cultural groups (Eliasoph and Lichterman). There also exists a hierarchy among them where a cultural group might be a subset of a bigger group. While the dominant discourse in China is largely controlled by CCP propaganda, counter-culture groups can ensure more freedom of wills and speech for group members, thus being a critical angle to reveal the true opinions of Chinese people.

  The video website Bilibili, now known as the YouTube of China, has long been serving as the land of intersection of those counter-culture groups since its establishment. Different cultural groups would upload their fandom videos which contain information about the corresponding counter-culture groups. We want to explore the establishment, development of counter-cultural groups in China and how they interact with other groups from the data. Specifically, our research questions will be:

### Substantial:

- How to collect, filter and store the data about counter-culture groups on Bilibili at an appropriate cost of time and space?

### Feasible:

- What patterns exist among the data in a video that can be a key identifier to certain counter-culture groups? And how to define and quantify the relationship of two culture groups by the data?
- How to derive the hierarchy of all culture groups from the defined relationship? 
- What is the dynamics of interactions between different countercultural groups with the development of time?

### Relevant:

- What can we observe about establishment, evolvement of counter-culture groups from these relations?

After thorough discussions, we propose the following justification for our research questions:

### Substantial:

- Data scraping work is very critical in our project. Due to the limitation of Bilibili, no online open-source database was allowed to store their data, in which case we have to scrape data in 9999998 videos ourselves. Storing, accessing and playing with the retrieved data in an efficient way also presents challenges to us.

### Feasible:

- Each video includes abundant information about a trait of certain counterculture groups, which may occur in the tags (fixed once uploaded), title and the time of uploading. The interaction of multiple counterculture groups may also leave clues in the information, in which we can analyze their relationships and represent them in a numerical way (e.g. weights). We may further derive the hierarchy of groups from their relationships. We will finalize by a good visualization of our data which is capable of demonstrating the massive data we will potentially get.
- If we still have time, we may further construct a time series model over the hierarchy model, in which we will reveal the emergence of counterculture groups and the development in their relationships with others.

### Relevant:

- We will interpret the results of data analysis into findings about the counterculture group in a culture and movement style. We may elaborate on some specific groups (like a famous video game fandom group) to illustrate the counter-culture groups more vividly.

## Data Collection

To get the result we desire with statistical significance, we need to feed our model with tens of millions of data. For each video on bilibili, we will need the video title, upload date, uploader, description, tags, and comments. Luckily, the data on bilibili is well organized and relatively easy to scrape. All videos on Bilibili could be accessed with a unique identifier "av+number", with the number from 2 to 9999999 in ascending order. We also find various open source online API that may be proved helpful. For example, one of the API linked earlier made it possible for us to scrape all the data we need at once.

As most of the Bilibili CDN nodes are deployed in China, we may apply for a virtual machine at Duke Kunshan University for data scraping. We will store the scraped data in SQL database for easy utilization.

## Modules

### Module 4: Data Wrangling 

In our project, we plan to use data wrangling to deal with the scraped data. We will wrangle data through different formats, with missing data, and working with text.
The potential parts we are going to apply in our project are python string operations and regular expressions. Python string operations are likely used to edit data with potential wrong format or with potential unit transformation (similar to some questions in Homework 04), while using regular expressions may help us find the correct data that match our requirements from millions of data. 

### Module 6: Combining Data

In our project, we will use Pandas Group by: split-apply-combine, merge, join, concatenate and compare methods to combine the data that we collected. This module is helpful to gather all the useful dataframes from data wrangling and make them as a whole to get a deep understanding analysis. The potential stages to apply the knowledge from the module 6 (combining data) are data gathering, data cleaning, and data investigation.

### Module 7: Database & SQL

SQL (structured query language) is a convenient and feasible language to deal with data. Similar to Pandas, SQL also has many data selecting and combining methods, such as where, group by, and order by. Additionally, it also has statistical methods by adding aggravate columns. In our project, we plan to use both SQL language and python to make a comprehensive analysis after we scrape data. We may try to add some new data based on our scraped data, but we will make sure that every data is traceable and understandable to our audience.

### Module 8: Visualization

In our project, we will use Python Seabron and Matplotlib to do the data visualization to illustrate our data analysis from applying module 7. We will draw scatterplots, line plot, barplot, heatmap, stackplots and streamgraphs. Data visualization is more understandable to our audience compare to the dataframe. The potential stages to apply the knowledge from the module 8 (Visualization) are data analysis and final report.

## Collaboration Plan

Since this project has a large task volume and huge database, we need to develop an efficient team form and plan ahead for the schedule and the details of the project. We divide our project into 3 phases: (1) data scraping, (2) API design and deployment, and (3) visualization. To maintain efficiency while keeping everyone have chance to learn things from all phases instead of everyone do one part of project, we set “leading birds” for every phase who master the progress of everyone and provided help when others are stuck with their works. With efficient teamwork, we expect this project will cost total 30 hours for each team member. To maintain the efficiency of the teamwork, we plan to meet at least one time a week, however, we can work together whenever and wherever we want since we keep contact frequently via WeChat and email. In order to make the file transformation efficient and stable, we mainly use Google Doc for writing tasks such as this proposal and store the data on private server set by Zezhen so everyone have easy access. Moreover, we consider using GitHub or extensions on V.S. Code to share our code.

Contributer: Eric, Jingheng, Weicheng, Yantao, Zezhen
