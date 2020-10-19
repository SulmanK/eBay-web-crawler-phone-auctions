#--------------------- Packages
from app import app
import dash_html_components as html
import dash_core_components as dcc
# --------------------- Tab 1
"""First Tab of Plotly Dash Web Application."""
tab_1_layout = html.Div(
    [
        dcc.Markdown(
            ''' 
With the abundance in the number of phones listed on online marketplaces, it overwhelms the user in selecting satisfactory auctions. My approach includes building a web-scraping tool to collect data on phone auctions and calculating various metrics to aid in auction selection. 
            '''
        ),

        html.Div([
            dcc.Markdown(
                '''
**Process**


1) _Create the web-scraping script._

2) _Containerize the script._

3) _Utilize workflow services to perform scraping daily. _

4) _Store the data into a database._

5) _Preprocess the data._

6) _Perform exploratory data analysis._

7) _Deployment._


                    '''
            ),
        ], className='one-half column'),


        html.Div(

            # Create Banner Layout (Title and Logos)
            [
                html.Div(
                    [
                        dcc.Markdown('''
                            **Technologies Used**
                            '''),

                        # Insert Github Logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "python_logo.png"))
                            ], href="https://www.python.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "docker_logo.png"))
                            ], href="https://www.docker.com/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "apache_airflow_logo.png"))
                            ], href="https://airflow.apache.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "postgresql_logo.png"))
                            ], href="https://www.postgresql.org/",
                        ),

                        # Insert Dash logo with href link
                        html.A(
                            [
                                html.Img(src=app.get_asset_url(
                                    "heroku_logo.png"))
                            ], href="https://www.heroku.com/",
                        ),

                    ], className="one-half column",
                )
            ], className="technology"
        ),
        html.Div([
            dcc.Markdown(
                '''
**Future Work**

* Scale up PostgreSQL database.
* Create a functionality for notifications - select a certain threshold for auction pricing and the application will notify you.


More information on the technical details is available on the GitHub repository. 

Click the Application Tab on the top of the page to begin!
                    '''
            )], className='twelve columns'
        )
    ], style={'padding': '2rem 4rem 2rem 4rem', 'fontSize': 28,
              'font-family': "Myriad Pro", 'color': "#000000",

              }
)
