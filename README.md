# EMW100R Remote Controlled Switch

This is a simple Python script for the use with a 433 MHz RF
transmitter (tested with FS1000A), a Rasbperry Pi and EMW100R series
remote controlled switches.

The EMW100R remote controlled switches are made by EverFlourish for
Clas Ohlson AB.

## Protocol

The only
[documentation](http://kinavara.blogspot.se/2015/01/remote-control-power-shitch.html)
I could find on the web turned out not to work with my switches.

Probably the protocol varies between revisions of the switches. This
protocol is tested with my switches labelled with: `Ref: 26.1183` &
`200909 28239`.

After sniffing the protocol I learned that the message format is
`[INTRO],[ID],[COMMAND]` and the transmission frequency is around 1.75
KHz.

### Intro

Intro sequence is:
`10101010101001001010100100101010010010101001001010010100101001010100100101001010`
(80 bits)
Hexdecimal: `0XAAA4A92A4A9294A5494AL`

### ID

The ID is 27 bits long

| ID | Binary                      | Hexadecimal |
|----|-----------------------------|-------------|
|  1 | 100101001010010100100101001 | 0X4A52929   |
|  2 | 100100101001010010101001010 | 0X494A54A   |
|  3 | 010101001001010100101001001 | 0X2A4A949   |
|  4 | 010100101010010100101001010 | 0X295294A   |

### Command

The command is 22 bits long

Switch On:  `0100101001010010100101 (0X1294A5)`
Switch Off: `0101001010010100101001 (0X14A529)`

## Usage

The Python script is fairly minimal as my only desire was to integrate
it with [Home Assistant](https://home-assistant.io/).

Usage: `./EMW100.py [ID] [STATE]`

Examples:
- Turn on switch 1: `./EMW100.py 1 1`
- Turn off switch 4: `./EMW100.py 4 0 `

Change `TX_PIN` to whatever GPIO pin you connect the DATA line to from
the RF Transmitter.
