# eBay-web-crawler-for-popular-phone-auctions

## Objective

* Build a functional eBay web scraping tool. 
* Store and maintain a PostgreSQL database.
* Create a live dashboard that pulls from the database and various metrics using the data.

## Background Information
With the abundance in the number of phones listed on online marketplaces, it overwhelms the user in selecting satisfactory auctions. My approach includes building a web-scraping tool to collect data on phone auctions and calculating various metrics to aid in auction selection. 

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
7) Deploymen

## Technologies


## Pertinent Deliverables
* [Dashboard](https://ebay-scraping-popular-phones.herokuapp.com/)
