class AverageMeter(object):
    """Computes and stores the average and current value.

    Adapted from:
        https://github.com/pytorch/examples/blob/master/imagenet/main.py
    """
    def __init__(self):
        self.avg = 0
        self.val = 0
        self.sum = 0
        self.count = 0

    def reset(self):
        self.__init__()

    def update(self, val, n=1):
        self.val = val
        self.sum += val * n
        self.count += n
        self.avg = self.sum / self.count
