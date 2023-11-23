# What to do

You need to have the following Python library cloned and installed: https://github.com/Zokrates/pycrypto/tree/master

```bash
git clone https://github.com/Zokrates/pycrypto.git
cd pycrypto
pip install -r requirements.txt
```

From within the pycrypto repo you can generate an EdDSA signature:

```bash
# Generate private key (field element) and public key (point on BabyJubJub curve)
python cli.py keygen
# => Private and public key
# => 37e334c51386a5c92152f592ef264b82ad52cf2bbfb6cee1c363e67be97732a ab466cd8924518f07172c0f8c695c60f77c11357b461d787ef31864a163f3995

# Generate EdDSA signature
# python cli.py sig-gen <pvt_key> <message>
python cli.py sig-gen 37e334c51386a5c92152f592ef264b82ad52cf2bbfb6cee1c363e67be97732a 11dd22
# => Signature_R Signature_S
# => 172a1794976d7d0272148c4be3b7ad74fd3a82376cd5995fc4d274e3593c0e6c 24e96be628208a9800336d23bd31318d8a9b95bc9bd8f6f01cae207c05062523

# Verify EdDSA signature
# python cli.py sig-verify <public_key> <message> <signature_r> <signature_s>
python cli.py sig-verify ab466cd8924518f07172c0f8c695c60f77c11357b461d787ef31864a163f3995 11dd22 172a1794976d7d0272148c4be3b7ad74fd3a82376cd5995fc4d274e3593c0e6c 24e96be628208a9800336d23bd31318d8a9b95bc9bd8f6f01cae207c05062523
# => True
```

From within this repo you can generate the ZoKrates input values for the CLI..

```bash
python test.py
```

..which you can then use to compute a witness, generate a proof, and verify it:

```bash
cat zokrates_inputs.txt | xargs zokrates compute-witness -a
zokrates generate-proof
zokrates verify
```
