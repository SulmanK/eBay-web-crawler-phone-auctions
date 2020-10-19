import dash
# CSS applied to the dashboard
external_css = [

    # Normalize the CSS
    "https://cdnjs.cloudflare.com/ajax/libs/normalize/7.0.0/normalize.min.css",

    # Fonts
    "https://fonts.googleapis.com/css?family=Open+Sans|Roboto",
    "https://maxcdn.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css",
    '/assets/base-styles.css',
    '/assets/custom-styles.css',
]


# Dash application
app = dash.Dash(__name__, external_stylesheets=external_css)

server = app.server
app.config['suppress_callback_exceptions'] = True
