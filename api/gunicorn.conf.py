import multiprocessing
bind = '0.0.0.0:9000'
workerConnections = 1000
workers = multiprocessing.cpu_count() * 2 + 1
k = 'gevent'