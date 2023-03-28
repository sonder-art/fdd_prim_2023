FROM python:latest as base

# Instalar conda
# ## Conda Install
RUN apt-get update && \
    apt-get install -y build-essential  && \
    apt-get install -y wget && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN apt -y update &&\
    apt-get -y install vim
# Install miniconda
ENV PATH="/root/miniconda3/bin:${PATH}"
ARG PATH="/root/miniconda3/bin:${PATH}"
RUN apt-get update
RUN apt-get install -y wget && rm -rf /var/lib/apt/lists/*
RUN wget \
    https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh \
    && mkdir /root/.conda \
    && bash Miniconda3-latest-Linux-x86_64.sh -b \
    && rm -f Miniconda3-latest-Linux-x86_64.sh
# make conda activate command available from /bin/bash --interative shells
RUN conda init bash
RUN conda update -n base -c defaults conda

# Instalar librerias necesarias
WORKDIR /app
COPY requirements.txt /app/requirements.txt
COPY environment.yml /app/environment.yml
RUN conda env update --name base --file /app/environment.yml
RUN pip install -r requirements.txt

# Target para development
FROM base as dev
COPY dev_environment.yml /app/dev_environment.yml
RUN conda env update --name base --file /app/dev_environment.yml
#COPY app.py /app/app.py
ENTRYPOINT ["conda", "run","-n", "base", "jupyter", "lab","--ip=0.0.0.0","--allow-root", "--NotebookApp.token=''","--NotebookApp.password=''"]


# Target de prod
FROM base as prod
# Porque repito este COPY?
COPY app.py /app/app.py
CMD ["python", "-u", "app.py"]
#ENTRYPOINT [ "/bin/bash" ]