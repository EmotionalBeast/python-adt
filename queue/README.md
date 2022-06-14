## 队列 queue (FIFO)
    队列的概念：
        front 队首 出队列的位置
        rear 队尾 入队列的位置
    队列的操作：
        Queue()
        enqueue(any)
        dequeue() -> any
        is_empty() -> bool
        size() -> int

## 双端队列 deque
    双端队列的概念：
        front 队首
        rear 队尾
        队首 队尾都可以出入队列
    队列的操作：
        Deque()
        add_front(any)
        add_rear(any)
        remove_front() -> any
        remove_rear() -> any
        is_empty() -> bool
        size() -> int

## 案例
    josephus.py 环状队列， 间隔取数问题
    print.py 打印机问题