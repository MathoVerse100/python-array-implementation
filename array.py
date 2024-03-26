class array():
    def __init__(self, *args):
        self.array_ = list(args[0]) if len(args) == 1 and type(args[0]) == type((i for i in [])) else list(args)

    def __str__(self):
        output = f"array({', '.join([str(x) for x in self.array_])})".split("'")
        return "".join(output)
    
    def __add__(self, other):
        if isinstance(other, (int, float)):
            return array(*[self.array_[i] + other for i in range(len(self.array_))])
        elif isinstance(other, array):
            return array(*[self.array_[i] + other.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[self.array_[i] + other[i] for i in range(len(self.array_))])
        else:
            raise TypeError("Unsupported operand type(s) for +: '{}' and '{}'".format(type(self), type(other)))
    
    def __radd__(self, other):
        return self.__add__(other)
    
    def __sub__(self, other):
        if isinstance(other, (int, float)):
            return array(*[self.array_[i] - other for i in range(len(self.array_))])
        elif isinstance(other, array):
            return array(*[self.array_[i] - other.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[self.array_[i] - other[i] for i in range(len(self.array_))])
        else:
            raise TypeError("Unsupported operand type(s) for -: '{}' and '{}'".format(type(self), type(other)))
        
    def __rsub__(self, other):
        return self.__sub__(other)
        
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return array(*[self.array_[i] * other for i in range(len(self.array_))])
        elif isinstance(other, array):
            return array(*[self.array_[i]*other.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[self.array_[i]*other[i] for i in range(len(self.array_))])
        else:
            raise TypeError("Unsupported operand type(s) for *: '{}' and '{}'".format(type(self), type(other)))
        
    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, other):
        if isinstance(other, (int, float)):
            other_list = [other]*len(self)
            other_array = array(*other_list)
            return self.__truediv__(other_array)
        elif isinstance(other, array):
            resulting_list = []
            for i in range(len(self.array_)):
                if other.array_[i] == 0:
                    if self.array_[i] == 0:
                        resulting_list.append('UNDEFINED')
                    else:
                        if self.array_[i] > 0:
                            resulting_list.append(float('inf'))
                        else:
                            resulting_list.append(-float('inf'))
                else:
                    resulting_list.append(round(self.array_[i] / other.array_[i], 2))
            return array(*resulting_list)
        elif isinstance(other, list):
            other_list = array(*other)
            return self.__truediv__(other_list)
        else:
            raise TypeError("Unsupported operand type(s) for /: '{}' and '{}'".format(type(self), type(other)))

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            other_list = [other]*len(self)
            other_array = array(*other_list)
            return other_array.__truediv__(self)
        elif isinstance(other, list):
            other_array = array(*other)
            return other_array.__truediv__(self)
        
    def __mod__(self, other):
        if isinstance(other, (int, float)):
            return array(*[self.array_[i] % other for i in range(len(self.array_))])
        elif isinstance(other, array):
            return array(*[self.array_[i] % other.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[self.array_[i] % other[i] for i in range(len(self.array_))])
        else:
            raise TypeError("Unsupported operand type(s) for %: '{}' and '{}'".format(type(self), type(other)))
    
    def __rmod__(self, other):
        if isinstance(other, (int, float)):
            return array(*[other % self.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[other[i] % self.array_[i] for i in range(len(self.array_))])
        
    def __pow__(self, power):
        if isinstance(power, array):
            return array(*[self.array_[i] ** power.array_[i] for i in range(len(self.array_))])
        elif isinstance(power, list):
            return array(*[self.array_[i] ** power[i] for i in range(len(self.array_))])
        elif isinstance(power, int) or isinstance(power, float):
            if power < 0:
                return self.__truediv__(power)
            return array(*[self.array_[i] ** power for i in range(len(self.array_))])
        else:
            raise TypeError("Unsupported operand type(s) for 'pow': '{}' and '{}'".format(type(self), type(power)))
    
    def __rpow__(self, other):
        if isinstance(other, (int, float)):
            return array(*[other ** self.array_[i] for i in range(len(self.array_))])
        elif isinstance(other, list):
            return array(*[other[i] ** self.array_[i] for i in range(len(self.array_))])
    
    def __getitem__(self, index):
        return array(*self.array_[index])
    
    def __iter__(self):
        return iter(self.array_)
    
    def __len__(self):
        return len(self.array_)
    
    def prod(self):
        product = 1
        for e in self:
            product *= e
        return product
    
    def sorted(self, key=None, reverse=None):
        if key is None and reverse is None:
            return array(*sorted(self))
        elif key is None:
            return array(*sorted(self, reverse=reverse))
        elif reverse is None:
            return array(*sorted(self, key=key))
        return array(*sorted(self, key=key, reverse=reverse))
               
    def index(self, element):
        indices = [] 
        i = 0

        while True:
            try:
                index_ = self.array_[i:].index(element) + i
                indices.append(index_)
                i += index_ + 1
            except (IndexError, ValueError):
                break
            
        return indices
    
    def append(self, *elements):
        for element in elements:
            if isinstance(element, list) or isinstance(element, array):
                for e in element:
                    self.array_.append(e)
            else:
                self.array_.append(element)
        return
    
    def prepend(self, *elements):
        current = []
        for element in elements:
            if isinstance(element, list) or isinstance(element, array):
                for e in element:
                    current.append(e)
            else:
                current.append(element)
        
        self.array_ = current + self.array_
        return
