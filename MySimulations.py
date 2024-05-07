from TaskSimulation import Task, HeapPQ

# See TaskSimulation.py for two example simulations

def simulation1():
       TQ = HeapPQ()
       N = 100
       Tape = list(range(N))

       t0 = Task(-2, 1)
       TQ.insert(0, t0)

       for t in range(N):
              #tt = time
              tt, task = TQ.findmin()
              while task is not None and tt == t:
                     task.execute(Tape, t)
                     TQ.removemin()

                     next_time = tt + task.multiplicity
                     TQ.insert(next_time, task)

                     tt, task = TQ.findmin()
       return Tape, TQ
     

def simulation2():
       TQ = HeapPQ()
       N = 10
       Tape = list(range(N))
       
       for t in range(N):
              if t < 2:
                     continue
              time = t
              task = Task(Tape[t], 1)

              while task is not None and time == t:
                     task.execute(Tape, time)
                     TQ.removemin()
                     next_time = t + 1
                     TQ.insert(next_time, task)
                     time, task = TQ.findmin()
              #fix code below (when next_time is 't+1' multiplier is 9, when it
              #is t+2, multiplier is 10

              TQ.removemin()
              task = Task(t+1, 1)
              TQ.insert(t+1, task)
       return Tape, TQ
       pass

def simulation3():
       TQ = HeapPQ()
       N = 10
       Tape = list(range(N))

       for t in range(N):
              if t < 1:
                     continue
              time = t
              task = Task(Tape[t]**2, 1)

              while task is not None and time == t:
                     task.execute(Tape, time)
                     TQ.removemin()
                     next_time = t + 1
                     TQ.insert(next_time, task)
                     time, task = TQ.findmin()

              TQ.removemin()
              task = Task((t+1)**2, 1)
              TQ.insert(t+1, task)
       return Tape, TQ
                     
       pass

def simulation4():
       TQ = HeapPQ()
       N = 100
       Tape = list(range(N))

       for t in range(N):
              if t < 2:
                     continue

              time, task = TQ.findmin()

              while task is not None and time == t:
                     task.execute(Tape, time)
                     TQ.removemin()
                     next_time = t + task.multiplicity
                     TQ.insert(next_time, task)
                     time, task = TQ.findmin()

              if Tape[t] != 0:
                     task = Task(0, t)
                     TQ.insert(t+task.multiplicity, task)
              
                     
       len_Tape = len(Tape)
       while len_Tape > 0:
              for i in Tape:
                     if i <= 1:
                            Tape.remove(i)
              len_Tape -= 1
       return Tape, TQ
       pass


def simulation5():
       TQ = HeapPQ()
       N = 100
       Tape = list(range(N))

       for t in range(N):
              if t < 2:
                     continue
              task = Task(-1, t)
              time = t
              TQ.insert(t, task)

              while task is not None and time == t:
                     task.execute(Tape, time)
                     TQ.removemin()
                     TQ.insert(t+task.multiplicity, task)
                     time, task = TQ.findmin()

       len_Tape = len(Tape)
       while len_Tape > 0:
              for i in Tape:
                     if i <= -1:
                            Tape.remove(i)
              len_Tape -= 1

       return Tape, TQ
       pass
#print(simulation5())
