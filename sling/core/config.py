import os


LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO').upper()
LOG_FORMAT = os.environ.get('LOG_FORMAT', '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
LOG_TIMESTAMP_FORMAT = os.environ.get('LOG_TIMESTAMP_FORMAT', '%Y-%m-%d %H:%M:%S %z')
