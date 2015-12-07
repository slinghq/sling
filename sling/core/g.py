import threading
import uuid


class G(threading.local):

    @property
    def transaction_id(self):
        if getattr(self, '_transaction_id', None) is None:
            self.generate_transaction_id()
        return self._transaction_id

    def generate_transaction_id(self):
        self._transaction_id = str(uuid.uuid4())

    def clear_transaction_id(self):
        self._transaction_id = None


g = G()
