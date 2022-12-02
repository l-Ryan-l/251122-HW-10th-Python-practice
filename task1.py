class MinStat:

    def add_number(self, number):
        list_numbers = []
        for i in number:
            list_numbers.append(i)
        return list_numbers

    def result(self, list_numbers):
        if list_numbers == []:
            return 'None'
        else:
            minn = list_numbers[0]
            for i in list_numbers:
                if i < minn:
                    minn = i
            return minn


class MaxStat:

    def add_number(self, number):
        list_numbers = []
        for i in number:
            list_numbers.append(i)
        return list_numbers

    def result(self, list_numbers):
        if list_numbers == []:
            return 'None'
        else:
            maxx = list_numbers[0]
            for i in list_numbers:
                if i > maxx:
                    maxx = i
            return maxx


class AverageStat:

    def add_number(self, number):
        list_numbers = []
        for i in number:
            list_numbers.append(i)
        return list_numbers

    def result(self, list_numbers):
        if list_numbers == []:
            return 'None'
        else:
            count = len(list_numbers)
            summ = 0
            res = 0
            for i in list_numbers:
                summ += i
            res = summ / count
            return res


values = [1, 5, 4, 9, 63]
mins = MinStat()
maxs = MaxStat()
average = AverageStat()
mins.add_number(values)
maxs.add_number(values)
average.add_number(values)
print(mins.result(values))
print(maxs.result(values))
print('{:<05.3}'.format(average.result(values)))
