from decouple import config


class Config:
    secret_key = config('secret_key')


class DevelopmentConfig(Config):
    DEBUG = True


config = {'develoment': DevelopmentConfig}
