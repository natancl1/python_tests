class Iters:
    def __init__(self, value):
        self.data = value

    def __getitem__(self, i):           # Fallback for iteration
        print('get[%s]:' % i, end='')   # Also for index, slice
        return self.data[i]

    def __iter__(self):                 # Preferred for iteration
        print('iter=> next:', end='')   # Allows multiple active iterators
        for x in self.data:             # no __next__ to alias to next
            yield x
            print('next:', end='')

    def __contains__(self, x):          # Preferred for 'in'
        print('contains: ', end='')
        return x in self.data

