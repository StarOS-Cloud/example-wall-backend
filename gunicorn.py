
# The socket to bind.
bind='0.0.0.0:5000'

# The number of worker processes for handling requests.
workers = 1

# The number of worker threads for handling requests.
threads = 2

# The maximum number of pending connections.
backlog=2048

# The type of workers to use.
worker_class="sync" #sync, gevent, meinheld

# The maximum number of simultaneous clients.
worker_connections=1000

# Workers silent for more than this many seconds are killed and restarted.
timeout=30

# debug=True

# A base to use with setproctitle for process naming.
proc_name='wall-api'

# A filename to use for the PID file.
pidfile='wall-api.pid'

# Switch worker processes to run as this user.
# user = 'root'

# The Access log file to write to.
accesslog = 'log/access.log'

# The access log format.
access_log_format = '%(t)s %(h)s %(l)s %(u)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" %(D)s %({Header}i)s %({Header}o)s'

# The Error log file to write to.
errorlog = 'log/error.log'

# The granularity of Error log outputs. debug / info / warning / error / critical
loglevel='error'
