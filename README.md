# eBay-web-crawler-for-popular-phone-auctions

## Objective

* Build a functional eBay web scraping tool. 
* Store and maintain a PostgreSQL database.
* Create a live dashboard that pulls from the database and various metrics using the data.

## Background Information
With the abundance in the number of phones listed on online marketplaces, it overwhelms the user in selecting satisfactory auctions. My approach includes building a web-scraping tool to collect data on phone auctions and calculating various metrics to aid in auction selection. 

---
## Repository Structure
```plaintext
eBay-web-crawler-phone-auctions/
├── Dashboard/                              # Contains files related to the live dashboard
│   ├── assets/                             # CSS/IMG files used in the dashboard
│   ├── layout_assets/                      # All functions used to create the figures in the dashboard layout
│   ├── model/                              # Model related functions
│   ├── Procfile                            # Configuration of the web application
│   ├── app.py                              # Defines the server application
│   ├── index.py                            # Defines the layout of the application
│   └── requirements.txt                    # Python dependencies for the dashboard
├── Scraping_Application_Docker/            # Dockerized web scraping application
│   ├── Dockerfile                          # Dockerfile for setting up the scraping environment
│   ├── active_auctions.py                  # Checks for active auctions and updates the SQL databases
│   ├── clear_db.py                         # Checks if the number of rows in the SQL database exceeds 10,000 rows
│   ├── remove_duplicates.py                # Removes all duplicate item ids from the SQL database
│   ├── requirements.txt                    # Python dependencies for the scraper
|   └── scraper.py                          # Main web scraping script
│   
├── Animation.gif                           # GIF demonstrating the application's functionality
├── LICENSE                                 # Licensing information for the repository
└── README.md                               # Overview of the repository
```
---
## Process:
1) Create the web-scraping script.
2) Containerize the script.
3) Utilize workflow services to execute scripts.
   * Execute scraping to get more auctions.
   * Execute the removal of duplicate ids.
   * Monitor the number of rows in the database and empty if it reaches over 10,000 samples (our database storage limit)
   * Check if an auction is active.
4) Store the data into a database.
5) Preprocess the data.
6) Perform exploratory data analysis.
7) Deployment

## Technologies
* **Docker**
* **Python**
* **Apache Airflow**
* **PostgreSQL**
* **AWS**

## Pertinent Deliverables
* [Dashboard](http://phone-auction-aide-3-env.eba-pt2ur9kp.us-east-1.elasticbeanstalk.com/)

## Demo
![Demo2](Animation.gif)

