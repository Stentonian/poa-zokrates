import hashlib

from zokrates_pycrypto.eddsa import PrivateKey, PublicKey
from zokrates_pycrypto.field import FQ


if __name__ == "__main__":

    raw_msg = "This is my secret message"
    msg = hashlib.sha512(raw_msg.encode("utf-8")).digest()

    # sk = PrivateKey.from_rand()
    # Seeded for debug purpose
    key = FQ(1997011358982923168928344992199991480689546837621580239342656433234255379025)
    sk = PrivateKey(key)
    sig = sk.sign(msg)

    pk = PublicKey.from_private(sk)
    is_verified = pk.verify(sig, msg)
    print(is_verified)

    # this is for the anon set
    sk_2 = PrivateKey.from_rand()
    pk_2 = PublicKey.from_private(sk)

    # it is assumed that the size of the anon set is N=2
    # for i=1 the signature is present, and for i=2 it is not (hence the zeros)

    sig_R, sig_S = sig
    cli_args = [sig_R.x, sig_R.y, 0, 0] + [sig_S, 0] + [pk.p.x.n, pk.p.y.n, 0, 0]

    M0 = msg.hex()[:64]
    M1 = msg.hex()[64:]
    b0 = [str(int(M0[i:i+8], 16)) for i in range(0,len(M0), 8)]
    b1 = [str(int(M1[i:i+8], 16)) for i in range(0,len(M1), 8)]
    cli_args = cli_args + b0 + [0,0,0,0,0,0,0,0] + b1 + [0,0,0,0,0,0,0,0]

    # ownership array parameter
    cli_args = cli_args + [1,0]

    # balances array parameter
    cli_args = cli_args + [7,11]

    # anon set array parameter
    # the first pub key is the one that the signature is linked to, and the other is just a random pub key
    cli_args = cli_args + [pk.p.x.n, pk.p.y.n, pk_2.p.x.n, pk_2.p.y.n]

    cli_args = " ".join(map(str, cli_args))

    path = 'poa_zokrates_cli_inputs.txt'
    with open(path, "w+") as file:
        for l in cli_args:
            file.write(l)

