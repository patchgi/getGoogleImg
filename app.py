from googleImg import GoogleImg as GI

def main():
    th1 = GI("猫")
    th2 = GI("犬")
    th1.start()
    th2.start()

if __name__ == "__main__":
    main()
