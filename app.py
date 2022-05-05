from fastapi import FastAPI
from pydantic import BaseModel
from email.message import EmailMessage
import smtplib 
from smtplib import SMTPResponseException
from starlette.responses import JSONResponse
import re


app = FastAPI()

class Sendmail(BaseModel):
    email: str
    subject: str

@app.post('/sendmail')
async def envia_email(sendmail: Sendmail):

    msg = EmailMessage()
    msg['Subject'] = sendmail.subject
    msg['From'] = 'arellanos.baaeus@gmail.com'
    msg['To'] = sendmail.email
    emailvalidate = sendmail.email
    html = """\
            <DOCTYPE html>
            <html>
                <body>
                    <h1>Hola mundo</h1>
                    <p>subject {sendmail.asunto}</p>
                </body>
            </html>
        """.format(**locals())

    msg.add_alternative(html, subtype="html")
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", emailvalidate):
        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:

                smtp.login('arellanos.baaeus@gmail.com','jpjmrebeogqgvfhi')

                smtp.send_message(msg)
                return JSONResponse(status_code=200, content={"message": "se ha enviado el email"})

        except SMTPResponseException as e:
            error_code = e.smtp_code
            error_message = e.smtp_error

            return JSONResponse(status_code=error_code, content={"message": error_message})
    else: 
        return JSONResponse(status_code=401, content={"message": "El email es inválido "})
