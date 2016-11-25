import subprocess
import time
from datetime import datetime
from threading import Thread

try:
    from Queue import Queue, Empty
except ImportError:
    from queue import Queue, Empty # for Python 3.x

numServers = 4
pythonPath = "..\Panda3D-1.9.0\python\ppython.exe"

def launchWithoutConsole(command, args):
   """Launches 'command' windowless"""
   startupinfo = subprocess.STARTUPINFO()
   startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW

   return subprocess.Popen([command] + args, startupinfo=startupinfo,
                    stderr=subprocess.PIPE, stdout=subprocess.PIPE)

def startAstron():
    process = launchWithoutConsole("start_astron_cluster.bat",[])
    return process

def startUberdog():
    process = launchWithoutConsole("start_uberdog_server.bat",[])
    return process


def startAISever(number):
    process = launchWithoutConsole("start_ai_server.bat", [str(number)])
    return process


def enqueue_output(out, queue, prefix):
    for line in iter(out.readline, b''):
        queue.put((prefix + line).strip())
    out.close()

timeout = 0.1

if __name__ == "__main__":
    processes = []
    print("Starting astron")
    astron = startAstron()
    print("Starting uberdog")
    uberdog = startUberdog()

    for i in range(input('Number of districts?: ')):
        processes.append(startAISever(i+1))
        print("Started Server " + str(i+1))
        time.sleep(1)

    q = Queue()
    threads = []
    i = 1
    for p in processes:
        threads.append(Thread(target=enqueue_output, args=(p.stderr, q, "[District %s]:: " %(i))))
        i += 1

    threads.append(Thread(target=enqueue_output, args=(astron.stdout, q, "[Astron] ")))
    threads.append(Thread(target=enqueue_output, args=(uberdog.stderr, q, "[Uberdog] ")))

    for t in threads:
        t.daemon = True
        t.start()

    while True:
        try:
            line = q.get_nowait()
        except Empty:
            pass
        else:
            print(datetime.now().strftime("%Y-%m-%d %H:%M:%S")+ ' - ' + line)

        #break when all processes are done.
        if all(p.poll() is not None for p in processes):
            break

    print('All processes done')
