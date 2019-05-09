## restful api


### swagger ui

FAB_API_SWAGGER_UI = True


http://localhost:5000/swaggerview/v1


werkzeug:127.0.0.1



## 需要修改几个地方
+ /site-packages/flask_wtf/recaptcha/validators.py


- RECAPTCHA_VERIFY_SERVER = 'https://recaptcha.net/recaptcha/api/siteverify'

+ /site-packages/flask_wtf/recaptcha/widgets.py

- RECAPTCHA_SCRIPT = u'https://recaptcha.net/recaptcha/api.js'
