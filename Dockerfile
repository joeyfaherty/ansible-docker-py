FROM python:3
ADD app.py /
ENTRYPOINT [ "python", "./app.py" ]
