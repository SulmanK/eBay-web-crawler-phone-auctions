FROM python:3.7
WORKDIR /code
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY scraper.py .
COPY clear_db.py .
COPY remove_duplicates.py .
COPY active_auctions.py .
CMD [ "python","./scraper.py" ]