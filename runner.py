import asyncio
import subprocess
import sys

bluetoothctl_process = None
script_process = None


async def start_detached_bluetoothctl():
    global bluetoothctl_process
    bluetoothctl_process = subprocess.Popen(["bluetoothctl"],
                                            stdin=subprocess.PIPE,
                                            stdout=subprocess.PIPE,
                                            stderr=subprocess.PIPE,
                                            close_fds=True)


async def kill_bluetoothctl_process():
    global bluetoothctl_process
    if bluetoothctl_process:
        bluetoothctl_process.terminate()
        bluetoothctl_process.wait(timeout=1)  # Wait for the process to terminate
        if bluetoothctl_process.poll() is None:
            # If the process is still running after terminate, force kill it
            bluetoothctl_process.kill()


async def execute_python_script(device_address, user_pin):
    global script_process
    script_process = subprocess.run(["python3", "main.py", device_address, user_pin])


async def main(device_address, user_pin):
    print(f"Runner is starting")

    try:
        # Start bluetoothctl
        await start_detached_bluetoothctl()

        # Execute your Python script
        await execute_python_script(device_address, user_pin)

    finally:
        # Stop bluetoothctl
        await kill_bluetoothctl_process()


asyncio.run(main(sys.argv[1], sys.argv[2]))
