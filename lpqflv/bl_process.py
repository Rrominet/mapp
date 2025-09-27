import subprocess
import threading
import os
import bpy

class blProcess:
    def __init__(self, cmd, cwd=os.getcwd(), outcb=None, errcb=None):
        self._cmd =cmd
        self._cwd = cwd
        self._process = None
        self._thread = None
        self._stdout_lines = []
        self._stderr_lines = []
        self._output_callbacks = []
        self._error_callbacks = []
        self._start_error_callbacks = [] 
        self._on_terminate_callbacks = []
        self._running = False
        self._lock = threading.Lock()
        self.user_data = None

        if (outcb):
            self.addOnOutput(outcb)
        if (errcb):
            self.addOnError(errcb)

    def setCmd(self, cmd):
        """Set the command to be executed"""
        self._cmd = cmd

    def setCwd(self, cwd):
        """Set the current working directory for the process"""
        self._cwd = cwd

    def start(self):
        """Start the process asynchronously on a different thread"""
        if self._running:
            raise RuntimeError("Process is already running")
        
        if not self._cmd:
            raise ValueError("Command not set")
        
        self._running = True
        self._stdout_lines = []
        self._stderr_lines = []
        
        self._thread = threading.Thread(target=self._run_process)
        self._thread.daemon = True
        self._thread.start()

    def _run_process(self):
        """Thread function that starts and monitors the process"""
        try:
            self._process = subprocess.Popen(
                self._cmd,
                cwd=self._cwd,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=1  # Line buffered
            )
            
            stdout_thread = threading.Thread(target=self._read_output, args=(self._process.stdout, self._stdout_lines, self._output_callbacks))
            stderr_thread = threading.Thread(target=self._read_output, args=(self._process.stderr, self._stderr_lines, self._error_callbacks))
            
            stdout_thread.daemon = True
            stderr_thread.daemon = True
            
            stdout_thread.start()
            stderr_thread.start()
            
            self._process.wait()
            
            stdout_thread.join()
            stderr_thread.join()

            def bl_c() : 
                for c in self._on_terminate_callbacks:
                    c()
            bpy.app.timers.register(bl_c)

        except Exception as e:
            # Handle process start errors (like FileNotFoundError for bad executable)
            with self._lock:
                for callback in self._start_error_callbacks:
                    try:
                        def bl_c() : 
                            callback(str(e))
                        bpy.app.timers.register(bl_c)
                    except Exception as cb_error:
                        print(f"Error in start error callback: {cb_error}")
        finally:
            with self._lock:
                self._running = False
                self._process = None

    def _read_output(self, stream, line_list, callbacks):
        """Read from a stream and call callbacks for each line"""
        for line in iter(stream.readline, ''):
            line = line.rstrip('\n')
            with self._lock:
                line_list.append(line)
                for callback in callbacks:
                    try:
                        def bl_c() : 
                            callback(line)
                        bpy.app.timers.register(bl_c)
                    except Exception as e:
                        print(f"Error in callback: {e}")

    def stop(self):
        """Stop the process gracefully"""
        with self._lock:
            if self._process and self._running:
                self._process.terminate()
                self._thread.join()

    def terminate(self):
        """Forcefully terminate the process"""
        with self._lock:
            if self._process and self._running:
                self._process.kill()
                self._thread.join()
                def bl_c() : 
                    for c in self._on_terminate_callbacks:
                        c()
                bpy.app.timers.register(bl_c)

    def output(self):
        """Get all stdout lines from the process"""
        with self._lock:
            return self._stdout_lines.copy()

    def error(self):
        """Get all stderr lines from the process"""
        with self._lock:
            return self._stderr_lines.copy()

    def addOnOutput(self, callback):
        """Add callback that will be called for each new stdout line"""
        with self._lock:
            self._output_callbacks.append(callback)

    def addOnTerminate(self, callback):
        """Add callback that will be called when the process terminates"""
        with self._lock:
            self._on_terminate_callbacks.append(callback)

    def addOnError(self, callback):
        """Add callback that will be called for each new stderr line"""
        with self._lock:
            self._error_callbacks.append(callback)
            
    def addOnStartError(self, callback):
        """Add callback that will be called if the process fails to start"""
        with self._lock:
            self._start_error_callbacks.append(callback)

    def isRunning(self):
        """Check if the process is running"""
        with self._lock:
            return self._running

def chain(processes):
    """
    Execute a chain of processes sequentially, where each process starts
    after the previous one has completed.
    
    Args:
        processes: A list of blProcess objects to be executed in sequence
    """
    if not processes:
        return
        
    # Make a copy of the processes list to avoid modifying the original
    process_queue = processes.copy()
    
    def start_next_process():
        """Start the next process in the queue if available"""
        if not process_queue:
            return
            
        current_process = process_queue.pop(0)
        print ("starting " + str(current_process._cmd))
        
        # Add the completion callback
        current_process.addOnTerminate(start_next_process)
        
        # Start the current process
        try:
            current_process.start()
        except Exception as e:
            print(f"Error starting process in chain: {e}")
            # Continue with next process if this one fails
            bpy.app.timers.register(start_next_process)
    
    # Start the first process
    bpy.app.timers.register(start_next_process)
