import smtplib 

main = smtplib.SMTP_SSL('smtp.gmail.com', 465)
send = 'elayarajameenaloshini002@gmail.com'
password = 'rxjl uxdw qyjm tvow'
rec = 'sit20ad009@sairamtap.edu.in'
Msg = 'Testing mail'
main.login(send, password)
main.sendmail(send, rec, Msg)
print('Mail sent')
main.quit()



