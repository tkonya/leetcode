# works, but is too slow, and also space-inefficient
# class MyCalendarThree:
#
#     def __init__(self):
#         self.dict = {}
#         self.max = 0
#
#     def book(self, start, end):
#         """
#         :type start: int
#         :type end: int
#         :rtype: int
#         """
#         for i in range(start, end):
#             if i in self.dict:
#                 self.dict[i] += 1
#                 if self.dict[i] > self.max:
#                     self.max = self.dict[i]
#             else:
#                 self.dict[i] = 1
#                 if self.max < 1:
#                     self.max = 1
#
#         return self.max


class MyCalendarThree:

    def __init__(self):
        self.bookings = []
        self.max = 0

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: int
        """
        print('----------------------------------\ncreating booking for: ' + str(start) + ' - ' + str(end))
        # check for collisions
        collisions = self.get_collisions(start, end)
        if len(collisions) > 0:
            self.bookings += self.merge_collisions(start, end, collisions)
        else:
            self.bookings.append(TimeSegment(start, end, 1))


        print('all bookings:')
        for b in self.bookings:
            b.print()
            if b.count > self.max:
                self.max = b.count

        return self.max

    def get_collisions(self, start, end):
        collisions = []
        non_collisions = []
        for i, b in enumerate(self.bookings):
            if start < b.end and end > b.start:
                collisions.append(b)
            else:
                non_collisions.append(b)

        self.bookings = non_collisions
        return collisions

    @staticmethod
    def merge_collisions(start, end, collisions):

        print('merging collisions:')
        for c in collisions:
            c.print()
        print('[' + str(start) + ' - ' + str(end) + ' (1)]')

        min_time = start
        max_time = end

        starts = [start]
        ends = [end]

        for c in collisions:
            for x in range(0, c.count):
                starts.append(c.start)
                ends.append(c.end)

            if c.start < min_time:
                min_time = c.start
            if c.end > end:
                max_time = c.end

        current_segment = None
        count = 0
        merged_collisions = []
        for time in range(min_time, max_time + 1):

            if time in starts or time in ends:

                next_segment = False
                while time in starts:
                    count += 1
                    starts.remove(time)
                    next_segment = True
                while time in ends:
                    count -= 1
                    ends.remove(time)
                    next_segment = True

                if next_segment:
                    if current_segment is not None:
                        if current_segment.count == count:
                            continue  # don't make a new segment if the counts are the same
                        current_segment.end = time
                        merged_collisions.append(current_segment)
                    current_segment = TimeSegment(time, None, count)

        print('merged collisions:')
        for mc in merged_collisions:
            mc.print()

        return merged_collisions


class TimeSegment:

    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count

    def print(self):
        print('[' + str(self.start) + ' - ' + str(self.end) + ' (' + str(self.count) + ')]')


# Your MyCalendarThree object will be instantiated and called as such:
cal = MyCalendarThree()
print('result: ' + str(cal.book(10, 20)) + '\n\n')
print('result: ' + str(cal.book(50, 60)) + '\n\n')
print('result: ' + str(cal.book(10, 40)) + '\n\n')
print('result: ' + str(cal.book(5, 15)) + '\n\n')
print('result: ' + str(cal.book(5, 10)) + '\n\n')
print('result: ' + str(cal.book(25, 55)) + '\n\n')