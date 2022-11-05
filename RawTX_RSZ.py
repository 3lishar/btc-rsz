import bitcoin
import hashlib
import txnUtils
import keyUtils

tx = "01000000011330411f54242ac02d3f1978413063424de00d2769262b2fa26cc2deeb873806000000006a473044022075d6447622472df4c8c3a6a434ffb527f5c468169b3365dd7029ce0dfb4e1105022008b5b4391f34e02c17ba1f0a59d224cf18a74460cf4ee2f2abba58630f1dcf99012102b0ff8748d965aa62c073b7824f4366b4b3dc671ca2488f1c22428537ecff2fd1ffffffff028047a1190000000017a9146f9bf6508731196724bba2e43a619c89cfb41f1287c864dd0e5d0000001976a9148925f039ec9593bcbcf71fb3236c45de9161b07888ac00000000"

m = txnUtils.parseTxn(tx)
e = txnUtils.getSignableTxn(m)
z = hashlib.sha256(hashlib.sha256(e.decode('hex')).digest()).digest()
z1 = z[::-1].encode('hex_codec')
z = z.encode('hex_codec')
s = keyUtils.derSigToHexSig(m[1][:-2])
pub =  m[2]
sigR = s[:64]
sigS = s[-64:]
sigZ = z
print ('Signed TX is :', tx)
print ('Signature (r, s pair) is :', s)
print ('Public Key is :', pub)
print ("")
print ("#################################################################################################")
print ("")
print ('Unsigned TX is :', e)
print ('hash of message (sigZ) is USE This ONE :', z)
print ('reversed z :', z1)
print ("")
print ("#################################################################################################")
print ("##################################VALUES NEEDED ARE BELOW #######################################")
print ("#################################################################################################")
print ("")
print ('THE R VALUE is  :', sigR)
print ('THE S VALUE is  :', sigS)
print ('THE Z VALUE is  :', sigZ)
print ('THE PUBKEY is :', pub)


