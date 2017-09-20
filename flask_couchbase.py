from flask import current_app
import couchbase


# Find the stack on which we want to store the database connection.
# Starting with Flask 0.9, the _app_ctx_stack is the correct one,
# before that we need to use the _request_ctx_stack.
try:
    from flask import _app_ctx_stack as stack
except ImportError:
    from flask import _request_ctx_stack as stack


class Couchbase(object):
    def __init__(self, app=None):
        self.app = app
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        # Use the newstyle teardown_appcontext if it's available,
        # otherwise fall back to the request context
        if hasattr(app, 'teardown_appcontext'):
            app.teardown_appcontext(self.teardown)
        else:
            app.teardown_request(self.teardown)

    def connect(self):
        conn = self._make_conn_string(current_app.config['COUCHBASE_CONNECTION'],
                                      current_app.config.get('COUCHBASE_CONNECT_OPTIONS'))
        password = current_app.config.get('COUCHBASE_PASSWORD')
        return couchbase.bucket.Bucket(conn, password=password)

    def teardown(self, exception):
        self
        ctx = stack.top
        if hasattr(ctx, 'couchbase_db'):
            del ctx.couchbase_db

    @property
    def connection(self):
        ctx = stack.top
        if ctx is not None:
            if not hasattr(ctx, 'couchbase_db'):
                ctx.couchbase_db = self.connect()
            return ctx.couchbase_db

    def _make_conn_string(self, conn, options=None):
        self
        if options is None:
            return conn
        return conn + '&' + options
