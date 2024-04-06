FROM python:3.8

WORKDIR /app

# 复制应用文件
COPY . /app

# 安装依赖
RUN pip install Flask uwsgi pandas flask_cors pytz matplotlib

# 创建非root用户，这里我们创建一个名为 "myappuser" 的用户
RUN adduser --disabled-password --gecos '' myappuser

# 切换到非root用户
USER myappuser

# 启动命令，启用uWSGI的主进程管理器并以非root用户运行
CMD ["uwsgi", "--http", "0.0.0.0:5000", "--module", "backend:app", "--master", "--processes", "1", "--threads", "8"]
