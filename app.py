from googleImg import GoogleImg as GI

def main():
    th1 = GI("hoge1", 1)
    th2 = GI("jaj", 1)
    th1.start()
    th2.start()

if __name__ == "__main__":
    main()
