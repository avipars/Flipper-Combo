Some links on this site are affiliate links. If you make a purchase through these, I earn a small commission at no extra cost to you.

Tested personally on Momentum firmware revision 007: 

* [CC1101 SubGhz 433Mhz Board](https://s.click.aliexpress.com/e/_Dd17tsN)

    Pins:

        Plugs into all 18 GPIO Pins and the board has the pins numbered accordingly

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


* ESP32-S3 Mini

    Bought it recently and plan on experimenting with GhostESP & Maurader

    Demo Video & more info coming soon


Resources:

* [Official GPIO Docs](https://docs.flipper.net/gpio-and-modules)
