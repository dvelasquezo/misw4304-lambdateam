#!/bin/sh
gunicorn  --chdir /usr/src/flask_app wsgi:app -w 5 --timeout 3600 --bind :$PORT -e UPLOAD_FOLDER=/usr/src/flask_app/archivosApp/bases/ -e CONVER_FOLDER=/usr/src/flask_app/archivosApp/convertidos/ -e ACCESS_KEY=AKIA25VVIETXHARH4RQC -e SECRET_KEY=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 -e AWS_REGION=us-east-2 -e SQS_ENDPOINT=https://sqs.us-east-2.amazonaws.com/867579940304/alertas-monitor.fifo -e SQS_QUEUE_NAME=sqs-convertidor.fifo -e PASSWORD_BD=Puros98+53A**22L