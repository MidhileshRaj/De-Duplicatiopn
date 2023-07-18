fileid=2

import pyAesCrypt
password = "please-enter-a-long-random-password"
blocksize= 1024* 1024
from DBConnection import  Db
db=Db()

qry="SELECT `filesize`,filename FROM `files` WHERE `fileid`='"+str(fileid)+"'"
res= db.selectOne(qry)

totalsize= int(res['filesize'])
filename= res['filename']



qry="SELECT `blockid` FROM `fileblockindex` WHERE `fileid`='"+str(fileid)+"' ORDER BY `indexid`"



res=db.select(qry)
byt1=[]
for i in res:

    qry="SELECT filename FROM `block` WHERE `blockid`='"+str(i['blockid'])+"'"
    res2= db.selectOne(qry)

    s="D:\\kabu\\final\\cloud_deduplication\\static\\blocks\\"+ res2['filename']

    pyAesCrypt.decryptFile(s, "a.txt", password)

    with open("a.txt", "rb") as h:
        temp = h.read()

        print(type(temp),len(temp),len(byt1))

        byt1.extend(temp)



with open("download"+filename,"wb") as h:
    import numpy

    h.write(bytearray(byt1))









