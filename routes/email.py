from fastapi import APIRouter, FastAPI
from pydantic import BaseModel
from email.message import EmailMessage
import smtplib 
from smtplib import SMTPResponseException
from starlette.responses import JSONResponse
from fastapi import APIRouter, Response, status
from config.db import conn
from certifi import where
from models.email import mails
from schemas.email import Email

import re

email = APIRouter()

@email.post('/mails', response_model=Email)
async def envia_email(sendmail: Email):

    resultado =  conn.execute(mails.select().where(mails.c.idtemplate == sendmail.idtemplate)).first()

    msg = EmailMessage()
    msg['Subject'] = sendmail.subject
    msg['From'] = 'arellanos.baaeus@gmail.com'
    msg['To'] = sendmail.email
    emailvalidate = sendmail.email
    html = resultado.template.format(subject=sendmail.subject)

    msg.add_alternative(html, subtype="html")
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", emailvalidate):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

                smtp.login('arellanos.baaeus@gmail.com','vkkvjuzevdnnfwcw')

                smtp.send_message(msg)
                return JSONResponse(status_code=200, content={"message": "se ha enviado el email"})

        except SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error

            return JSONResponse(status_code=error_code, content={"message": error_message})
    else: 
        return JSONResponse(status_code=401, content={"message": "El email es inválido "})
