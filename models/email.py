import email
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import meta, engine

mails = Table("email", meta, 
    Column("id", Integer, primary_key=True), 
    Column("idtemplate", String(255)), 
    Column("template", String(255)),
    Column("fecha_creado", String(255)))

meta.create_all(engine)