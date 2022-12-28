FROM python:3.8-alpine

WORKDIR /app

COPY . .
RUN pip install -r requirements.txt

# RUN pytest

ENTRYPOINT [ "python" ]
CMD ["my_app.py"]

EXPOSE 5000