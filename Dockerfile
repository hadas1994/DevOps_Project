FROM python:3
COPY "rest_app.py" /
RUN pip install pymysql=="1.0.2"
EXPOSE 5000
CMD python3 ["docker_backend_testing.py", "clean_environment.py"]
