#ANOX HERE
#----------------------------------------------
import marshal, base64, zlib
exec(marshal.loads(zlib.decompress(base64.b64decode(b'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'))))