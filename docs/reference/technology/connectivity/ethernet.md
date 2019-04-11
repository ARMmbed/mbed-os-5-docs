<h1 id="ethernet-technology">Ethernet</h1>

The term "Ethernet" refers to technologies first introduced in 1980 and standardized in 1983 as IEEE 802.3. Ethernet is a wired network, usually implemented by twisted pair wiring, but optical fibre and coaxials exist, as well. However, coaxial has been superseded, and no one uses it anymore.

Initially, the speed from the standard was 1 Mb/s but later standards increased it to first 10 Mb/s and later 100 Mb/s and 1 Gb/s. The latter two remain the most popular connection speeds today.

Ethernet works with cable lengths of up to 100 meters. When connected to a switch, Ethernet allows the maximum segment length to span 200 meters.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ethernet-segment.png)<span>Ethernet segment</span></span>

## Ethernet connection speeds

Since introducing the initial standard, IEEE has improved Ethernet by making it faster and cheaper and has released subsequent standards covering these improvements.

| Speed     | Name       | Standard     | Year | Description |
|-----------|------------|--------------|------|-------------|
| 10 Mb/s   | 10BASE-5   | IEEE 802.3   | 1983 | First Ethernet standard, used thick coaxial cable. |
| 10 Mb/s   | 10BASE-2   | IEEE 802.3a  | 1985 | Superseded the first coaxial by using thinner and cheaper cable. Newer versions of IEEE 802.3 make both obsolete now. |
| 10 Mb/s   | 10BASE-T   | IEEE 802.3i  | 1990 | Became most popular Ethernet by replacing problematic coaxial cables. Uses CAT-3 twisted pair cable. |
| 100 Mb/s  | 100BASE-TX | IEEE 802.3u  | 1995 | Standard called "Fast Ethernet", uses CAT-5 twisted pair cable. |
| 1000 Mb/s | 1000BASE-T | IEEE 802.3ab | 1999 | Increased the speed to 1 Gb/s by using CAT-5e cable. Together with 100BASE-TX remain the most popular standards today. |

Today, most Ethernet devices are capable of automatically negotiating connection speeds of 10/100/1000 Mbit/s with the switch. However, embedded devices rarely support 1 Gb/s connection speed.

## Ethernet frames

Ethernet framing has remained nearly untouched after its initial introduction, making it possible to connect devices with various speeds to the same Ethernet segment. Mbed OS only uses Ethernet for carrying IP frames.

<span class="images">![](https://s3-us-west-2.amazonaws.com/mbed-os-docs-images/ethernet-frame.png)<span>Ethernet frame</span></span>

**Fields in frame:**

DST: 48 bit destination MAC address

SRC: 48 bit source MAC address

Type: Originally this was length field, but later used as specifying the content type of payload. Also known as EtherType.
    Values higher than 1536 are registered type specifiers. Most common is 0x0800 for IPv4 and 0x86DD for IPv6.

Q-Tag: Optional virtual lan ID.

FCS: Frame Check Sequence is used for integrity check. Implemented as CRC-32

## Follow-up information

To understand the use of Ethernet and TCP/IP in Mbed OS, please see the following sections:

- [IP networking](ip-networking.html).
- [Ethernet API](../apis/ethernet.html).
- [Socket API](../apis/socket.html).
