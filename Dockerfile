FROM python:3.9

# Обновляем список пакетов и устанавливаем необходимые пакеты
# RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" | tee /etc/apt/sources.list.d/google-chrome.list

RUN apt-get update && \
    apt-get install -y redis-server postgresql postgresql-contrib
    # apt-get -y install curl unzip xvfb libxi6 libgconf-2-4 google-chrome-stable && \
    # apt-get install apt-utils
    


# RUN curl -sS -o - https://dl-ssl.google.com/linux/linux_signing_key.pub | apt-key add && \
#     echo "deb https://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google.list && \
#     apt-get -y update && \
#     apt-get -y install google-chrome-stable && \
#     LATEST_CHROMEDRIVER_VERSION=$(curl -sS chromedriver.storage.googleapis.com/LATEST_RELEASE) && \
#     curl -sS -o /tmp/chromedriver_linux64.zip http://chromedriver.storage.googleapis.com/${LATEST_CHROMEDRIVER_VERSION}/chromedriver_linux64.zip && \
#     unzip /tmp/chromedriver_linux64.zip chromedriver -d /usr/local/bin/ && \
#     chmod +x /usr/local/bin/chromedriver


# Копируем файлы внутрь контейнера
COPY . /app
    
# Устанавливаем зависимости Python
RUN pip install -r /app/requirements.txt

# Настраиваем переменные окружения для PostgreSQL
# ENV POSTGRES_USER=suslicketeam
# ENV POSTGRES_PASSWORD=AndrewSus228
# ENV POSTGRES_DB=EpicGamesBot

ENV PYTHONPATH="/app/src/:${PYTHONPATH}"


WORKDIR /app/src/

# Запускаем PostgreSQL и Redis
# CMD service redis-server start && service postgresql start && python parser/main.py && python bot/bot.py
# parser/main.py && python bot/bot.py
# CMD ["Xvfb", ":99", "-screen", "0", "1920x1080x24", "-ac"]
# CMD [ "python", "parser/main.py"]  
# CMD ["./start.sh"]
CMD Xvfb :99 -screen 0 1920x1080x24 -ac && python parser/main.py
# CMD /bin/bash -il
# CMD service postgresql start && /bin/bash -il