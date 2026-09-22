
# Generated file, do not edit
from __future__ import annotations
import struct
import zlib
import binascii

UCD_VERSION = (18, 0, 0)

version_map = {1: (1, 1), 2: (2, 0), 3: (2, 1), 4: (3, 0), 5: (3, 1), 6: (3, 2), 7: (4, 0), 8: (4, 1), 9: (5, 0), 10: (5, 1), 11: (5, 2), 12: (6, 0), 13: (6, 1), 14: (6, 2), 15: (6, 3), 16: (7, 0), 17: (8, 0), 18: (9, 0), 19: (10, 0), 20: (11, 0), 21: (12, 0), 22: (12, 1), 23: (13, 0), 24: (14, 0), 25: (15, 0), 26: (15, 1), 27: (16, 0), 28: (17, 0), 29: (18, 0)}
VersionSpan = struct.Struct('HB')

def iter_spans():
    start = 0
    for count, packed_ver in VersionSpan.iter_unpack(VERSION_SPANS):
        stop = start + count
        if packed_ver:
            yield (start, stop, *version_map[packed_ver])
        start = stop + 1

VERSION_SPANS = zlib.decompress(binascii.a2b_base64(
b'eNqdWUusXWUV/vY++/24d+9zzr77nHv2bil90HL7gtKWh6UiFghEK1IoqEgCcSD4'
b'SDQa48QwkIE40cSBODIGpw4ICRNjjDpwxAhnhoSxxmjCwIHW9X3/3veetkCIDaz8'
b'Z+3/sf71/NZ/3/e8CYIeXowAiIC4RuAjzpCUSJ+GFyDwEJ+EBwSpflaIL8FLND9G'
b'HCCx+Z4mFIgmyGzskdo/z0cKfqom3F080ZnoDmkmvp0S6VNwM625YWgbBIgnSIyT'
b'i/+AqBsf1Vae9rEb3cUlkbdGgXTFQRCTJsYMkW5yslFbmHsoYlQm1eFBzl6CzY+I'
b'YhCy9zintM8VfCAp4Kf8lCakvs+de5N1G6ZY+zcP4GXABLFWVQHsl13BFBhrbKs2'
b'gYVjAsWSSs6mVB0NEZJflLrCw5I/kCQboj05sbOL2a4kRa+F25TWRIx7JDWy07KX'
b'SXAvUvHnJ3hlbCC3JSsUunNh/2eY2dR9FKnzsOCOWMX8SfkzlCEqD7XJHGOaos34'
b'ab6BKVBvaw6Q+xQvlhWKmmM7pZDk1PNCHhLwuEqaNydJRCsthGwEGQ6NOLvO41OZ'
b'njc4UhytzdTaJNaniZigD3mynzt6ZkOtjd1yG4Xj5BvO8q6n44nccLJ2ok+++TCl'
b'chJG1Cq90c5KB6ncnu7QgXPzWU7UdG2OP567Mdw9HieUurv9q0NeCh+tN2+QLXaq'
b'i4dg2buFIq0HWm9Ndf4YyJmED1Gk46dQF3eHTjT21qLbGzn+qCKdaImCmwfXr9Wy'
b'LNRaxhWSnOkoluM5f5jHazrZEpUSqmBYvhjTyN620Z7tzBC1ZOts5njrzGlSOmxi'
b'zpnKGz/iuMFAnrzu5rOC8Qjs+Uy6a1C595LBRnu5g9qbDio2ReWophPnRXsHKUKn'
b'E3Km8jQG3fp1QmT2KdIqWZNCKaWj1Vh5G0pl5huBvDeY0KADX14UhNytkm9YgsU9'
b'MlwH79D1hjbV6Wez+xOUoZGojbTU+NfNN1GHJcX4VYl+b45uvXQ6H41V7gceZr7F'
b'LaQmfDZhjvUnKEJxoK9zZuAgGjm+rrMxXC3TQnNCW8ssZHc5wE+ZkmcmXWXSiU0w'
b'DWRLBBeHydlYFErtVdqPI0NxcXnbti2foQ/kD4o+Tj3kEfdM7hd1up2Mmt/VtuMc'
b'uWnOvo+xyu3v+Fsaf8iqxO0/FcejgyUrWX+JxGx9hV/NkUz5te6Zf8cPEuSd5nyO'
b'RbOK6HxGFpFoorjbQpTQoaN8+Gqqj2RIcr6kqiTPdB5lOcSZY+E4Vzme24JjgyFw'
b'CXlKT4tVZ61sWMoaqG3lc2YshzGIYmOrGvlkvEXKi+fKPMl+xCt+5fh+1bhO9S5D'
b'rpmk5VABzc/bEosN1rs+Rxegt3z7GAN2obusjjOQbby6nfFV5ozN8gwBgym5OE+m'
b'7UN6J7IEU1tid7ldtcZnPilt5q0U1TLcTFdrbMJLiK/SfIZMsg1ipJlOnCrMWRZf'
b'E6gwTPWMQrtRRISih9fG8fUhtkv36etdGqskoRxXgcfsFk0IvcDBPCWiKCTSMPeO'
b'5eFRhCSgZTP51aZC274S5xjiCFh2Cx+9KgVLtD8gMYsLuQY2fN66xnDHTpMhaBfI'
b'o5IJFW56wN1iqlwmG/qk5GnqzU8NsDCdUBJTUW3W/4LgaI7on6wgA4z83jAzMjh0'
b'RhfJWFlsnzxDEVHbpufZIZ3lY9WozBnO+xG8mZDwz+CliC4LG8eIZsJaQpKMrye1'
b'MFcGSIWEM/Idkow3OU5TyWyiplLCdFCFcYqW48qldBXBYqXxrUOSH/j+MM6Fc0xs'
b'XnCf+K3mlKLRoL1SBiq1G6G44dtrCK55BvyIJM3TAia09CgFIxa1TLVUnt9P61jx'
b'ag+w5s5zuajw8GyB+QT1BjFwc5L3WjhaIPVlBSXMNNTdX+QppgHmyeNIbsiZZ2nK'
b'UjXXwVpizi0k9DBN/vh0P7KWt7ZDLa1RjJQ7212mARHsXMWF6NSjx/YrZgkK8rQq'
b'2jsIlkwsVvu2zw9gOxo7Djwx5HYXX9Gz8nb7dttQkWfqCCC+wXev5XLDt63ZfUaR'
b'Vrr5tum/k9vYj4Pwcho9NpdeDczkDkI7S5VWXl2TtfVdjZ/XhH3CXW8urfNqLyJ+'
b'/XGvYaBlMfcpE9Rz3bRA62Px44C5ulbcbcrzc1F/6Owsn+MU8h0vm0l7Qua2Vbli'
b'NnOxWV5FHrOU0J0Czklf1ExVB6salvqqlD9LhfNUcLpS1ZiHrOzWL1j1N3lWntqH'
b'ERFZUl0Y03KFMnkv01sSMOu0gkOlGoRsh8a15UOKPo/U5Pm04FlMexEorhT4duIT'
b'yAR0sk5p/zPK85kqgrniPlWQc0zItrsDSJmcIVtxTvUp5C1Nnm+hTGnrwluj8skC'
b'Iz3FaLVDTVReUJ0gLqN2bZST9lc7fk7tUYDTotdi/8Q2Acy9NARnfhXJYcHyXLBH'
b'oREsRni5DqF36UvwNinDYhPd1zwbLy7SPbqzRIBU736E6oIjVVubFqUqiEogmYLC'
b'XMW5dJyOyd9ByslQAlzaxCtrnc6zo/P7Y6FZpw7YR2OXoU4nUOa3q9Hhl6JTURcC'
b'G6rdlosOAN8XwvdV2Y+rsltH/CjzA0NYpT9znmDucRI4gexlOhOL7GmViZVeFfbx'
b'ZcAGYcLdZtsIVXktuVk/E7uu5yD92c5NjrFuhiaM0csDMiEmOShQ7ehtqGzZGba6'
b'UMO7kOQLXdPhgYXc7AP4PheuzLLnvCohGrZgMSGqlkrjnGOiCcOkv0hmPHaj2BkV'
b'pSsP/EYubUjsfkmVoDpFldaaWQf0mXpJcJJrVboUiAKxa3eY4VMqFsxvy01BuxOs'
b'mImWJyqxiTAb6TaV7xAL1ZWQOVe1s5RuGSO3GrGfSLUSJOMFz+pch6y2kWvDvBZW'
b'tPjKqZnqMvAI8nOERnUhGgln3kZcZPq3vGFGWWmflTrk1ds0ay51tRKvFZCz7Gpj'
b'm9lJ532CrmHTaptYMBrTPi3dtscwb+iBi8P0k3bGqGwSpgirqrbGugaHYKsHeJDB'
b'UbiXgYXKU8pXDgNOpSCT5bq5mjXePeF1TKu1slabDq86tfq6SpCGaed2pUeT5wJF'
b'de1nrYir5Ta1XMiad9wrX02ZRTlHeZU+oytXaq4q3beS1SolikobzpO1ab6oHgQg'
b'kaDAJ1U7RNlSZmC+52jmSo9dK3wQf7LG90a7mIqfYWy2yvxw+V89YNuzQatk0Op1'
b'OgaPNlXMUB9gAnen844FplN5prrFRThqe4aVanTtDLEhaLdJb1m8BdyH+QvA5+VU'
b'oIO13tDhmq5aCdnq7WsY68mpJQhDe4lzGjl/o/rdbFPamcLc0HizpYJusKHgiYu7'
b'5cApm9D+Ctd2V9kqrkopJGRE8PrHRUs+gpnzma0tRqay18B/hMqfSZ6ZAnzmD+3/'
b'wEkkQ4pZyIiYi096aG0cKgZdmOygm3DchXqu+TvdlV8r9ctHsfRpPBuvrkg5liTv'
b'YKPNxvwbk/SYqvxXgOeRCuD1Ao1mmv4PqJW1esOyzxPa4SRR0jJB02Fpk17bZEfz'
b'kF+/tY17sPpThLt9g51wRTZVTjA//KzyWyqz9vKBUDnwkmi65slzuegU1W88bUgY'
b'P2dnSNhAukO3KfWYACFPAzyNLlteHHyPtgMxHi0eoDNz/601+EcoYlb7lz99zzN+'
b'f1BenaBt1OJ9GfgWOrvjTybEIXei7/aZw9+Y4Q3wdN5swrv0yhXLjlHWyPGWJWOk'
b'0SsxXrVpKV7UjQqFWzK4UCX/rL64iX8rcdmnNzy60JaSmDVBsWhFeXq5KPHqlrLT'
b't7G4D3gfYcrME+qBLnsDYcZMvpijv8TWw0zcX6BX8XFpRuiOpxAnjL40wvwVdvdM'
b'CQ+JetyHbuWN44n4uShExYn15I5PjhxdJJSKQuWI3ZmWW4a1/vj1cS9U28jkfIBj'
b'voPdgfBV3/oIBGMOvMzA6d+b8LU55LP58ikhQ8vtZ2UXPXCZxafKY1PJP9WJZmVc'
b'wPIW2eKbDEZD+xZ0jWp6I29sLnrcueL7VaOy2LztWWlYvsP8vJJfrX5HH+70dNUp'
b'y3Xvjm4wWXMGV+j/KINuojoKPEpJGsXjVMdNLQYexPwx4BNofs/lpapqqU1KjE2Q'
b'+/OBCscwByOVHsvJGmeX+h+yz4fR9ZnulGjtxPVz0+HPGWUwnhKMnDPax7bY0YPb'
b'C8hyqqIQiiv01M+fjjq0kxEMWAi0quBz1/BmouOzRqGecaABO45CHW6hJq6Q5Ozd'
b'knGVN65KWb73xvVQjPpzLBzD5gVzdZ6ML6UJd2Ysl3Tu2c/5hFjklNAKJa9wafgz'
b'RD0T/5B+BjyIZd04lZ4LYtT3D1cmfVN0QtmYVC9oMFEHaqtaykYAcFT0SW0IYjDX'
b'OhXS/I3U8dWAmA8M/N1xriNMTlPmKYmtdGqpYKpq0qgCmif3LkH5TOOV/lxi1M0Z'
b'irXP3FIYOJmwL1teoeT2aempO8uHlLvY4GsYE/v5sbKHIzzuB+Bh+Gcl52dxNDx2'
b'hMtnwu0Gt0zDzNIxezdjUoZcUSNq1ZB/NirGbt1WTVj6WzWMcwWXVQQDjVMzXKZP'
b'oRzDQlsFsdH1De81cgOD3yzlCzaGtrbTn9zm3pCoTaSlsvdCf31wTdxSaIePUVKd'
b'ZeZmSjFszjIaB5pja9llY0BKnUp5r7+RcaY6WTezx96fzIb9jan5XaRpHl/M8FNh'
b'lXNoD2GVynY+O0D/L78OBW+srcNdVa4stAzR/ZVuwM1f3jK3ZJU83c8snX7d3/6l'
b'IWA/fJfvev6jMyt5eK5a/rnqfvgLXDze/5bPTP5/rv3/1KV3O/s5hD8A/oG4/C+u'
b'XfPtP/v6P2+dCJk='
))
