FROM python:3.10-slim

WORKDIR /app
COPY app.py .
COPY requirements.txt .
RUN pip install -r requirements.txt && apt update && apt install -y binutils && pyinstaller --clean -F app.py 

FROM ubuntu:22.04
WORKDIR /app/
COPY --from=0 /app/dist/app ./
EXPOSE 5000
CMD [ "./app" ]

