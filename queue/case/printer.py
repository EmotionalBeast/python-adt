# -*- coding: utf-8 -*-
# Created by Lazy on 2022/6/9
# Copyright (c) 2022 Lazy. All rights reserved.
import random
from queue.queue import Queue


class Printer:
    def __init__(self, ppm):
        self.page_rate = ppm
        self.current_task = None
        self.time_remaining = 0

    def tick(self):
        if self.current_task is not None:
            self.time_remaining -= 1

        if self.time_remaining <= 0:
            self.current_task = None

    def is_busy(self):
        return self.current_task is not None

    def start_next(self, task):
        self.current_task = task
        self.time_remaining = task.get_pages() * 60 / self.page_rate


class Task:
    def __init__(self, timestamp):
        self._timestamp = timestamp
        self._pages = random.randint(1, 21)

    def get_timestamp(self):
        return self._timestamp

    def get_pages(self):
        return self._pages

    def wait_time(self, current_time):
        return current_time - self._timestamp


def simulation(num_seconds, pages_per_minute):
    lab_printer = Printer(pages_per_minute)
    print_queue = Queue()
    waiting_times = []
    for current_second in range(num_seconds):
        if generate_print_task(20):
            task = Task(current_second)
            print_queue.enqueue(task)
        if (not lab_printer.is_busy()) and (not print_queue.is_empty()):
            next_task = print_queue.dequeue()
            waiting_times.append(next_task.wait_time(current_second))
            lab_printer.start_next(next_task)
        lab_printer.tick()
    average_wait = sum(waiting_times) / len(waiting_times)
    print('Average Wait %6.2f secs %3d tasks remaining.' % (average_wait, print_queue.size()))


def generate_print_task(students):
    number = int(3600/(students * 2)) + 1
    num = random.randint(1, number)
    return num == number


if __name__ == '__main__':
    # 增加模拟次数，查看模拟效果
    for i in range(10):
        simulation(3600, 5)
