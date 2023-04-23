from reedsolo import RSCodec

def encode(infile,outfile):
    rs = RSCodec(255-223)

    output = open(outfile, "wb")

    with open(infile, "rb") as input:
        while True:
            chunk = input.read(-1)#223)
            if not chunk:
                break
            print(chunk)
            print("----------")
            data = rs.encode(chunk)
            print(data)
            print("----------")

            for ii in data:
                #print(bin(ii)[2:])
                #output.write(bytes(bin(ii)[2:],'utf-8'))
                output.write(bytes( '{0:0{1}b}'.format(ii, 8), 'utf-8' ))
                print(bytes( '{0:0{1}b}'.format(ii, 8), 'utf-8' ))

    output.close()

def decode(infile,outfile):
    rs = RSCodec(255-223)

    output = open(outfile,"wb")

    with open(infile, "rb") as input:
        while True:
            chunk = input.read(-1)#256*8)
            if not chunk:
                break
            chunk=chunk.replace(b'\n',b'')#no newlines
            chunk=chunk.replace(b'9',b'0')
            chunk=chunk.replace(b'8',b'0')
            chunk=chunk.replace(b'6',b'0')
            chunk=chunk.replace(b'o',b'0')
            chunk=chunk.replace(b'e',b'0')
            chunk=chunk.replace(b' ',b'1')
            chunk=chunk.replace(b'|',b'1')
            print(chunk)

            datastr = bytearray()

            for i in range(0, len(chunk), 8):
                byte = int(chunk[i:i+8], 2)
                #print(hex(byte))
                #datastr += chr(byte)
                #print(hex(int(ord(datastr[-1]))))
                datastr.append(byte)

            print(datastr)
            print("-----")

            #data = rs.decode(datastr.encode('utf-8'))
            data = rs.decode(datastr)
            print(data)
            output.write(data[0])

    output.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('infile')
    parser.add_argument('outfile')
    parser.add_argument('-e', '--encode', action='store_true', help='encode a file')
    parser.add_argument('-d', '--decode', action='store_true', help='decode a file')
    args = parser.parse_args()

    if args.encode:
        encode(args.infile,args.outfile)
    elif args.decode:
        decode(args.infile,args.outfile)
    else:
        print("no operation specified")
