# HackIM Crypto 2 - 400pts

>Some one was here, some one had breached the security and had infiltrated here. All the evidences are touched, Logs are altered, records are modified with key as a text from book.The Operation was as smooth as CAESAR had Conquested Gaul. After analysing the evidence we have some extracts of texts in a file. We need the title of the book back, but unfortunately we only have a portion of it...

## Write-up

This challenge was also pretty simple, they provided some cipher text and the word `CAESAR` is capitalized in the description, so naturally I just shifted all the characters by one character 26 times and looked for the one that made sense. There's clearly a bug in the `caesar()` implementation, but this was enough to extract the passage  ¯\_(ツ)_/¯. Taking that to a quick google search heeded the flag `In the Shadow of Greed`

Flag:
> In the Shadow of Greed

```python
import string

def caesar(plaintext, shift):
    alphabet = string.ascii_lowercase
    shifted_alphabet = alphabet[shift:] + alphabet[:shift]
    table = string.maketrans(alphabet, shifted_alphabet)
    return plaintext.translate(table)

for x in range(26): print "%d, %s" % (x,caesar(a,x)[:100])
"""
0, Nb. Ckbkr De bkmoc kqksxcd dswo dy lvymu dro wycd nkxqobyec Sxdobxod wkvgkbo ofob mbokdon, k lydxod
1, Nc. Clcls Df clnpd lrltyde etxp ez mwznv esp xzde olyrpczfd Syepcype xlwhlcp pgpc ncplepo, l mzeype
2, Nd. Cmdmt Dg dmoqe msmuzef fuyq fa nxaow ftq yaef pmzsqdage Szfqdzqf ymximdq qhqd odqmfqp, m nafzqf
3, Ne. Cnenu Dh enprf ntnvafg gvzr gb oybpx gur zbfg qnatrebhf Sagrearg znyjner rire perngrq, n obgarg
4, Nf. Cofov Di foqsg ouowbgh hwas hc pzcqy hvs acgh robusfcig Sbhsfbsh aozkofs sjsf qfsohsr, o pchbsh
5, Ng. Cpgpw Dj gprth pvpxchi ixbt id qadrz iwt bdhi spcvtgdjh Scitgcti bpalpgt tktg rgtpits, p qdicti
6, Nh. Cqhqx Dk hqsui qwqydij jycu je rbesa jxu ceij tqdwuheki Sdjuhduj cqbmqhu uluh shuqjut, q rejduj
7, Ni. Criry Dl irtvj rxrzejk kzdv kf scftb kyv dfjk urexviflj Sekvievk drcnriv vmvi tivrkvu, r sfkevk
8, Nj. Csjsz Dm jsuwk sysafkl laew lg tdguc lzw egkl vsfywjgmk Sflwjfwl esdosjw wnwj ujwslwv, s tglfwl
9, Nk. Ctkta Dn ktvxl tztbglm mbfx mh uehvd max fhlm wtgzxkhnl Sgmxkgxm fteptkx xoxk vkxtmxw, t uhmgxm
10, Nl. Culub Do luwym uauchmn ncgy ni vfiwe nby gimn xuhayliom Shnylhyn gufquly ypyl wlyunyx, u vinhyn
11, Nm. Cvmvc Dp mvxzn vbvdino odhz oj wgjxf ocz hjno yvibzmjpn Siozmizo hvgrvmz zqzm xmzvozy, v wjoizo
12, Nn. Cwnwd Dq nwyao wcwejop peia pk xhkyg pda ikop zwjcankqo Sjpanjap iwhswna aran ynawpaz, w xkpjap
13, No. Cxoxe Dr oxzbp xdxfkpq qfjb ql yilzh qeb jlpq axkdbolrp Skqbokbq jxitxob bsbo zobxqba, x ylqkbq
14, Np. Cypyf Ds pyacq yeyglqr rgkc rm zjmai rfc kmqr bylecpmsq Slrcplcr kyjuypc ctcp apcyrcb, y zmrlcr
15, Nq. Czqzg Dt qzbdr zfzhmrs shld sn aknbj sgd lnrs czmfdqntr Smsdqmds lzkvzqd dudq bqdzsdc, z ansmds

16, Nr. Carah Du races against time to block the most dangerous Snternet malware ever created, a botnet
                   ^---- Ding ding ding!

17, Ns. Cbsbi Dv sbdft bhbjotu ujnf up cmpdl uif nptu ebohfspvt Soufsofu nbmxbsf fwfs dsfbufe, b cpuofu
18, Nt. Cctcj Dw tcegu cickpuv vkog vq dnqem vjg oquv fcpigtqwu Spvgtpgv ocnyctg gxgt etgcvgf, c dqvpgv
19, Nu. Cdudk Dx udfhv djdlqvw wlph wr eorfn wkh prvw gdqjhurxv Sqwhuqhw pdozduh hyhu fuhdwhg, d erwqhw
20, Nv. Cevel Dy vegiw ekemrwx xmqi xs fpsgo xli qswx herkivsyw Srxivrix qepaevi iziv gviexih, e fsxrix
21, Nw. Cfwfm Dz wfhjx flfnsxy ynrj yt gqthp ymj rtxy ifsljwtzx Ssyjwsjy rfqbfwj jajw hwjfyji, f gtysjy
22, Nx. Cgxgn Da xgiky gmgotyz zosk zu hruiq znk suyz jgtmkxuay Stzkxtkz sgrcgxk kbkx ixkgzkj, g huztkz
23, Ny. Chyho Db yhjlz hnhpuza aptl av isvjr aol tvza khunlyvbz Sualyula thsdhyl lcly jylhalk, h ivaula
24, Nz. Cizip Dc zikma ioiqvab bqum bw jtwks bpm uwab livomzwca Svbmzvmb uiteizm mdmz kzmibml, i jwbvmb
25, Na. Cjajq Dd ajlnb jpjrwbc crvn cx kuxlt cqn vxbc mjwpnaxdb Swcnawnc vjufjan nena lanjcnm, j kxcwnc
"""
```
