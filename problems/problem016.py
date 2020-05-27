class OrderLogger:
  def __init__(self):
    self.log = []

  def record(self, l: int) -> None:
    self.log.append(l)
    
  def get_last(self, n: int) -> int:
    size = len(self.log)
    return self.log[size-n]