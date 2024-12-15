Some links on this site are affiliate links. If you make a purchase through these, I earn a small commission at no extra cost to you.

Tested personally on Momentum firmware revision 007: 

* [CC1101 SubGhz 433Mhz Board](https://s.click.aliexpress.com/e/_Dd17tsN)

    Pins:

        Plugs into all 18 GPIO Pins and the board has the pins numbered accordingly (ensure the numbers on the PCB are facing up)

        In practice, there are only visible traces to a subset of those (8 pins)

    Works natively in the Sub-Ghz App (in Frequency Analyzer, you can see Ext on the top left meaning external antenna is in use). Via Radio Settings, you can toggle the flipper between the internal CC1101 or the external one you bought. 

    Can receive signals in the general sub-ghz range, but it is advised only to send signals that are 433Mhz to reduce risk of damaging antenna and/or board.

    Even though the listing states that it can control mouses and Wi-Fi, it can really only send and transmit sub-ghz signals

    Fits well even with a case on.

    A bit top heavy, and advised to 3D print a case/enclosure for it, or buy a slimmer module

    Demo Video coming soon


* [DHT11 - Temperature and Humidity sensor](https://s.click.aliexpress.com/e/_Ddo8mjr)
    
    Pins:

        9 (3.3v) for VCC 

        10 for SWC (data) 

        11 for Ground

    Works with the UNITEMP flipper app (it will ask you which module are you using and then what pin is relevant) but not the older DHT-Monitor app 

    Doesn't fit well with a silicon case, you can remove the case or get 3 jumper (dupont) wires and connect via them

    You are better off getting a more accurate sensor (such as BMP280 or BME280), make sure it’s supported by the [UNITEMP repo](https://github.com/quen0n/unitemp-flipperzero) (there is an image with a table of supported sensors)


    [![Demo Video of DHT11](https://img.youtube.com/vi/Jic9GVFarsc/0.jpg)](https://www.youtube.com/watch?v=Jic9GVFarsc)


* [ESP32-S3 Mini](https://s.click.aliexpress.com/e/_o2EzYFD)

    Also known as S3 Zero

    B = Boot

    R = Reset

    Make sure to buy the one with pre-soldered pins (M/Welded version)

    Additionally, you will need 4 [Male to Female Dupont Cables](https://s.click.aliexpress.com/e/_opdRKWB)

    I am experimenting with GhostESP & Maurader

    Pinout:

    * 3V3 - 9 (FLIPPER) -> 3V3 (ESP)

    * TX - 13 (FLIPPER) -> RX (ESP)

    * RX - 14 (FLIPPER) -> TX (ESP)

    * GROUND - 11 (FLIPPER) -> GROUND (ESP32)

    [![Video with Pinouts](https://img.youtube.com/vi/3hAXeu2nMg0/0.jpg)](https://www.youtube.com/watch?v=3hAXeu2nMg0)

    GhostESP:

    * Go to the [latest release](https://github.com/Spooks4576/Ghost_ESP/releases)

    * Then unzip the asset file matching your board, I selected esp32s3-generic.zip

    * Go to USB Connection method: https://github.com/Spooks4576/Ghost_ESP/wiki/Installation#usb-connection-method

    * When installing for the S3, ensure to use:

        bootloader.bin at 0x0

        partition-table.bin 0x8000  

        Ghost_ESP_IDF.bin 0x10000

    [![Demo Video](https://img.youtube.com/vi/0_xXlQu8Fg4/0.jpg)](https://www.youtube.com/watch?v=0_xXlQu8Fg4)


Resources:

* [Official GPIO Docs](https://docs.flipper.net/gpio-and-modules)
