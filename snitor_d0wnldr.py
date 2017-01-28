import requests, sys, socket, socks

def usage():
    message = '''
    *************************************************************************************************************
                                                     snitor_d0wnldr

             Hi I Can Download Your Files Through Tor :)
        1) Just Run python '''+sys.argv[0]+'''
        2) Add The link Of Your File At The End of Step1
        3) Enjoy Your Results ^__^

                                                                                       Coded By Alae Larheribi
                                                                        Email: snipeo.1998@gmail.com | Snî-PeO
    *************************************************************************************************************
    '''
    print(message)
    print("usage : \n\t"+sys.argv[0]+" [WEBSITE]\n Ex : python " +sys.argv[0]+ " http://www.pdf995.com/samples/pdf.pdf")
socks.setdefaultproxy(proxy_type=socks.PROXY_TYPE_SOCKS5, addr="127.0.0.1", port=9050)
socket.socket = socks.socksocket


def download(lien):
    filename = lien.split('/')[-1]
    try:
        print('Your Download Will Be Establish From This IP>>> ' + str(requests.get("http://ident.me/").text))
        r = requests.get(lien, stream=True)
        if r.status_code == requests.codes.ok:
            with open(filename, 'wb') as z:
                for chunk in r.iter_content(chunk_size=1024):
                    if chunk:
                        z.write(chunk)
        print("Done ^_^")
        return filename
    except:
        print("Maybe The File Or the Website is Not Available")

if __name__ == '__main__':
    if len(sys.argv) <=1:
        usage()
    else:
        lien=sys.argv[1]
        download(lien)
