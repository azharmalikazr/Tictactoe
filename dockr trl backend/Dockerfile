FROM python:3.6


WORKDIR /app


COPY . .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install -U flask-cors


ENTRYPOINT [ "python" ]
CMD [ "ticTacToeServer.py" ]