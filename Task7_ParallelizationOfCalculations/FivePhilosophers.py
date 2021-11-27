import threading
import time


class Philosopher(threading.Thread):
    hungry = True

    def __init__(self, index, left_fork, right_fork, is_dead_lock=False):
        threading.Thread.__init__(self)
        self.index = index
        self.leftFork = left_fork
        self.rightFork = right_fork
        self.isDeadlock = is_dead_lock

    def run(self):
        while self.hungry:
            time.sleep(2)
            print('%s is hungry\n' % self.index)
            if self.isDeadlock:
                self.with_deadlock()
            else:
                self.no_deadlock()

    def with_deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            has1 = fork1.acquire()  # philosopher is trying to pick right fork
            has2 = fork2.acquire()  # if succeeded, he is trying to pick left fork, holding right fork all the time
            if has1 and has2:  # if he has both, starts eating
                break
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def no_deadlock(self):
        fork1, fork2 = self.rightFork, self.leftFork
        while self.hungry:
            fork1.acquire()  # philosopher is trying to pick right fork
            locked = fork2.acquire(False)  # if succeeded, he tries to pick left fork
            if locked:  # if left fork free, he starts eating
                break
            fork1.release()  # if not, he puts the right fork back
            print('%s will try other fork\n' % self.index)
            fork1, fork2 = fork2, fork1  # and next time try to pick other fork first
        else:
            return
        self.eat()
        fork2.release()
        fork1.release()

    def eat(self):
        print('%s starts eating\n' % self.index)
        time.sleep(2)
        print('%s finishes eating and thinking\n' % self.index)


def main():

    forks = [threading.Semaphore() for n in range(5)]

    # no deadlock
    print("No deadlock")
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5]) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('---Done---\n')

    # with deadlock
    print('With deadlock')
    philosophers = [Philosopher(i, forks[i % 5], forks[(i+1) % 5], True) for i in range(5)]

    Philosopher.hungry = True
    for x in philosophers:
        x.start()
    time.sleep(10)
    Philosopher.hungry = False
    print('---Done---')


if __name__ == '__main__':
    main()
