FROM python:3
RUN mkdir /companyapi
WORKDIR /companyapi
ADD . /companyapi
RUN pip install -r requirements.txt
EXPOSE 8000
CMD python manage.py runserver 
