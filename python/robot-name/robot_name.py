import string
import random
import uuid


class Robot(object):
  def __init__(self):
    self.name = self._random_name()

  def reset(self):
    random.seed(uuid.uuid4())
    self.name = self._random_name()

  def _random_name(self):
    return self._random_alphas() + str(self._random_digits())

  def _random_alphas(self, k=2):
    return ''.join(random.choices(string.ascii_uppercase, k=k))

  def _random_digits(self):
    return random.randint(100, 999)

