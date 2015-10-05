import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    WTF_CSRF_ENABLED = True
    SECRET_KEY = 'thisisasecret-key' #This needs to be changed in deployment
    MONGODB_SETTINGS = {'DB': 'trendalyser'}

    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    debug = True
    DEBUG_TB_PANELS = ['flask.ext.mongoengine.panels.MongoDebugPanel', 'flask_debugtoolbar.panels.timer.TimerDebugPanel', 'flask_debugtoolbar.panels.headers.HeaderDebugPanel', 'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel', 'flask_debugtoolbar.panels.template.TemplateDebugPanel', 'flask_debugtoolbar.panels.logger.LoggingPanel']
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class ProductionConfig(Config):
    debug = False


config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
