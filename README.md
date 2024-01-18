# downscaled

Hardware
 - SABRENT USB Bluetooth 4.0 Micro Adapter for PC \[v4.0 Class 2 with Low Energy Technology\] (BT UB40)
   ![image](https://github.com/MihaStemberger/downscaled/assets/9533590/9ca1c15e-63a5-48d4-91a9-fd7f0d7e9f98)

 - Beurer BF 600
   ![image](https://github.com/MihaStemberger/downscaled/assets/9533590/f8d1a71a-7618-4bff-a527-b1f5549ecb26)

Software

 - Proxmox:
   - Ubuntu server
     - sudo apt install bluez
     - sudo apt get pip
     - sudo pip install bleak
       
 - Python

## First make sure you can see a device with bluetoothctl
 1. start with `bluetoothctl` command
 2. `scan on`, now we should see what devices are available to you.
    ```text
    $ bluetoothctl
    Agent registered
    [CHG] Controller ${CONTROLLER_MAC} Pairable: yes
    [bluetooth]# devices
    Device ${MAC_1} Samsung Galaxy J3 (2016)
    [bluetooth]# scan on
    Discovery started
    [CHG] Controller CONTROLLER_MAC Discovering: yes
    [NEW] Device ${MAC_2} Adv360 Pro
    [NEW] Device ${MAC_BF600} BF600   <---------------- the one we are interested in
    .
    .
    .
    ```
    By observing the output it is known to us, that `Samsung Galaxy J3 (2016)` is already connected to our controller. In addition there are two NEW devices, `Adv360 Pro` and `BF600`.
    
  ## Next step is to try and connect to the BF600 device
   ```python
   import asyncio

   from bleak import BleakClient
   
   ADDRESS = "${MAC_BF600}" # change the value of this variable to whatever your BF600 device MAC address is(should know about it from step 2.)
   
   async def main():
       async with BleakClient(ADDRESS) as client:
           print(f"Connected: {client.is_connected}")
           print(f"Client address is: {client.address}")
   
   if __name__ == "__main__":
        asyncio.run(main())
   ```

   You should be seeing the following output by executing the above code:
   ```text
   Connected: True
   Client address is: ${MAC_BF600}
   ```

   If that is the case you have successfully made a connection to BF600 device


   
