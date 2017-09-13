from googleImg import GoogleImg as GI

def main():
    img1 = GI("お金 ほしい")
    img2 = GI("犬")
    img1.start()
    img2.start()

if __name__ == "__main__":
    main()
