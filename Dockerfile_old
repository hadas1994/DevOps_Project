FROM python:3
COPY "rest_app.py" /
RUN pip install pymysql=="1.0.2"
EXPOSE 5000
COPY "web_app.py" /
RUN pip install requests=="2.28.0"
EXPOSE 5001
CMD python3 ["backend_testing.py", "frontend_testing.py", "combined_testing.py", "clean_environment.py"]
