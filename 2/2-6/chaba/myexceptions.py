class AuthenticationException(Exception):
    """
        与身份验证相关的异常
    """
    def __init__(self, message_text):
        self.message_text = message_text

    def get_message(self):
        return self.message_text
