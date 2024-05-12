import asyncio
import subprocess

bluetoothctl_process = None
script_process = None


def start_detached_bluetoothctl():
    global bluetoothctl_process
    bluetoothctl_process = subprocess.Popen(["bluetoothctl"], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE, close_fds=True)


def kill_bluetoothctl_process():
    global bluetoothctl_process
    if bluetoothctl_process:
        bluetoothctl_process.terminate()
        bluetoothctl_process.wait(timeout=1)  # Wait for the process to terminate
        if bluetoothctl_process.poll() is None:
            # If the process is still running after terminate, force kill it
            bluetoothctl_process.kill()


async def execute_python_script():
    global script_process
    script_process = subprocess.run(["python", "main.py"])


async def main():
    print(f"Starting")
    # Start bluetoothctl
    start_detached_bluetoothctl()
    await asyncio.sleep(5)

    # Execute your Python script
    await execute_python_script()

    # Stop bluetoothctl
    kill_bluetoothctl_process()


asyncio.run(main())
