import ddddocr

def main(ImagePath):
    with open(ImagePath, 'rb') as f:
        res = ddddocr.DdddOcr().classification(f.read())
    return res

if __name__ == '__main__':
    main()