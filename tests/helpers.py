from functools import wraps
from app import create_manager
from app.db import db


def with_context(test):
    @wraps(test)
    def _wrapped_test(self):
        with self.app.app_context():
            with self.app.test_request_context():
                test(self)
    return _wrapped_test


def with_client(test):
    @wraps(test)
    def _wrapped_test(self):
        with self.app.test_client() as client:
            test(self, client)
    return _wrapped_test


def setUpApp(self):
    manager = create_manager()
    self.app = manager.app
    self.manager = manager
    self.app.config['TESTING'] = True


def setUpDB(self):
    with self.app.app_context():
        db.create_all()


def tearDownDB(self):
    with self.app.app_context():
        db.session.remove()
        db.drop_all()
