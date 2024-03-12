FROM python:latest

COPY lvmtoExcel.py /app/

WORKDIR /app

RUN pip install pandas

CMD [ "python3", "lvmtoExcel.py" ]
