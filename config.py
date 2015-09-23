WTF_CSRF_ENABLED = True
SECRET_KEY = 'thisisasecret-key' #This needs to be changed in deployment

MONGODB_SETTINGS = {'DB': 'trendalyser'}
DEBUG_TB_PANELS = ['flask.ext.mongoengine.panels.MongoDebugPanel', 'flask_debugtoolbar.panels.timer.TimerDebugPanel', 'flask_debugtoolbar.panels.headers.HeaderDebugPanel', 'flask_debugtoolbar.panels.config_vars.ConfigVarsDebugPanel', 'flask_debugtoolbar.panels.template.TemplateDebugPanel', 'flask_debugtoolbar.panels.logger.LoggingPanel']
