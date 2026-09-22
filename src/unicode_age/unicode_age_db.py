
# Generated file, do not edit
from __future__ import annotations
import struct
import zlib
import binascii

UCD_VERSION = (18, 0, 0)

version_map = {1: (1, 1), 2: (2, 0), 3: (2, 1), 4: (3, 0), 5: (3, 1), 6: (3, 2), 7: (4, 0), 8: (4, 1), 9: (5, 0), 10: (5, 1), 11: (5, 2), 12: (6, 0), 13: (6, 1), 14: (6, 2), 15: (6, 3), 16: (7, 0), 17: (8, 0), 18: (9, 0), 19: (10, 0), 20: (11, 0), 21: (12, 0), 22: (12, 1), 23: (13, 0), 24: (14, 0), 25: (15, 0), 26: (15, 1), 27: (16, 0), 28: (17, 0), 29: (18, 0)}
VersionSpan = struct.Struct('IB')

def iter_spans():
    start = 0
    for count, packed_ver in VersionSpan.iter_unpack(VERSION_SPANS):
        stop = start + count
        if packed_ver:
            yield (start, stop, *version_map[packed_ver])
        start = stop + 1

VERSION_SPANS = zlib.decompress(binascii.a2b_base64(
b'eNq1Wk2sJFUVvlVdXf/1XlV311T3q64Hw/zAMAMzOMyAKDOiDhCMIjr8qUiCcSH+'
b'JRqNcWNYyELcaOJCXBmDWxeEhI0xRl24YoU7Q8JaYzRh4ULHPuf2992+j34DRH3J'
b'65y6de655557/m+9FRgTjIwx0bD6CRKBVv8mlp+kkcdQoHz1k1arn+wJwROcKJAX'
b't8ujIEcZX9Ty4oo8pqQnlBMBU6UXcFopb4WDXMcCQPoXCHJmgFyPwBsx1tCU0GlA'
b'OfGU05jI0fWhBmyMdTF5k8i6qb4tiHcfITd2CxcPuK5K904QjYMtkMzIejxGCaBU'
b'UYSPbBekFFLyhfyUglzrzk94chm4/dlJQsYTyRBgbqVTBBSBm1QOJcyAnKWAwhBc'
b'DSqdPbNWH/2biawCURUjYwkp1/JCx1WIqhYJx5Sy7MrMHYr8lAuoVD6BMlh1HAOv'
b'rCjEByi/iLvcITTgbeL0VHW8AmQGkt+DhFQcibxIRS3yc9Rn3dc9IhzizW7DoRhZ'
b't1CicqolT6XUX9n1VMnsY9NLQZlHwOsTvLDykxmVbLoWvEZlJSgT2UyXA3km64qo'
b'TLPHufJThBBEQk0sG4wppyWlZvVqTmuMwHhNrVOTTAnVJG+ou4bqbVq+PWC6IVQl'
b'CDxzTuItVLhGmhB5RBQDKw6o6W4zUx3iGolbSJ/HPqlDeQ4Og3zuLRujLdyHwFPf'
b'ZHfupBFDcwIoiZll3s4dL24LG2+vz7MTTrZlbujvY8c7o8SfVvGM9K8ZQ8TmvetB'
b'4MkgccqQeK70oCTpr8U2TRdsUYbQDyc5RSfslpmPPObxuC2MOBZsiTiB/zb0D5nc'
b'a7izrEWHrUHS+ZhrVIDSAoE5oXtw9jZLtpzlEUI8sjryFpr7AfIgQ/HbdVzVsaEM'
b'lkrFP5ncaQl1o00wd0IP8p4Y31DbgJ7h+jxHPpPm7baaHTADOrJFgblTn93uuuyW'
b'u4TobvQsnSUfZJfRYDLC2wm9gHXh2wQrRHNFjkmZFmA3zqTNdBxjHmYY/NUGI3qk'
b'aAQz2MCjJUdjcFDTBjXtMe+neou0g+OHmYsqA1+0B14Y7K2lcFqedBseQk+Fs0G0'
b'9GcwsTs4lyezcLrmq3J1gzw+gHzI3AhIRZePkPuEApVjvjWcMUO2FMX+25CC3fGE'
b'nZO8ugxdw0ZilelRIOdMXXKeec6z1Gl6WrlsLrrskcr9FLHi6pUOnvRSU5eHKUPV'
b'k7Ct4iOEHsG5FTF4SS8Rcjo08rXugIa5tyevO3f/v6Ds+HN4Rzj2Limnjr8J3wYw'
b'+7SnRYnsU7WZq5ih5qyq1/AEim+tsCNZs1hy7idRAtQxnIQC85hQSj8uW4hTOKy4'
b'8Gao2sVUfPv2c8x86VWcdWtsdIo5d28fx9hMCZ7y1NFIsVdk8AIJ6wpNLTWob0C6'
b'eAgqCc1Ui0wd08yyGPmSzHA8BaNuKmaa9Jhhxy4x914yHxfKBalYqPKydfVrnYzN'
b'd5CPD0JmKawNmg99DGFiTpn2ZxBOdKy/Ff65KhADqvMo01SlyruAouta6H0CyeYm'
b'SlRleitz1hDxslIqN0E4miNMKexWp31ZRPI4FF2rynwHtfOU3E8YgGxC/yJLPK3F'
b'n2Swaekdx4RObBlLDnPSB6B9zriTY0x6TeVTNmD1QAlgWJEa14BgOI7HqALVkSX0'
b'ZrGIJI1gFTntfJfBRmfYulZrwggFRymLD8wibekSelW++kmaoNkJcTKN8WS/JCnD'
b'ZkNE605HUDM9N3M3UZj4pztEZuqiilSc9Roa2Qi71ENu1KI+w8aMsBr/HdnmRoPk'
b'Ox6VWAvj8xRnjqxU1y3ksYyhYapX0+PkWbjqWybg2oH4gUBTdpl+Io9CK36YPSj5'
b'iaes2dklsf75UZIvGK0ydply4LkuSbKLsSyjrFQ4GY9s4h2evi07jNUuaWPKXvYc'
b'u8lL6TbwQm+sYF2rArNi3ydex7kVodjTiIpqW5ED2zzT/tA1Ecm1YN2esF0S9QIR'
b'0oDsFmzf9mQ0ii+Y190AjdXUuTuKWmNW0Mmw3zQVXZ4J0WYHvaX2dsh57iDZfxZS'
b'E5mmZGOe0bPgVE/L5iVnQGBrrnIByl+x1nANIdtrEX+QpgjgqfnfQSKmvMPJ6BY0'
b'IbAbzMCVynQSodszY2pqOzYBvM/QI9LZTT7B7Pp1gRYIn5qj793ltcJiv3tpPu3l'
b'cM4/x0/Rwyn2zV51MmV30BBPW3JBh4W0P9SpHU2x6Z7ns6f6t6TB6uAxeSxgQok6'
b'rd5DSe9As0GTEy0kXEv5yLc59gyn7bOOf2Wx7jp3kuUmL62S0aCFu84TrFsJk82M'
b'pyDq2MmO5j+MkHM19OO79HoFodDrimu+ZsTRFqdXU/IpNYJdNV286pEBuBhQSWAu'
b'EiSf1rAjzM2eJRVmjJpZajJRZ3hRMbBM2NiqmVnOxqiKtJ+oFZXutw/YaPSrY01x'
b'5uG6W2kGZmkDjUlDlmpsx8K4YtswPw3T0IU2kixR1kz3+1E2AhLos2139AxPyr0o'
b'cM7CNl8y4fs487qc2aE6j31mmxeRRilvrmzOaWp5j7n1hwXqYD6FnEeVwWbKYAtE'
b'X1IaHzqLCKFbUOFYsbPLbiS0Na5B7CT0i5XswgIaYbd1jtC1lbDC2/ZQlt4DdbRU'
b'viRiP8GGWsGCl84ymvuNlG1NrAOQJJDBLvY2F2j5lWA9Nr8MQ1xeQLfCKpJYwJg3'
b'ITErDCUQZ0zjGRZzukg1Tue0ksxP/VzTZOQlgS5hMc9v6cI+5bu+0E9Xt0GufRf7'
b'nUp2YSNmfSps6+YWhCaEnBPcYY2jMVlCqvkuu3khq6IzrIr0duQhxDcbRFhM5c7K'
b'1BDFWRrRq/w5GLUtKc4xgex5c7aPWy19HKfgYCr57phVh6YG2llNXGf2GPyV7iM9'
b'hTpgrFtV6GGvqrS15DG2uBwksadW0udxuWF4zTGn1OY8AFdvzekA3gEvBPlereLi'
b'arBO0WtSV6qbqzuogJ17ilAKBzpcBkri3yDoVePGcfNQNvBaOi2t8i9x5/JYn4XS'
b'NKTSRLDVZoHSsiDlbMGS26DHszwBR1vRJ6ofqnbZbLgN2X/KhVKWEyl7BRbag+q5'
b'6tMefAqUGXNxTdo0+hWaO96ALk7Not+K/QL34apyWaggG0XDnof65wKnWotemQcF'
b'5SKK5aYkFLOvcjPqZNU/jYOqoj3X7Xlv0r8Ggyh48B0F0bGdoBmPjimVJXVtkG0t'
b'W1xB6JLq6hVFkReOISE/a+Et5idgl90Unr9NEeS0clCq2ll03Z76PrCrjRnjbrXm'
b'TIQz3BRqeV2xqNacYcZWtj2jFIJVzWkY2bvMu7lt2BGvWbTagHsrExHd770Qjrso'
b'aOi9GxpsQyPWqyO9RrU+J0MmY+cyz7G2ykOp2USueR41NbtmuKvJxizdQiAkxGss'
b'w00bhicLsYVrZZAhW7L3taTS8yq+N++MN9qCF/h6qur0JGJAx6zPuPyPvfVuQNu6'
b'phnUL8H87Gb08OQsm6NIy9yOrOzFtiYTehV26OdjX8OESs/apXHquMNmwy4sdP6q'
b'PH5AUL4g0Kdo4gZm3wXebYaeeUeRdLyj3xjj9XWXgrXuCua2dH0tK512DxKaMgBp'
b'B609wjJIC7YS3M/vplvKcGUwXMUay8fRnO8rHuMY3tEe1BlCFa7s1UmozajvnFCf'
b'N/AehOpNud8pw8409C6qNt6m3JssNB3DO86IZ6HjW8bG9O3OgcpqyxHGlmNevP4V'
b'jsfOqHmfIi2GRQgl17H+Ko9WU5I7cF1jr3++tqKfnWKl9EX5lYovY9thYAtElXX4'
b'neAxsg/a/XkGzQZze7T2kwuRRivCXujkF3fRXb1/xWDz6t76Bqv/g+zh7nDdcDGu'
b'pMgYy9RvfIL5QUaDGGhbY+YWVwhlW7zUjE5Gzrv+VUA20KCbRZDukg5+eRoGW/Gq'
b'zLDromVuy6OoLns+wuq4Qe/BWo+ssVTD+Uu3blTY4lE1+x8raUzeDNZ4wzF6LpnR'
b'tWySf14GvyGPKvsfjVA3SnQelvtrN3d4NqdlrtCajiDTgTFvsYSnbukeFhV8Z8sv'
b'ncwLSkCk/SylW9Jxp54R1/Qv9WfFxv/J8K7ILwcw4iMM+dqyTQjV2O9AJ2P7OUcY'
b'sb8pkDg885aoRoaoO+ZnC/nL8pgjS5uLWgxX0MxUIxnuhY3bq+kpmnHmMdlBCo+e'
b'yd5mz+PGyYay+wkFWNeaeeCPjYhXEDKE+DbhR3HmQ/5binPMQx4zyh2gojF0Y43Q'
b'n/FIsKaXGqZWRzFm7+1FLuMXwnXf0UR+bvEw3Ovw5ghfWI3xwdriMXY1NIe7QD3l'
b'tbtaz4Rxf0L5Tci9WoqRk1ncSJ38Oly9dvjUhbeshVp6kPZyAK5q3J+3TOjb14J1'
b'srh4HflVTzvvfwPftOS1+ZKZwvIN38BGW0zNlUu/pxmIAdTis81D2GVLfz8h4xP1'
b'gnL1O5N7MPNBwfstFqpYOVRcsjJ+y9Z9aMj0cmOu8SFqSDXa8vYAFL7Ldd8ttI2K'
b'4zTewv22fWTeh5VV5HMa+W/Pc11d7jQ/M5BsKS9weCU7CSU/7rMvHOQq3BylljrB'
b'jtXOzF1z5IT8C8GSvfoNKEL3suRtRsmWd0mp2R536lMOfMoZCp2DY42X6g4XkV5u'
b'sFYi5ypS/yuaFFzZmFLBiU1/io84ygLS0HTfCvGK94FjMyXecb6IwK4tiPRtzYsv'
b'EUlzyTsUC71CaAQZ2BTnXj6OeFuglDvIwJZVtxB6lGwY1PauGVxS6w6HHB7bmmpb'
b'G3gHxgoyqXJRVTlLgTGx0eA1YQbaMltXLzW4sB0iQav54adCbu5GKRMihurF62KE'
b'PvXiKqSmyIuAHevCS4r0Gl9v8G36dpdfFY39RtTglYda//Z0fTa113r/JBaasg+n'
b'hbtqk820EvS4FcXuraBnJaQZvP1gt/RviJTyCMVUxzb9jK5Zs0NtgUxUvXMij2l+'
b'GmyYxrc8KO1HtDQwbZTZ4meO9ruuseTn27PAS7d00wtmZHN+0eha3gtWuPaqm8qg'
b'WVU7wQZ17iL2HzlX17A3NcaropcsfgZ+O22p8JbCURnM2z+q3uBPUUhvGZNAgNt/'
b'82PWnOKMOnEKfUYdD9FXD//0y5W3YSGrDXFzZ73u5Nt1ZfvLP8PALGvPHVk7FJvp'
b'n1uNTjWx+eqKrb2fZ2sGx2/gi4jwoek6KTdPr8gv/rj6WX7/Z6vHy6v8Y/g1rqrD'
b'f137/0MukdPdPC3Q9wT6m35c/2/FC034H9Y9BJs='
))
