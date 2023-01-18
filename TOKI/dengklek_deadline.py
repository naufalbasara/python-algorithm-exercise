def deadline(seconds):
    print(seconds//3600)
    print((seconds%3600)//60)
    print(seconds%60)


if __name__ == "__main__":
    deadline(int(input()))