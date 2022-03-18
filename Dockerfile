# 
FROM python:3.9-alpine

# 
WORKDIR /app

ENV PYTHONPATH "${PYTHONPATH}:/app"

# 
COPY requirements.txt .

# 
RUN pip3 install -r requirements.txt

COPY . .

#
RUN chmod a+x /app/deploy/docker_entrypoint.sh
ENTRYPOINT ["/app/deploy/docker_entrypoint.sh"]