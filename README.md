# Swiss-Voting-Data-Analysis-and-Visualization-1848-2023


This project leverages data from [Swissvotes.ch] (https://swissvotes.ch/page/home) to provide a comprehensive analysis and visualization of Swiss voting data from 1848 to 2023. Although the homepage is available in German, French, and English, not all data is accessible in English. This project aims to make this information readily accessible by highlighting the most significant Swiss votes over the years, categorizing them into the upper and lower quantiles. The analysis is presented in an interactive Plotly Dash graph, accompanied by a list that includes direct links to specific votes. Additionally, the results are available for download as HTML files. [Extreme Swiss votes over the years](https://drive.google.com/uc?export=download&id=14p4r9uy71Lk963vjmU-Skqf6KI3aDMFT)

The data used for this purpose comes from the University of Bern. The Année Politique Suisse, based there, maintains a comprehensive data set
(Swissvotes) on all votes that have taken place since the founding of the modern federal state in 1848 (<https://swissvotes.ch/page/dataset>) to 2023. 

Since the data set is very large (834 variables), following variables are selected: 


-   **volkja-proz** : Percentage of yes-votes out of valid votes
-   **ja-lager**: Sum of the voter shares of all parties that recommended their voters to vote "Yes", the yes camp
-   **datum**: Date of the voting day
-   **title_kurz_d**: Short version of the official title of the vote in German
-   **title_kurz_en**: Short version of the official title of the vote in English
-   **swissvoteslink**: Link to the vote
