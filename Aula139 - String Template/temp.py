from string import Template
from datetime import datetime
from dados_email import meu_email, minha_senha, meus_clientes

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib

with open('template.html', 'r') as html:
    template = Template(html.read())
    data_atual = datetime.now().strftime('%d/%m/%Y')
    corpo_msg = template.substitute(nome='Pudim', data=data_atual)

msg = MIMEMultipart()
msg['from'] = 'Cabeludo Bonitão'
msg['to'] = meus_clientes
msg['subject'] = 'Atencione, esto el um emaito automatito!'

corpo = MIMEText(corpo_msg, 'html')  # Esou recebendo o arquivo digitado e informando que é um HTML
msg.attach(corpo)  # attach está atrelando a menságem (como um anexo)

with open('img.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    msg.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    try:
        smtp.ehlo()
        smtp.starttls()
        smtp.login(meu_email, minha_senha)
        smtp.send_message(msg)
        print('E-mail enviado com sucesso!')
    except Exception as e:
        print('E-mail não enviado...')
        print('Erro: ', e)
